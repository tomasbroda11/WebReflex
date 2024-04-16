import reflex as rx
import WebTomas.styles.styles as styles

def link_icon(url: str) -> rx.Component:
    return rx.link(
        rx.icon(
            tag= "linkedin",
        ),
        href= url,
        is_external= True
    )