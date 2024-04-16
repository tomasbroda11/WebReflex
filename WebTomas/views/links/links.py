import reflex as rx
from WebTomas.components.link_button import link_button
from WebTomas.components.title import title
from WebTomas.styles.styles import Size


def links() -> rx.Component:
    return rx.vstack(
       title("Mis links"),
       link_button("LinkedIn","Visita mi perfil profesional" ,"https://linkedin.com/in/tomasbroda"),
       link_button("GitHub","Hecha un vistazo a mis proyectos","https://github.com/tomasbroda11"),
       link_button("Twitter","Lee mis opiniones sobre varios temas" , "https://twitter.com/tomasbroda11"),
       link_button("Instagram","Mi lifestyle al 100%" , "https://www.instagram.com/tomasbroda/"),
       width="100%",
       spacing="2"
       )