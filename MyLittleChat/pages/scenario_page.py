import reflex as rx
import MyLittleChat.components.layout as layout
import MyLittleChat.components.form_chat as chat
from MyLittleChat.manager.chat_manager import ChatManager

class ScenarioState(rx.State):
    chat_list: list[list[str]] = [["test 1"], ["이것은", "개행", "테스트다"], ["test 3"]]

    @rx.event
    async def handle_chat(self, form_data: dict):
        self.add_chat(form_data["chat"])
        response = await ChatManager().chat(token="user_token", msg=form_data["chat"], option="gemini")
        print(response)
        self.add_chat(response)
        
    def add_chat(self, msg: str):
        self.chat_list.append(msg.split("\n"))

@rx.page(route="/scenario")
def scenario_page() -> rx.Component:
    # Welcome Page (Index)
    return rx.hstack(
        layout.side_navi(),
        layout.scenario_navi(),
        rx.container(
            rx.vstack(
                rx.box(
                    rx.foreach(ScenarioState.chat_list, chat.temp_chat),
                    style={
                        "flex": 1,
                        "overflow": "auto"
                    }
                ),
                rx.divider(),
                chat.chatter(ScenarioState.handle_chat),
                style={
                    "height": "calc(100vh - 2rem)",
                    "justifyContent": "space-between"
                }
            ),
        )
    )
