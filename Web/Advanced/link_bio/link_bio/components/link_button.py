import reflex as rx
import link_bio.styles.styles as styles

def link_button(title: str, body: str, url: str, image: str) -> rx.Component:
    return rx.link(
        rx.button(
            rx.hstack(
                rx.image(
                    src = image,     
                    width = styles.Size.BIG,
                    heigth = styles.Size.BIG,
                    alt = title,
                    margin = styles.Size.DEFAULT,
                    margin_right = styles.Size.SMALL      
                ),
                rx.vstack(
                    rx.text(
                        title, 
                        style=styles.button_style_title
                    ),
                    rx.text(
                        body,
                        style=styles.button_style_body
                    ),
                    align_items = "start",
                    gap = styles.Size.EXTRA_SMALL
                ),
                align_items = "center"
            ),
        ),
        href = url,
        is_external = True,
        width = "100%"
    )      