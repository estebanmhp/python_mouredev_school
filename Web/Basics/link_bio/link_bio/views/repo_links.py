import reflex as rx
from link_bio.components.link_button import link_button

def repo_links() -> rx.Component:
    return rx.vstack(
        link_button("Overview", "https://github.com/estebanmhp"),
        link_button("Programming in Python", "https://github.com/estebanmhp/python_mouredev_school"),
        link_button("Programming in JavaScript", "https://github.com/estebanmhp/javascript_mouredev_school"),
        link_button("Programming in C", "https://github.com/estebanmhp/holbertonschool-low_level_programming")
    )