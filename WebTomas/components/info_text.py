import reflex as rx 
from WebTomas.styles.styles import Size as Size
from WebTomas.styles.colors  import Color, text_color


def info_text(text: str, body: str )  -> rx.Component:
    return rx.box(
            rx.text(rx.text.strong(text, font_weight="bold", color=Color.PRIMARY.value), as_="span"),
            rx.text(rx.text.strong(f" {body}"),color=text_color.HEADER.value ,as_="span"), 
            font_size= Size.MEDIUM.value       
        )
