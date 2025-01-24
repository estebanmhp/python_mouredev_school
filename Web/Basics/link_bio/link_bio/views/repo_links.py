import reflex as rx
from link_bio.components.link_button import link_button
from link_bio.components.title import title

def repo_links() -> rx.Component:
    return rx.vstack(
        title("Learning and Building"),
        link_button(
            "Overview",
            "Discover everything I have been learning and building",
            "https://github.com/estebanmhp",
            "/icons/overview.png"
        ),
        link_button(
            "Programming in Python",
            "A collection of my Python-focused work",
            "https://github.com/estebanmhp/python_mouredev_school",
            "/icons/python.png"
        ),
        link_button(
            "Programming in JavaScript",
            "A showcase of my JavaScript knowledge",
            "https://github.com/estebanmhp/javascript_mouredev_school",
            "/icons/js.png"
        ),
        link_button(
            "Programming in C",
            "Low-level programming examples in C",
            "https://github.com/estebanmhp/holbertonschool-low_level_programming",
            "/icons/c.png"
        ),
        title("Tools and Technologies"),
        link_button(
            "Version Control and Collaboration",
            "Git and GitHub",
            "https://git-scm.com/doc",
            "/icons/git.png"
        ),
        link_button(
            "Databases",
            "Mongo DB and SQL",
            "https://www.mongodb.com/docs/",
            "/icons/database.png"
        ),
        link_button(
            "Back-end Development",
            "FastAPI, Django and Flask",
            "https://fastapi.tiangolo.com/",
            "/icons/backend.png"
        ),
        link_button(
            "Front-end Development",
            "HTML, CSS, Reflex",
            "https://www.w3schools.com/html/",
            "/icons/frontend.png"
        ),
        title("Contact me"),
        link_button(
            "Email",
            "estebanhernandezpe@gmail.com",
            "mailto:estebanhernandezpe@gmail.com",
            "/icons/email.png"
        ),
        link_button(
            "GitHub",
            "estebanmhp",
            "https://github.com/estebanmhp",
            "/icons/github.png"
        ),
        link_button(
            "LinkedIn",
            "esteban-m-hernandez",
            "https://www.linkedin.com/in/esteban-m-hernandez/",
            "/icons/linkedin.png"
        ),
        width = "100%",
    )