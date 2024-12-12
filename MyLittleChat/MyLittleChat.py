"""Welcome to Reflex! This file outlines the steps to create a basic app."""

import reflex as rx
from MyLittleChat.systems.mlcState import State as st

from MyLittleChat.components import layout

from MyLittleChat.pages import *  # noqa: F403

def index() -> rx.Component:
    # Welcome Page (Index)
    return rx.hstack(
        layout.side_navi(),
        rx.container(
            rx.vstack(
                rx.heading("메인 페이지"),
                align="center",
                justify="center",
                style={
                    "height": "calc(100vh - 2rem)",
                    "justifyContent": "space-between"
                }
            ),
        )
    )


app = rx.App()
app.add_page(index)
