import reflex as rx
from link_bio.styles.styles import Size as Size

def navbar() -> rx.Component:
    return rx.hstack(
        rx.text(
            "estebanmhp",
            font_size = "1.25rem",
            font_weight = "500"
        ),
        position = "sticky",
        background = "lightgray",
        padding_x = Size.DEFAULT,
        padding_y = Size.SMALL,
        z_index = "999",
        top = "0"
    )