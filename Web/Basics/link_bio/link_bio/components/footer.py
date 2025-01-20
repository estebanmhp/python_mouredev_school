import reflex as rx
import datetime

def footer() -> rx.Component:
    return rx.vstack(
        rx.image(src = "favicon.ico"),
        rx.text(f"2022 - {datetime.date.today().year} Always learning, always growing"),
        rx.link(
            "Esteban Hernandez", 
            href = "https://www.linkedin.com/in/esteban-m-hernandez/",
            is_external = True)
    )