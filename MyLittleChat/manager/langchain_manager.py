from operator import itemgetter
from langchain_community.document_loaders import TextLoader
from langchain_google_genai import GoogleGenerativeAIEmbeddings
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_community.vectorstores import FAISS
from langchain_community.vectorstores.utils import DistanceStrategy
from langchain_core.documents import Document
from langchain_core.vectorstores import VectorStore
from langchain_core.language_models.chat_models import BaseChatModel
from langchain.retrievers.multi_query import MultiQueryRetriever
from langchain_community.chat_message_histories import ChatMessageHistory
from langchain_core.runnables.history import RunnableWithMessageHistory
from typing import List

import os

class LangchainManager:
    """
        1. RAG 문서 제작\n
        2. 임베딩\n
        3. FAISS에 대입해 유사성 검색\n
        4. 채팅
    """
    _instance = None
    _store = {}
    _vectorstore: VectorStore = None
    def __new__(self):
        if not self._instance:
            self._instance = super().__new__(self)
        return self._instance


    # 해당 디렉토리의 모든 파일명을 가져오는 함수
    def _get_all_files_in_directory(self, dir):
        # 해당 디렉토리의 모든 파일 리스트 가져오기
        files = [os.path.join(dir, file) for file in os.listdir(dir)]
        return files

    # 1. rag 문서 리스트를 만들고, split 한다
    def _make_docs(self) -> list[Document]:
        result: list[Document] = []
        docs: list[Document] = []
        folder_path = "./rag_documents"

        # 폴더 내의 모든 텍스트 파일을 불러온다
        file_paths = self._get_all_files_in_directory(folder_path)
        for file_path in file_paths:
            print(f"문서 읽음: {file_path}")
            data = TextLoader(file_path, encoding="utf-8").load() # 텍스트 로더를 통해 도큐먼트화
            docs.extend(data)
        
        # 텍스트 쪼개기 준비
        text_splitter = RecursiveCharacterTextSplitter(
            chunk_size = 500,
            chunk_overlap = 0
        )
        result = text_splitter.split_documents(docs)
        return result
    
    # 도큐먼트 리스트를 하나의 긴 문자열로 변환
    def format_docs(self, docs: list[Document]) -> list[str]:
        return "\n\n".join([doc.page_content for doc in docs])
    
    # 2. 도큐먼트 리스트를 임베드하여 벡터스토어로 변환
    def _make_vectorstore(self, docs: List[Document]) -> VectorStore:
        embeddings_model = GoogleGenerativeAIEmbeddings(
            model="models/text-embedding-004"
        )
        vectorstore = FAISS.from_documents(
            documents=docs,
            embedding=embeddings_model,
            distance_strategy = DistanceStrategy.COSINE
        )
        return vectorstore
    
    def get_session_history(self, session_token: str):
        if session_token not in self._store:
            self._store[session_token] = ChatMessageHistory()
        return self._store[session_token]

    # 채팅 프로세스
    def chat(self, llm: BaseChatModel, session_token: str, message: str):
        # 3. 검색기를 만든다
        if self._vectorstore is None:
            self._vectorstore = self._make_vectorstore(self._make_docs())
        # retriever = self._vectorstore.as_retriever()
        retriever = MultiQueryRetriever.from_llm(
            llm = llm,
            retriever= self._vectorstore.as_retriever(
                k=5,
                fetch_k=50
            )
        )

        # 4. 프롬프트를 만든다
        # system_prompt = (
        #     "채팅 기록과 채팅 기록의 맥락을 참조할 수 있는 최신 사용자 질문이 주어졌을 때,"
        #     "채팅 기록 없이도 이해할 수 있는 독립적인 질문을 만들어 보세요."
        #     "질문에 답변하지 말고 필요한 경우 재구성하고 그렇지 않은 경우 그대로 반환하세요."
        # )
        prompt = PromptTemplate.from_template(
            """
            자유롭게 말해. 500자 이내로 대답해.
            이전 채팅 기록과 배경 지식이 존재해도 질문과 관련이 없으면 반영할 필요 없어.
            질문과 배경 지식은 너만 알고 있고, 유저에게 대답할 때에는 독립적인 문장으로 재구성해서 답변해줘.

            #이전 채팅 기록:
            {chat_history}
            
            #질문:
            {question}

            #배경 지식:
            {context}

            #답변:
            """
        )

        # 5. LLM 정의

        # 6. 체인 생성
        chain = (
            {
                "context": itemgetter("question") | retriever,# | self.format_docs,
                "question": itemgetter("question"),
                "chat_history": itemgetter("chat_history")
            }
            | prompt
            | llm
            | StrOutputParser()
        )

        # 7. 채팅 기록 붙이기
        chain_with_history = RunnableWithMessageHistory(
            chain,
            get_session_history=self.get_session_history,
            input_messages_key="question",
            history_messages_key="chat_history"
        )

        # 대화
        response = chain_with_history.invoke(
            {"question": message},
            config={
                "configurable": {
                    "session_id": session_token
                }
            }
        )

        # 결과
        return response