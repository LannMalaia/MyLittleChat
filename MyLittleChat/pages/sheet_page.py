import reflex as rx
from MyLittleChat.systems.mlcState import State as st
import MyLittleChat.components.layout as layout
import MyLittleChat.components.form as form

@rx.page(route="/sheet")
def sheetMaking() -> rx.Component:
    
    return rx.hstack(
        layout.side_navi(),
        rx.container(
            rx.form.root(
                rx.vstack(
                    rx.heading("기본 설정"),
                    rx.input(placeholder="이름"),
                    form.long_textarea(placeholder="설명"),
                    rx.divider(),
                    rx.heading("표상"),
                    form.symbol_selector(is_good = True),
                    form.symbol_selector(is_good = False),
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
                    form.stat_selector(),
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
                )
            )
        )
    )
