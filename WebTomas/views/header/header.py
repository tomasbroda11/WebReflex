import reflex as rx
from WebTomas.components.link_icon import link_icon
from WebTomas.components.info_text import info_text
from WebTomas.styles.colors  import Color, text_color
from WebTomas.styles.styles import Size
import WebTomas.styles.styles as sty


def header() -> rx.Component:
    return rx.vstack(
            rx.hstack(
                rx.avatar(
                    fallback="TB",
                    size="7", 
                    padding="4px",
                    src="Foto_TomasBroda.jpg", 
                    border="8px", 
                    border_radius="100%",
                    border_color=Color.SECONDARY.value
                ),
                rx.vstack(
                    rx.heading("Tomás Broda"),
                    rx.text("@tomasbroda", margin_top=Size.ZERO.value, color=Color.SECONDARY.value ),
                    width="100%",
                    align_items="start"
                )
                ),
                rx.flex(
                    info_text("+10", "proyectos finalizados"),
                    rx.spacer(),
                    info_text("+10", "proyectos finalizados"),
                    rx.spacer(),
                    info_text("+10", "proyectos finalizados"),
                    width="100%"
                ),

                rx.text("Soy un estudiante de ingenieria en sistemas de informacion de 24 años.\n"
                        "Vivo en Argentina y soy un apasionado por la tecnologia y la programacion.\n"
                        "Tambien me encanta el basquet y los videojuegos!",
                        color= text_color.BODY.value,
                        font_size = "0.9em"
                        ),
                rx.hstack(
                    link_icon(sty.LINKEDIN_URL),
                    link_icon(sty.LINKEDIN_URL),
                    link_icon(sty.LINKEDIN_URL)
                ),
                align_items="start",
                spacing="4"
    )
    