import reflex as rx

class State(rx.State):
    pass

# Graphic return

def index() -> rx.Component:
    return rx.text("Python web development")

app = rx.App()
app.add_page(index)
app._compile()