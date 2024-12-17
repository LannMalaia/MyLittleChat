from langchain_anthropic import ChatAnthropic
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_groq import ChatGroq
from dotenv import load_dotenv
import os

load_dotenv()

class Chat():
    def __init__(self, llm_type: str, role: str, character: str, message: str):
        self.llm_type: str = llm_type
        self.role: str = role
        self.character: str = character
        self.message: str = message

    def to_dict(self):
        return {"role": self.role, "content": f"{self.character}: {self.message}"}
    def to_message(self):
        return f"{self.character}:\n {self.message}"

class ChatManager():
    _instance = None
    llm_claude = ChatAnthropic(
        model = "claude-3-sonnet-20240229",
        temperature = 0.8,
        max_tokens = 500,
        api_key = os.environ.get("CLAUDE_API_KEY")
    )
    llm_gemini = ChatGoogleGenerativeAI(
        model = "gemini-2.0-flash-exp",
        temperature = 0.8,
        max_tokens = 500,
        google_api_key = os.environ.get("GOOGLE_API_KEY")
    )
    llm_groq = ChatGroq(
        model = "llama-3.3-70b-versatile",
        temperature = 0.8,
        max_tokens = 500,
        api_key = os.environ.get("GROQ_API_KEY")
    )
    chat_logs: dict = {}

    def __new__(self):
        if not self._instance:
            self._instance = super().__new__(self)
        return self._instance
    
    def get_chatlog(self, token: str) -> list[Chat]:
        if token not in self.chat_logs.keys():
            self.chat_logs[token] = [
                Chat(role="system", llm_type="", character="", message="자유롭게 말해. 500자 이내로 대답해줘."),
            ]
        return self.chat_logs[token]

    async def chat(self, token: str, msg: str, llm_type: str="claude", character: str="A"):
        """
            token = 세션 토큰
            msg = 메시지
            character = 어떤 캐릭터의 말인가
            option = 어떤 llm으로 대화할 것인가
        """
        logs: list = self.get_chatlog(token=token)
        logs.append(
            Chat(
                llm_type=llm_type,
                role="user",
                character=character,
                message=msg
            )
        )
        if llm_type == "claude":
            response = self.llm_claude.invoke(logs)
        elif llm_type == "gemini":
            response = self.llm_gemini.invoke(logs)
        elif llm_type == "groq":
            response = self.llm_groq.invoke(logs)
        else:
            raise KeyError
        logs.append(
            Chat(
                llm_type=llm_type,
                role="assistant",
                character="GM",
                message=response.content
            )
        )
        return response.content
