import reflex as rx
from MyLittleChat.systems.mlcState import State as st
import MyLittleChat.components.layout as layout

@rx.page(route="/sheet")
def sheetMaking() -> rx.Component:
    # Welcome Page (Index)
    return rx.hstack(
        layout.side_navi(),
        rx.container(
            rx.vstack(
                rx.heading("기본 설정"),
                rx.input(placeholder="이름"),
                rx.input(placeholder="설명"),
                rx.divider(),
                rx.heading("정체성과 고민"),
                rx.input(placeholder="정체성"),
                rx.input(placeholder="고민"),
                rx.divider(),
                rx.heading("기타 면모"),
                rx.input(placeholder="면모"),
                rx.input(placeholder="면모"),
                rx.input(placeholder="면모"),
                rx.divider(),
                rx.heading("기능"),
                rx.input(placeholder="이름"),
                rx.input(placeholder="설명"),
                rx.divider(),
                rx.heading("특기"),
                rx.hstack(
                    rx.input(placeholder="특기명"),
                    rx.input(placeholder="특기 설명"),
                ),
                rx.hstack(
                    rx.input(placeholder="특기명"),
                    rx.input(placeholder="특기 설명"),
                ),
                rx.divider(),
                style={
                    "height": "calc(100vh - 2rem)",
#                    "justifyContent": "space-between"
                }
            ),
        )
    )
