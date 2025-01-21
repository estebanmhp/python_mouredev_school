import reflex as rx
import link_bio.styles.styles as styles
from link_bio.components.link_icon import link_icon
from link_bio.components.info_text import info_text
from link_bio.styles.styles import Size as Size

def header() -> rx.Component:
    return rx.vstack(
        rx.hstack(
            rx.avatar(
                fallback = "EH DEV",
                size = "6",
                font_size = "12px",
                weight = "bold",
                radius = "full"
            ),
            rx.vstack(
                rx.heading("Esteban Hernandez"),
                rx.text("HELLO WORLD! 👋"),
                rx.hstack(
                    link_icon("https://github.com/estebanmhp"),
                    link_icon("https://www.linkedin.com/in/esteban-m-hernandez/"),
                ),                
                display = "block",
                align_items = "center",
                margin_left = Size.SMALL              
            ),            
            align_items = "center",
        ),
        rx.flex(
            info_text("Developing", "every day"),
            rx.spacer(),
            info_text("Exploring", "tech"),
            rx.spacer(),            
            info_text("Growing", "through projects"),
            width = "100%"
        ),
        rx.text(
            """I'm a programming student passionate about backend development, focused in Python. 
            I enjoy working with web technologies and have experience using Git and GitHub for version control. 
            With a foundation in C and JavaScript, I'm eager to keep learning and growing my skills every day.""",
            text_align = "justify"
        ),
        spacing = "6",
        align="start" 
    )