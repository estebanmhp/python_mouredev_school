import reflex as rx
from link_bio.styles.styles import Size as Size

def info_text(title: str, body: str) -> rx.Component:
    return rx.box(
        rx.hstack(
            rx.text(title, font_size = Size.MEDIUM, font_weight = "bold", color = "blue"),
            rx.text(body, font_size = Size.MEDIUM, margin_left = "-0.75em")
        )
    )
    