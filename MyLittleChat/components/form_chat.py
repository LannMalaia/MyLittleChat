import reflex as rx

from MyLittleChat.manager.chat_manager import ChatManager

class Chatter(rx.ComponentState):

    @classmethod
    def get_component(cls, handler, **props):
        return rx.form(
            rx.hstack(
                rx.text("LLM 모델: "),
                rx.select(
                    items=["claude", "gemini", "groq"],
                    name="llm_type",
                    default_value="claude"
                ),
                rx.spacer(),
                rx.text("캐릭터: "),
                rx.select(
                    items=["A", "B", "C"],
                    name="character",
                    default_value="A"
                ),
            ),
            rx.divider(size="2"),
            rx.input(placeholder="이곳에 텍스트 입력", name="chat"),
            on_submit=handler,
            reset_on_submit=True,
            style={
                "width": "100%"
            }
        )
    
chatter = Chatter.create

def temp_chat(msg_list: list[str]) -> rx.Component:
    return rx.box(
        rx.vstack(  
            rx.divider(),
            rx.foreach(msg_list, rx.text),
            rx.divider(),
        ),
        width="100%"
    )