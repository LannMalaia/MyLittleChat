이것은 Python Reflex 로 만들어지는 프로젝트이다
이것은 flutter랑 약간 비슷한 감성임

pip install reflex 로 라이브러리를 설치하고
reflex run 으로 구동시키자

사용된 라이브러리
- Reflex
 파이썬 기반 웹 프레임워크
- SQLModel
 SQL이 다루기 쉽게 되는 거
- python-dotenv
 .env 환경 변수 쉽게 불러오는 거
- langchain
 랭체인 코어 패키지
- langchain-community
 랭체인 커뮤니티 패키지
- langchain-anthropic
 앤트로픽의 클로드 LLM을 위한 랭체인
- langchain-google-genai
 구글의 제미나이 LLM을 위한 랭체인
- langchain-groq
 그록의 LLM 모델들을 사용하기 위한 랭체인
 그록은 24-12-17 기준 무료로 LLM을 사용할 수 있게 해준다구
- langchain-text-splitters
 RAG 적용을 위해 문서 텍스트를 쪼개주는 역할을 하는 패키지
 - faiss-cpu
 RAG 적용 중 벡터스토어의 유사성을 찾기 위해 사용되는 FAISS


사용된 환경변수
- CLAUDE_API_KEY (클로드 API 키, claude 3.0 sonnet)
- GOOGLE_API_KEY (구글 GEMINI API 키, gemini 2.0 flash exp)
- GROQ_API_KEY (그록 API 키, llama-3.3-70b-versatile)

쓰는 것을 고려할만한 API
getimg.ai - 이미지 생성만을 위한 api
Replicate - 클라우드를 사용하는 ai api. 내가 튜닝한 모델을 직접 게시해서 굴릴 수 있는게 장점.