import reflex as rx
import WebTomas.styles.styles as styles
from  WebTomas.styles.colors  import text_color

def title(text: str) -> rx.Component:
    return rx.heading( 
            text,
            size="8",
            color= text_color.HEADER.value
            )