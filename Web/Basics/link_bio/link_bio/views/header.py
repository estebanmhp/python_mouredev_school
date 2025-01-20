import reflex as rx

def header() -> rx.Component:
    return rx.vstack(
        rx.avatar(
            fallback = "EH DEV",
            size = "6",
            font_size = "12px",
            weight = "bold",
            margin_left = "61.93px",
            radius = "full"
        ),
        rx.text("@estebanmh"),
        rx.text("HELLO WORLD! 👋 MY NAME IS ESTEBAN"),
        rx.text("""I'm a programming student passionate about backend development, focused in Python. 
                I enjoy working with web technologies and have experience using Git and GitHub for version control. 
                With a foundation in C and JavaScript, I'm eager to keep learning and growing my skills every day.""")
    )