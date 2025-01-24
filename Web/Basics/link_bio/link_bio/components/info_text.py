import reflex as rx
from link_bio.styles.styles import Size as Size
from link_bio.styles.colors import Color as Color
from link_bio.styles.colors import TextColor as TextColor

def info_text(title: str, body: str) -> rx.Component:
    return rx.box(
        rx.hstack(
            rx.text(
                title,
                font_size = Size.MEDIUM,
                font_weight = "bold",
                color = Color.PRIMARY
            ),
            rx.desktop_only(
                rx.text(
                    body,
                    font_size = Size.MEDIUM,
                    margin_left = "-0.75em",
                    white_space = "normal",
                    color = TextColor.BODY
                )
            )
        )
    )
    