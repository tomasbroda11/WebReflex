import reflex as rx
from enum import Enum
from WebTomas.styles.colors import Color, text_color
from .fonts import font, FontWeight

#Constantes
MAX_WIDTH="560px"
LINKEDIN_URL = "https://linkedin.com/in/tomasbroda"


STYLESHEETS = {
    "https://fonts.googleapis.com/css?family=Poppins:wgth@300;700&display=swap"
    "https://fonts.googleapis.com/css2?family=Noto+Serif:wgth@400&display=swap"
}

#Tamañanos por defecto creados por mi
class Size(Enum):
    SMALL = "0.5em"
    MEDIUM = "0.8em"
    DEFAULT = "1em"
    BIG = "2em"
    LARGE = "1.5em"
    ZERO = "0px"

#Estilos
BASE_SYTLE = {
    "font_family": font.DEFAULT.value,
    "font_weight": FontWeight.LIGHT.value,
    "background_color": Color.BACKGROUND.value,
    rx.heading:{
        "font_family": font.TITLE.value,
        "font_weight": FontWeight.BOLD.value,
        "color": text_color.HEADER.value,
        "size": "7"
    },
    rx.button: {
        "width": "100%",
        "height": "100%",
        "font_size": Size.MEDIUM.value,
        "padding": Size.SMALL.value,
        "border_radius": Size.DEFAULT.value,
        "background_color": Color.PRIMARY.value,
        "white_sapce": "normal",
        "text_align": "start",
        "_hover": {"background_color": Color.CONTENT.value}
    },
    rx.link:{
        "text-decoration":"none",
        "hover": {} 
    },
     rx.input:{
        "width": "100%",  # Ajusta el ancho del input al 100%
        "background-color": Color.BACK_INPUT.value,
        "padding": Size.SMALL.value,
        "border_radius": Size.SMALL.value,
    },
    rx.text_area: {
        "background-color": Color.BACK_INPUT.value,
        "width": "100%",  # Ajusta el ancho del textarea al 100%
        "padding": Size.SMALL.value,
        "border_radius": Size.SMALL.value,
    },
  
   
}

button_title_style = dict(
    font_size = Size.DEFAULT.value,
    font_family= font.DEFAULT.value,
    font_weight = FontWeight.LIGHT.value
)

button_body_style = dict(
    font_size = Size.MEDIUM.value
)

title_style = dict(
    width= "100%",
    padding_top= Size.DEFAULT.value,
    color= text_color.BODY.value,
    font_family= font.TITLE.value,
    font_weight = FontWeight.BOLD.value
)

nav_bar_style = dict(
    color=Color.SECONDARY.value,
    font_size= Size.LARGE.value,
    font_family= font.LOGO.value,
    font_weight = FontWeight.DEFAULT.value
    
)
 