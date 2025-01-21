import reflex as rx
import link_bio.styles.styles as styles

def link_button(title: str, body: str, url: str) -> rx.Component:
    return rx.link(
        rx.button(
            rx.hstack(
                rx.icon(
                    tag = "panel-left-open",     
                    width = styles.Size.BIG            
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