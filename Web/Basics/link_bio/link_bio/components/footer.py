import reflex as rx
import link_bio.styles.styles as styles
from link_bio.styles.styles import Size as Size
from link_bio.styles.colors import Color as Color
from link_bio.styles.colors import TextColor as TextColor
import datetime

def footer() -> rx.Component:
    return rx.vstack(
        rx.image(
            src = "/images/logo.png",
            margin_top = Size.MEDIUM,
            width = "4em",
            heigth = "4em"
        ),
        rx.text(
            f"2022 - {datetime.date.today().year}  ",            
            rx.link(
                "Esteban Hernandez", 
                href = "https://www.linkedin.com/in/esteban-m-hernandez/",
                margin_top = "-0.25em",
                is_external = True,
                color = Color.PRIMARY
            ),
            color = TextColor.FOOTER        
        ),
        rx.text(
            "PROGRAMMING WITH ♥ FROM COLOMBIA, DEVELOPING THE WORLD",
            font_size = "0.75rem",
            margin_top = "-0.25em",
            margin_bottom = Size.BIG,
            color = TextColor.FOOTER
        ),
        gap = styles.Size.EXTRA_SMALL,
        align="center",
        justify="center",
        margin_bottom = Size.BIG
    )