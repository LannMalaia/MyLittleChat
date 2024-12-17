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
                    form.short_textline(placeholder="이름"),
                    form.long_textarea(placeholder="설명"),
                    rx.divider(size="4"),
                    rx.heading("표상"),
                    form.symbol_selector(is_good = True),
                    form.symbol_selector(is_good = False),
                    rx.divider(size="4"),
                    rx.heading("정체성과 고민"),
                    form.long_textline(placeholder="정체성 면모"),
                    form.long_textline(placeholder="고민 면모"),
                    rx.divider(size="4"),
                    rx.hstack(
                        rx.heading("기타 면모"),
                        rx.icon_button("plus")
                    ),
                    form.aspect_input(placeholder="일반 면모"),
                    form.aspect_input(placeholder="일반 면모"),
                    form.aspect_input(placeholder="일반 면모"),
                    rx.divider(size="4"),
                    rx.heading("기능"),
                    form.stat_selector(),
                    rx.divider(size="4"),
                    rx.heading("특기 (미구현)"),
                    form.skill_input(),
                    form.skill_input(),
                    rx.divider(size="4"),
                    style={
                        # "height": "calc(100vh - 2rem)",
    #                    "justifyContent": "space-between"
                    }
                )
            )
        )
    )
