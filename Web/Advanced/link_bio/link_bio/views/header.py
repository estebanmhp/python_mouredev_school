import reflex as rx
import link_bio.styles.styles as styles
from link_bio.components.link_icon import link_icon
from link_bio.components.info_text import info_text
from link_bio.styles.styles import Size as Size
from link_bio.styles.colors import Color as Color
from link_bio.styles.colors import TextColor as TextColor

def header() -> rx.Component:
    return rx.vstack(
        rx.hstack(
            rx.avatar(
                src="/images/Profile_photoV3.jpg",
                size="7",
                radius="full"
            ),
            rx.vstack(
                rx.heading(
                    "Esteban Hernandez",
                    color = TextColor.HEADER
                ),
                rx.text(
                    "ARCHITECT BY EDUCATION, PROGRAMMER BY PASSION",
                    font_size = Size.MEDIUM,
                    font_weight = "450",
                    color = Color.PRIMARY
                ),
                rx.hstack(
                    link_icon(
                        "/icons/github.png",
                        "https://github.com/estebanmhp",
                        "github"
                    ),
                    link_icon(
                        "/icons/linkedin.png",
                        "https://www.linkedin.com/in/esteban-m-hernandez/",
                        "linkeding"
                    ),
                ),                
                display = "block",
                align_items = "center",
                margin_left = Size.SMALL              
            ),            
            align_items = "center",
        ),
        rx.flex(
            info_text("Exploring", "new techs"),
            rx.spacer(),
            info_text("Developing", "every day"),
            rx.spacer(),            
            info_text("Growing", "with projects"),
            width = "100%"
        ),
        rx.text(
            """I'm a programming student passionate about backend development, focused in Python. 
            I enjoy working with web technologies and have experience using Git and GitHub for version control. 
            With a foundation in C and JavaScript, I'm eager to keep learning and growing my skills every day.""",
            text_align = "justify",
            color = TextColor.BODY
        ),
        spacing = "6",
        align="start" 
    )