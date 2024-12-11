"""Welcome to Reflex! This file outlines the steps to create a basic app."""

import reflex as rx

from MyLittleChat.components import button
from rxconfig import config


class State(rx.State):
    num = 0
    my_todo = ["aa", "bb", "cc", "dd"]
    def increase_num(self):
        self.num += 1
    def decrease_num(self):
        self.num -= 1



def index() -> rx.Component:
    # Welcome Page (Index)
    return rx.container(
        rx.color_mode.button(position="top-right"),
        rx.hstack(
            rx.button("감소", on_click=State.decrease_num, color_scheme="grass"),
            rx.text(State.num),
            rx.button("증가", on_click=State.increase_num, color_scheme="ruby"),
            spacing="4",
        ),
        rx.vstack(
            rx.foreach(State.my_todo, button.my_list_element),
        ),
        rx.logo(),
    )


app = rx.App()
app.add_page(index)
