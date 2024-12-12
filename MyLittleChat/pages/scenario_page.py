import reflex as rx
from MyLittleChat.systems.mlcState import State as st
import MyLittleChat.components.layout as layout

@rx.page(route="/scenario")
def scenario_page() -> rx.Component:
    # Welcome Page (Index)
    return rx.hstack(
        layout.side_navi(),
        rx.container(
            rx.vstack(
                rx.box(
                    rx.foreach(st.num_list, rx.text),
                    style={
                        "flex": 1,
                        "overflow": "auto"
                    }
                ),
                rx.divider(),
                rx.form(
                    rx.input(placeholder="이곳에 텍스트 입력", on_change=st.set_num),
                    on_submit= lambda x: st.add_num,
                    reset_on_submit=True,
                    style={
                        "width": "100%"
                    }
                ),
                style={
                    "height": "calc(100vh - 2rem)",
                    "justifyContent": "space-between"
                }
            ),
        )
    )
