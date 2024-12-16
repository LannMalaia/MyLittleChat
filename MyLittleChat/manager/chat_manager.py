from langchain_anthropic import ChatAnthropic
from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
import os

load_dotenv()

class ChatManager():
    _instance = None
    llm_claude = ChatAnthropic(
        model = "claude-3-sonnet-20240229",
        max_tokens = 200,
        temperature = 0.8,
        api_key = os.environ.get("CLAUDE_API_KEY")
    )
    llm_gemini = ChatGoogleGenerativeAI(
        model = "gemini-2.0-flash-exp",
        max_tokens = 200,
        temperature = 0.8,
        google_api_key = os.environ.get("GOOGLE_API_KEY")
    )
    chat_logs: dict = {}

    def __new__(self):
        if not self._instance:
            self._instance = super().__new__(self)
        return self._instance
    
    def get_chatlog(self, token: str):
        if token not in self.chat_logs.keys():
            self.chat_logs[token] = [
                {"role": "system", "content": "자유롭게 말해."},
            ]
        return self.chat_logs[token]

    async def chat(self, token: str, msg: str, option: str="claude"):
        logs: list = self.get_chatlog(token=token)
        logs.append({"role":"user", "content": msg})
        if option == "claude":
            response = self.llm_claude.invoke(logs)
        elif option == "gemini":
            response = self.llm_gemini.invoke(logs)
        else:
            raise KeyError
        logs.append({"role":"assistant", "content": response.content})
        return response.content
