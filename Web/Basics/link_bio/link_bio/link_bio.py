import reflex as rx
from link_bio.components.navbar import navbar
from link_bio.components.footer import footer
from link_bio.views.header import header
from link_bio.views.repo_links import repo_links

class State(rx.State):
    pass

# Graphic return (rx.Component)

def index() -> rx.Component:
    return rx.vstack(
        navbar(),
        header(),
        repo_links(),
        footer()
    )

app = rx.App()
app.add_page(index)
app._compile()