import reflex as rx
import WebTomas.styles.styles as styles 
from WebTomas.styles.styles import Size
from WebTomas.styles.colors  import Color, text_color

def navbar() -> rx.Component:
    return rx.hstack(
            rx.text(
                "<TB/>",
                style= styles.nav_bar_style
                ),
            position="sticky",
            background_color= Color.NAV_BAR.value,
            padding_x= Size.BIG.value,
            padding_y= Size.DEFAULT.value,
            z_index="999"
        )