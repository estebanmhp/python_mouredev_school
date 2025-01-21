import reflex as rx
from link_bio.components.navbar import navbar
from link_bio.components.footer import footer
from link_bio.views.header import header
from link_bio.views.repo_links import repo_links
import link_bio.styles.styles as styles
from link_bio.styles.styles import Size as Size

class State(rx.State):
    pass

# Graphic return (rx.Component)

def index() -> rx.Component:
    return rx.box(
        navbar(),
        rx.center(
            rx.vstack(
                header(),
                repo_links(),            
                align="center",
                justify="center",
                max_width = styles.MAX_WIDTH,
                width = "100%",
                margin_y = Size.BIG.value
            ),
        ),
        footer()
    )

app = rx.App(
    style = styles.BASE_STYLE
)
app.add_page(index)
app._compile()