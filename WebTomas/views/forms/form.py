import reflex as rx
from WebTomas.components.link_button import link_button
from WebTomas.components.title import title
from WebTomas.styles.styles import Size
from WebTomas.styles.colors import Color, text_color

class FormState(rx.State):
    form_data: dict = {} 
    def manejar_envio(self, form_data: dict):
        self.form_data = form_data


def form() -> rx.Component:
    return rx.vstack(
        title("Contactame"),
        rx.form(
            rx.vstack(
                rx.flex(
                    rx.input(
                        placeholder="Nombre",
                        name="first_name",
                        width="100%",
                        autocomplete="off"
                    ),
                    rx.input(
                        placeholder="Apellido",
                        name="last_name",
                        width="100%",
                        autocomplete="off"
                    ),
                    spacing= "2",
                    width="100% "
                ),
                rx.flex(
                    rx.input(
                        placeholder="Email",
                            name="email",
                            match="badInput",
                            width="100%",
                            autocomplete="off"
                    ),
                    rx.input(
                        placeholder="Telefono",
                        name="phone",
                        width="100%",
                        autocomplete="off"
                    ),
                    spacing= "2",
                    width="100%"
                ),
                rx.text_area(
                    placeholder="Escribeme un mensaje para saber algo de ti...",
                    name="message",
                    min_length=10,
                    width="100%",
                    autocomplete="off"
                ),
                rx.button("Enviar", type="submit")
            ),
            width="100%",
            on_submit=FormState.manejar_envio,
            reset_on_submit=True,
            
        ),
        rx.divider(color_scheme="orange", decorative=True),
        title("Resultados"),
        rx.text(FormState.form_data.to_string(),
                color= text_color.FOOTER.value
                ),
        spacing= "3",
        width="100%",
        align= "center"
    )