import reflex as rx
from link_bio.components.navbar import navbar
from link_bio.components.footer import footer
from link_bio.views.header import header
from link_bio.views.repo_links import repo_links
import link_bio.styles.styles as styles
from link_bio.styles.styles import Size as Size
from link_bio.api.api import repo, live

class State(rx.State):
    is_live: bool
    async def check_live(self):
        is_live = live("mouredev")

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
        footer(),
    )

app = rx.App(
    style = styles.BASE_STYLE
)
app.add_page(
    index,
    title = "Esteban Hernandez - Passionate Developer",
    description = "Developer focused on building projects, honing skills, and embracing new technologies every day",
    image = "/images/logo.png"
)
app.api.add_api_route("/repo", repo)
app.api.add_api_route("/live/{user}", live)