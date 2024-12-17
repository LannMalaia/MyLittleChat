from langchain.document_loaders import TextLoader
from langchain_text_splitters import CharacterTextSplitter
from langchain_core.embeddings import Embeddings
from openai import OpenAI
from typing import List

import os

class LangchainRagMaker:
    # 해당 디렉토리의 모든 파일명을 가져오는 함수
    def _get_all_files_in_directory(self, dir):
        # 해당 디렉토리의 모든 파일 리스트 가져오기
        files = [os.path.join(dir, file) for file in os.listdir(dir)]
        return files

    def load(self):
        result = []

        # 파일 선택 창을 띄워서 파일을 선택한다. 이 때 엑셀 파일로 한정한다.
        # root = tk.Tk()
        # root.withdraw()
        # folder_path = filedialog.askdirectory(initialdir="./")
        folder_path = "./rag_documents"

        # 폴더 내의 모든 텍스트 파일을 불러와 RAG 문서화 한다.
        text_splitter = CharacterTextSplitter(
            separator="\n",
            chunk_size = 300,
            chunk_overlap = 50,
            length_function = len
        )
        file_paths = self._get_all_files_in_directory(folder_path)
        for file_path in file_paths:
            data = TextLoader(file_path, encoding="utf-8").load()
            texts = text_splitter.split_text(data[0].page_content)
            result.append(data)
        return result
    
class Embedder(Embeddings):
    def __init__(self, base_url, api_key="lm-studio"):
        self.client = OpenAI(base_url=base_url, api_key=api_key)
    
    def embed_documents(self, texts: List[str], model="nomic-embed") -> List[List[float]]:
        texts = list(map(lambda text:text.replace("\n", " "), texts))
        datas = self.client.embeddings.create(input=texts, model=model).data
        return list(map(lambda data:data.embedding, datas))
        
    def embed_query(self, text: str) -> List[float]:
        return self.embed_documents([text])[0]

from langchain_openai import ChatOpenAI
from langchain_core.callbacks.streaming_stdout import StreamingStdOutCallbackHandler
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain.memory import ConversationBufferMemory
from langchain.chains.conversational_retrieval.base import ConversationalRetrievalChain

class LangchainRequester:
    def ready(vectorstore):

        # 언어 모델
        llm = ChatOpenAI(
            base_url="http://localhost:5000/v1",
            api_key="lm-studio",
            model="aya-expanse-8b",
            temperature=0.8,
            streaming=True,
            max_tokens=300,
            callbacks=[StreamingStdOutCallbackHandler()] # 스트림시 출력되는 콜백 함수
        )

        # 메모리
        memory = ConversationBufferMemory(
            memory_key="chat_history",
            return_messages=True
        )

        # RAG 체인
        chain = ConversationalRetrievalChain.from_llm(
            llm=llm,
            retriever=vectorstore.as_retriever(search_kwargs={"k":3}),
            memory=memory,
            return_source_documents=True,
            combine_docs_chain_kwargs={
                "prompt": ChatPromptTemplate.from_messages([
                    ("system", """
                     200단어가 넘지 않게 짧고 간결하게 대답해줘.
                     모든 문장은 한국어로 표현해.
                     아래에 문서 내용이 있을 경우, 최대한 문서 내용을 기반으로 답해줘.
                     
                     문서 내용: {question}
                     """),
                    ("user", "{context}")
                ])
            }
        )

        return chain
    
    def chat(chain, question):
        try:
            response = chain({"question": question})
            sources = [doc.metadata.get('source', 'Unknown') for doc in response['source_documents']]
            return response['answer'], sources
        except Exception as e:
            print("대화 중 오류 발생")
            print(e)
            return None, None