import reflex as rx
from link_bio.styles.styles import Size as Size
from link_bio.styles.colors import Color as Color

def navbar() -> rx.Component:
    return rx.hstack(
        rx.text(
            "estebanmhp",
            font_size = "1.25rem",
            font_weight = "500",
            font_family = "Comfortaa, Sans-Serif",
            color = Color.PRIMARY
        ),
        position = "sticky",
        background = Color.SECONDARY,
        padding_x = Size.DEFAULT,
        padding_y = Size.SMALL,
        margin_left = "-1em",
        margin_right = "-1em",
        z_index = "999",
        top = "0"
    )