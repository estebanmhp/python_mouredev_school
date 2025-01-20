import reflex as rx

def navbar() -> rx.Component:
    return rx.hstack(
        rx.text(
            "Web Development",
            height = "40px",
            weight = "bold",
            color = "#FFFFFF"
        ),
        position = "sticky",
        background = "#000080",
        opacity = "50%",
        padding_x = "30px",
        padding_y = "10px",
        z_index = "999"
    )