import reflex as rx

def sidebar_item(
    text: str, icon: str, href: str
) -> rx.Component:
    return rx.link(
        rx.hstack(
            rx.icon(icon),
            rx.text(text, size="4"),
            width="100%",
            padding_x="0.5rem",
            padding_y="0.75rem",
            align="center",
            style={
                "_hover": {
                    "bg": rx.color("accent", 4),
                    "color": rx.color("accent", 11),
                },
                "border-radius": "0.5em",
            },
        ),
        href=href,
        underline="none",
        weight="medium",
        width="100%",
    )

def sidebar_items() -> rx.Component:
    return rx.vstack(
        sidebar_item("메인 페이지", "layout-dashboard", "/#"),
        sidebar_item("시나리오", "messages-square", "/scenario"),
        sidebar_item("시트 작성", "newspaper", "/sheet"),
        sidebar_item("Messages", "mail", "/#"),
        spacing="1",
        width="100%",
    )

def side_navi() -> rx.Component:
    return rx.box(
        rx.drawer.root(
            rx.drawer.trigger(
                rx.icon("align-justify", size=30)
            ),
            rx.drawer.overlay(z_index="5"),
            rx.drawer.portal(
                rx.drawer.content(
                    rx.vstack(
                        rx.box(
                            rx.drawer.close(
                                rx.icon("x", size=30)
                            ),
                            width="100%",
                        ),
                        sidebar_items(),
                        rx.spacer(),
                        rx.vstack(
                            rx.vstack(
                                sidebar_item(
                                    "Settings",
                                    "settings",
                                    "/#",
                                ),
                                sidebar_item(
                                    "Log out",
                                    "log-out",
                                    "/#",
                                ),
                                width="100%",
                                spacing="1",
                            ),
                            rx.divider(margin="0"),
                            rx.hstack(
                                rx.icon_button(
                                    rx.icon("user"),
                                    size="3",
                                    radius="full",
                                ),
                                rx.vstack(
                                    rx.box(
                                        rx.text(
                                            "My account",
                                            size="3",
                                            weight="bold",
                                        ),
                                        rx.text(
                                            "user@reflex.dev",
                                            size="2",
                                            weight="medium",
                                        ),
                                        width="100%",
                                    ),
                                    spacing="0",
                                    justify="start",
                                    width="100%",
                                ),
                                padding_x="0.5rem",
                                align="center",
                                justify="start",
                                width="100%",
                            ),
                            width="100%",
                            spacing="5",
                        ),
                        spacing="5",
                        width="100%",
                    ),
                    top="auto",
                    right="auto",
                    height="100%",
                    width="20em",
                    padding="1.5em",
                    bg=rx.color("accent", 2),
                ),
                width="100%",
            ),
            direction="left",
        ),
        padding="1em"
    )


def scenario_item(
    text: str, icon: str, href: str
) -> rx.Component:
    return rx.link(
        rx.hstack(
            rx.icon(icon),
            rx.text(text, size="4"),
            width="100%",
            padding_x="0.3rem",
            padding_y="0.4rem",
            align="center",
            style={
                "_hover": {
                    "bg": rx.color("accent", 4),
                    "color": rx.color("accent", 11),
                },
                "border-radius": "0.5em",
            },
        ),
        href=href,
        underline="none",
        weight="medium",
        width="100%",
    )
def scenario_category(text: str, icon: str) -> rx.Component:
    return rx.accordion.root(
        rx.accordion.item(
            header="test 1",
            content=rx.vstack(
                scenario_item("aaa", "minus", ""),
                scenario_item("bbb", "minus", ""),
                scenario_item("ccc", "minus", ""),
                scenario_item("ddd", "minus", ""),
                scenario_item("eee", "minus", ""),
            )
        ),
        rx.accordion.item(
            header="test 2",
            content=rx.vstack(
                scenario_item("aaa", "minus", ""),
                scenario_item("bbb", "minus", ""),
                scenario_item("ccc", "minus", ""),
                scenario_item("ddd", "minus", ""),
                scenario_item("eee", "minus", ""),
            )
        ),
        rx.accordion.item(
            header="test 3",
            content=rx.vstack(
                scenario_item("aaa", "minus", ""),
                scenario_item("bbb", "minus", ""),
                scenario_item("ccc", "minus", ""),
                scenario_item("ddd", "minus", ""),
                scenario_item("eee", "minus", ""),
            )
        ),
        width="100%",
        variant="ghost",
        collapsible=True,
    )

def scenario_items() -> rx.Component:
    return rx.vstack(
        scenario_category("메인 페이지", "layout-dashboard"),
        spacing="1",
        width="100%",
    )

def scenario_navi() -> rx.Component:
    return rx.box(
        rx.drawer.root(
            rx.drawer.trigger(
                rx.icon("align-justify", size=30)
            ),
            rx.drawer.portal(
                rx.drawer.content(
                    rx.vstack(
                        rx.box(
                            rx.drawer.close(
                                rx.icon("x", size=30)
                            ),
                            width="100%",
                        ),
                        rx.box(
                            rx.heading("목록", align="right"),
                        ),
                        scenario_items(),
                        rx.spacer(),
                        rx.vstack(
                            rx.vstack(
                                sidebar_item(
                                    "새로운 시나리오",
                                    "plus",
                                    "/#",
                                ),
                                width="100%",
                                spacing="1",
                            ),
                        spacing="5",
                        width="100%",
                        ),
                        width="100%",
                    ),
                    top="auto",
                    right="auto",
                    height="100%",
                    width="30em",
                    padding="1.5em",
                    bg=rx.color("accent", 2),
                ),
                width="100%",
            ),
            direction="left"
        ),
        padding="1em"
    )