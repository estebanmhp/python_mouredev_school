import reflex as rx
import link_bio.styles.styles as styles
from link_bio.styles.styles import Size as Size
import datetime

def footer() -> rx.Component:
    return rx.vstack(
        rx.image(
            src = "favicon.ico",
            margin_top = Size.MEDIUM
        ),
        rx.text(
            f"2022 - {datetime.date.today().year}  ",
            rx.link(
                "Esteban Hernandez", 
                href = "https://www.linkedin.com/in/esteban-m-hernandez/",
                margin_top = "-0.25em",
                is_external = True
            )        
        ),
        rx.text(
            "PROGRAMMING WITH ♥ FROM COLOMBIA, DEVELOPING THE WORLD",
            font_size = "0.75rem",
            margin_top = "-0.25em"
        ),
        gap = styles.Size.EXTRA_SMALL,
        align="center",
        justify="center",
        margin_bottom = Size.BIG
    )