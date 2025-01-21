import reflex as rx
from enum import Enum

# CONSTANTS

MAX_WIDTH = "550px"

# SIZES

class Size(Enum):
    EXTRA_SMALL = "0.25em"
    SMALL = "0.5em"
    MEDIUM = "0.75em"
    DEFAULT = "1em"
    BIG = "2em"

# STYLES

BASE_STYLE = {
    rx.button: {
        "width": "100%",
        "height": "100%",
        "display": "block",
        "padding": Size.SMALL.value,
        "border_radius": Size.DEFAULT.value
    },
    rx.link: {
        "text_decoration": "none",
        "_hover": {}
    }
}

title_style = dict (
    font_size = "1.5rem",
    font_weight = "600",
    width = "100%",
    padding_top = Size.DEFAULT
)

button_style_title = dict (
    font_size = Size.DEFAULT
)

button_style_body = dict (
    font_size = Size.MEDIUM
)