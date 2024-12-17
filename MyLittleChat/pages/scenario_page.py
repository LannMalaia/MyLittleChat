import reflex as rx
import MyLittleChat.components.layout as layout
import MyLittleChat.components.form_chat as chat
from MyLittleChat.manager.chat_manager import ChatManager
from MyLittleChat.manager.chat_manager import Chat

class ScenarioState(rx.State):
    chat_list: list[list[str]] = [["test 1"], ["이것은", "개행", "테스트다"], ["test 3"]]

    @rx.event
    async def handle_chat(self, form_data: dict):
        self.add_chat(form_data["chat"])
        response = await ChatManager().chat(
            token=self.session_token,
            msg=form_data["chat"],
            llm_type=form_data["llm_type"],
            character=form_data["character"]
            )
        print(response)
        self.add_chat(response)

    @rx.var
    def session_token(self) -> str:
        return self.router.page.params.get("token", "default")
        
    def add_chat(self, msg: str):
        self.chat_list.append(msg.split("\n"))

    @rx.event
    def init_chat_logs(self):
        self.chat_list: list[list[str]] = []
        logs = [item for item in ChatManager().get_chatlog(self.session_token)]
        for log in logs:
            if log.role != "system":
                self.add_chat(log.to_message())

@rx.page(route="/scenario/[token]", on_load=ScenarioState.init_chat_logs)
def scenario_page() -> rx.Component:
    # Welcome Page (Index)
    return rx.hstack(
        layout.side_navi(),
        layout.scenario_navi(),
        rx.container(
            rx.vstack(
                rx.box(
                    rx.heading(f"세션 토큰 - {ScenarioState.session_token}"),
                    width="100%",
                    style={
                        "background-color":"purple"
                    }
                ),
                rx.divider(size="2", width="100%"),
                rx.box(
                    rx.foreach(ScenarioState.chat_list, chat.temp_chat),
                    style={
                        "flex": 1,
                        "overflow": "auto"
                    }
                ),
                rx.divider(size="2", width="100%"),
                chat.chatter(ScenarioState.handle_chat),
                style={
                    "height": "calc(100vh - 2rem)",
                    "justifyContent": "space-between"
                },
                width="100%"
            ),
        )
    )
