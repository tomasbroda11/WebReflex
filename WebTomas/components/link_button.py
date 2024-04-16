import reflex as rx
import WebTomas.styles.styles as styles

def link_button(title: str, body: str, url: str) -> rx.Component:
    return rx.link(
        rx.button(
            rx.hstack(
                rx.icon(tag="arrow-right"),
                rx.vstack(
                    rx.text(title, style=styles.button_title_style),
                    rx.text(body, style=styles.button_body_style),
                    align_items= "left"
                )
            )
        ),
        href= url,
        is_external= True,
        width="100%"


    )
    
    
    
    
    
    
    
    
    
    
    return rx.link(
        rx.button(
            text,
            width="100%"
            ),
        href= url,
        is_external= True
        
    )
    
    
    
    