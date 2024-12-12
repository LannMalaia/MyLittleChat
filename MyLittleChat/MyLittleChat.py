"""Welcome to Reflex! This file outlines the steps to create a basic app."""

import reflex as rx

from MyLittleChat.components import layout
from rxconfig import config


class State(rx.State):
    num: int
    num_list = [3, 2, 1]

    def add_num(self):
        self.num_list.insert(0, self.num)
    def set_num(self, val):
        self.num = val


def index() -> rx.Component:
    # Welcome Page (Index)
    return rx.hstack(
        layout.side_navi(),
        rx.container(
            rx.vstack(
                rx.form(
                    rx.input(on_change=State.set_num),
                    on_submit= lambda x: State.add_num,
                    reset_on_submit=True
                ),
                rx.hstack(
                    rx.input(value=State.num, on_change=State.set_num),
                    rx.button("추가", on_click=State.add_num)
                ),
                rx.foreach(State.num_list, rx.text)
            ),
            height="100%"
        ),
        width="100%",
        height="100%"
    )


app = rx.App()
app.add_page(index)
