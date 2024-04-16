import reflex as rx
import WebTomas.components.navbar as navbar
import WebTomas.components.footer as footer
import WebTomas.views.header.header as header
import WebTomas.views.links.links as links
import WebTomas.views.forms.form as form
import WebTomas.styles.styles as styles
from WebTomas.styles.styles import Size


class State(rx.State):
    pass

def index() -> rx.Component: #esta es la pagina ppal
    return rx.box(
        navbar.navbar(),
        rx.center(
            rx.vstack(
                header.header(),
                links.links(),
                form.form(),
                max_width= styles.MAX_WIDTH,
                width="100%",
                align="center",
                margin_y= Size.BIG.value,
                justify= "center"
            )
        ),
        footer.footer()
    )

app = rx.App(style= styles.BASE_SYTLE)
app.add_page(index) #agrego la pagina ppal a la app 
app.compile()