import reflex as rx
from enum import Enum
from WebTomas.styles.colors import Color, text_color
from WebTomas.styles.fonts import font

#Constantes
MAX_WIDTH="560px"

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
    "background_color": Color.BACKGROUND.value,
    rx.heading:{
        "font_family": font.TITLE.value,
        "color": text_color.HEADER.value,
        "size": "7"
    },
    rx.button: {
        "width": "100%",
        "height": "100%",
        "display": "block",
        "font_size": Size.MEDIUM.value,
        "padding": Size.SMALL.value,
        "border_radius": Size.DEFAULT.value,
        "background_color": Color.PRIMARY.value,
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
    font_family= font.DEFAULT.value
)

button_body_style = dict(
    font_size = Size.MEDIUM.value
)

title_style = dict(
    width= "100%",
    padding_top= Size.DEFAULT.value,
    color= text_color.BODY.value,
    font_family= font.TITLE.value
)

nav_bar_style = dict(
    color=Color.SECONDARY.value,
    font_size= Size.LARGE.value,
    font_family= font.LOGO.value
    
)
 