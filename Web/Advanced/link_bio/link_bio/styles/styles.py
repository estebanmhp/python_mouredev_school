import reflex as rx
from enum import Enum
from .colors import Color, TextColor

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
    "background": Color.BACKGROUND,
    rx.button: {
        "width": "100%",
        "height": "100%",
        "padding": Size.SMALL.value,
        "border_radius": Size.DEFAULT.value,
        "color": TextColor.HEADER,
        "white_space": "normal",
        "display": "block",
        "_hover": {
            "background_color": Color.PRIMARY
        },  
        "background_color": Color.SECONDARY
    },
    rx.link: {
        "text_decoration": "none"
    },
    "padding_left": Size.DEFAULT,
    "padding_right": Size.DEFAULT,
    "margin_bottom": "-5em"
}

title_style = dict (
    font_size = "1.5rem",
    font_weight = "600",
    width = "100%",
    padding_top = Size.DEFAULT,
    color = TextColor.HEADER
)

button_style_title = dict (
    font_size = Size.DEFAULT,
    color = TextColor.HEADER
)

button_style_body = dict (
    font_size = Size.MEDIUM,
    font_weight = "400",
    color = TextColor.BODY
)