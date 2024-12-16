import reflex as rx

from MyLittleChat.manager.chat_manager import ChatManager

class Chatter(rx.ComponentState):

    @classmethod
    def get_component(cls, handler, **props):
        return rx.form(
            rx.input(placeholder="이곳에 텍스트 입력", name="chat"),
            on_submit= handler,
            reset_on_submit=True,
            style={
                "width": "100%"
            }
        )
    
chatter = Chatter.create

def temp_chat(msg_list: list[str]) -> rx.Component:
    return rx.vstack(  
        rx.divider(),
        rx.foreach(msg_list, rx.text),
        rx.divider()
    ) 