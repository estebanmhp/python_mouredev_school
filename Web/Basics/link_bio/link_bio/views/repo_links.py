import reflex as rx
from link_bio.components.link_button import link_button
from link_bio.components.title import title

def repo_links() -> rx.Component:
    return rx.vstack(
        title("Learning and Building"),
        link_button(
            "Overview",
            "Discover everything I have been learning and building",
            "https://github.com/estebanmhp"
        ),
        link_button(
            "Programming in Python",
            "A collection of my Python-focused work",
            "https://github.com/estebanmhp/python_mouredev_school"
        ),
        link_button(
            "Programming in JavaScript",
            "A showcase of my JavaScript knowledge",
            "https://github.com/estebanmhp/javascript_mouredev_school"
        ),
        link_button(
            "Programming in C",
            "Low-level programming examples in C",
            "https://github.com/estebanmhp/holbertonschool-low_level_programming"
        ),
        title("Tools and Technologies"),
        link_button(
            "Version Control and Collaboration",
            "Git and GitHub",
            "https://git-scm.com/doc"
        ),
        link_button(
            "Databases",
            "Mongo DB and SQL",
            "https://www.mongodb.com/docs/"
        ),
        link_button(
            "Back-end Development",
            "Django and Flask",
            "https://www.djangoproject.com/start/"
        ),
        link_button(
            "Front-end Development",
            "HTML, CSS, Reflex",
            "https://www.w3schools.com/html/"
        ),
        title("Contact me"),
        link_button(
            "Email",
            "estebanhernandezpe@gmail.com",
            "mailto:estebanhernandezpe@gmail.com"
        ),
        link_button(
            "GitHub",
            "estebanmhp",
            "https://github.com/estebanmhp"
        ),
        link_button(
            "LinkedIn",
            "esteban-m-hernandez",
            "https://www.linkedin.com/in/esteban-m-hernandez/"
        ),
        width = "100%",
    )