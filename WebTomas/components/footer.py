import reflex as rx
import datetime 
from WebTomas.styles.styles import Size
from WebTomas.styles.colors import Color, text_color


def footer() -> rx.Component:
    return rx.vstack(
        rx.avatar(
                    fallback="CD",
                    size="9", 
                    padding="4px",
                    src="carpe_diem.jpg", 
                    border="8px", 
                    border_radius="100%",
                    border_color=Color.SECONDARY.value,
                    width="auto"
                ),
        rx.link(
            f"{datetime.date.today().year} - BRODA TOMAS V1.0.1",
            href="https://www.google.com/search?sca_esv=db991f8d1f0bb011&sxsrf=ACQVn092nxnB_V3Q_wRC1F1C7ZaGdPjWyQ:1712954741651&q=brad+pitt+imagenes&uds=AMwkrPs4mDHqV7QfY9nYaKRHgvE9RTkQ3Z9UiDcGzR7IizhwE-CNVkVWKQgBKZb8yIsLpM7CWBd9xd0C-ARJ1jQL6se1z806ykS9RNzKXdYCWQBslsjYuOImPX_dl37V1E9Qgz73x8M8MG2UibAJGsOyzd5nsCXdtWUqkuQUg_LdtIx4i96mlrat2111mtvJCh64gfrA-z4oLqk6VSnIUoJcc1Nejx5oIjAWViV3AjNvFaxI-rHu8Vaaxmz2cFXiNIK0n0yWIIj6012xnfmj7F5gYuPn96hsWWKN6KNaFbrrk0G2fP74qVIVRlQ6w7ZkyvhhEhg0ZRSc&udm=2&prmd=invsbmtz&sa=X&ved=2ahUKEwj4sZHXxb2FAxVupJUCHYf-B8oQtKgLegQIExAB&biw=1536&bih=695&dpr=1.25",
            is_external= True,
            font_size= Size.MEDIUM.value,
        ),
        rx.text(
                "BUILDING SOFTWARE FROM ARGENTINA TO THE WORLD",
                 font_size= Size.MEDIUM.value,
                 margin_bottom= Size.ZERO.value
                 ),
        margin_bottom= Size.BIG.value,
        padding_bottom= Size.BIG.value,
        padding_y="2",
        align= "center",
        color= text_color.FOOTER.value
    )