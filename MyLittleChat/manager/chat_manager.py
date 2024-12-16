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

    def __new__(self):
        if not self._instance:
            self._instance = super().__new__(self)
        return self._instance

    async def chat(self, msg: str, option: str="claude"):
        messages = [
            {"role": "system", "content": "자유롭게 말해."},
            {"role": "user", "content": msg},
        ]
        if option == "claude":
            response = self.llm_claude.invoke(messages)
        elif option == "gemini":
            response = self.llm_gemini.invoke(messages)
        else:
            raise KeyError
        return response.content
