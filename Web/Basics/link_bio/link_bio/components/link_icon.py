import reflex as rx
import link_bio.styles.styles as styles

def link_icon(image: str, url: str, alt: str) -> rx.Component:
    return rx.link(
        rx.image(
            src = image,     
            width = styles.Size.BIG,
            height = styles.Size.BIG,
            alt = alt,   
        ),
        href = url,
        is_external= True
    )