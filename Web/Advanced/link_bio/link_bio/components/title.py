import reflex as rx
import link_bio.styles.styles as styles

def title(name: str) -> rx.Component:
    return rx.heading(
        name,
        style = styles.title_style
    )