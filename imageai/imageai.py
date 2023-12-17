import reflex as rx 
from .state import AppState
from .components import Box
from .style import css, blink
from .navbar import navbar

from typing import Any

def create_box_dimensions(width, height) -> dict[str, Any]:
        return {
            "width": width,
            "height": height,
            "box_shadow": "Opx 10px 20px 0px rgba(0,0,0,0.5)",
            "_hover": {"box_shadow": "none"},
            "transition": "all 450ms ease",
            "display": "flex",
            "justify_content": "center",
            "align_items": "center",
        }

dimensions: dict[str, dict[str, Any]] = {
    "square": create_box_dimensions ("5em", "5em'"),
    "rectangle": create_box_dimensions ("5em", "10.5em"),
    "custom-1": create_box_dimensions ("10.5em", "10.5em"),
    "custom-2": create_box_dimensions ("10.5em", "5em"),
}

def image_upload_box():
    return rx.container(
        rx.container(
            rx.cond(
                AppState.img,
                rx.image(src="/"+AppState.img[0],width='300px',height='300px',position='relative',left='70px'),
            )
        ),
        rx.container(
            rx.upload(
                rx.vstack(
                    rx.button("SelectFile"),
                    rx.text("Drag and Drop Files Here",text_align='center'),                    
                ),

                accept={
                    "image/png": [".png"],
                    "image/jpeg": [".jpg",".jpeg"]
                },
            ),
            rx.hstack(
                rx.container(
                    rx.foreach(
                        rx.selected_files,
                        rx.text,
                    )
                ),
            ),
            rx.button(
                "Upload",
                on_click = lambda:AppState.handle_upload_and_message(
                    rx.upload_files()
                ),position='relative',top='60px',left='210px'
            ),
        ),
    )


def image_section():
    return rx.vstack(
        image_upload_box(),margin_top='60px'
    )

def input():
    return rx.box(
        rx.input(type='text',value=AppState.question,placeholder='Enter a Question',on_change=AppState.set_question)
    )

def output():
    return rx.box(
        rx.box(
            rx.button('Ask', on_click=AppState.process_input),
        ),
        rx.box(
            rx.markdown(AppState.answera),style={'padding':AppState.box_padding,'line-height': '1.5', 'font-size': '16px'},max_width='700px',margin_top='30px',max_height='500px',overflow= 'auto',bg='10px 10px lightgrey',color='black',border='1px transparent',border_radius='30px'
        )
         # The text will be reactively updated when state changes.
    )


@rx.page(route='/about',on_load=AppState.on_load(AppState.answer,AppState.answera))
def about():
    return rx.responsive_grid(
        rx.hstack(
        rx.container(
             rx.text (
                "/"+AppState.prompt, font_size="32px",font_weight='bold',
                color=" rgba (255, 255, 255, 0.81)",position='relative',left='230px',top='147px',background_image="linear-gradient(271.68deg, #EE756A 0.75%, #756AEE 88.52%)",background_clip="text"
            ) ,
            rx.text("AskPixie",background_image="linear-gradient(271.68deg, #EE756A 0.75%, #756AEE 88.52%)",background_clip="text",font_weight="bold",
    font_size="2em",position='relative',left='100px',top='100px'),
    rx.image(src='/pixieb.png',width='100px',height='100px'),
            rx.box(
                input(),
            ),
            rx.box(
                 output(),position='relative',top='10px'
            ),
            max_width='50%',margin_top='30px',height='100%'
        ),rx.divider(orientation="vertical", border_color="black"),
        rx.container(
        image_section(),
                rx.box(
        rx.box(
            rx.markdown(AppState.answer),style={'padding':AppState.box_cadding,'line-height': '1.5', 'font-size': '16px'},max_width='700px',margin_top='80px',max_height='500px',overflow= 'auto',bg='10px 10px lightgrey',color='black',border='1px transparent',border_radius='30px'),
        )
        )
        ),rx.divider(border='1px solid black',margin_top="10px"),
    )

def index():

    return rx.vstack( 
        
        navbar(),
        rx.spacer(
            rx.divider(margin_top='0.5rem'),
            style= css['app'],
            ),
        rx.vstack(
            rx.hstack(
            rx.button(
            rx.icon(tag="moon"),
            on_click=rx.toggle_color_mode,
        ),
            ),
            spacing="0", 
            style=css["content"],
        ),
        rx.divider(height="0.2em", opacity="0"),
        rx.hstack(
            rx.vstack(
                rx.hstack(
                    rx.vstack(
                         rx.link(
                              Box(
                            dimensions["custom-2"],
                            "red",
                            "1.5",
                            "time"),
                            href='/about',on_click=AppState.history_compo
                         ),
                        rx.link(Box(
                            dimensions["custom-2"],
                            "teal",
                            "1.5",
                            "plus_square",),href='/about',on_click=AppState.math_compo
                        ),),
                        rx.link(Box(
                        dimensions["rectangle"], 
                        "orange",
                        "1.75",
                        "sun"
                        ),href='/about',on_click=AppState.astro_compo),
                        
                    
                    ),
                rx.link(Box(
                    dimensions["custom-1"],
                    "grey",
                    "4",
                    "edit",
                ),href='/about',on_click=AppState.art_compo),
                
                transition= "all 550ms ease",
                spacing= AppState.leftSpacing
            ),
            rx.vstack(
                rx.hstack(
                    rx.vstack(
                         rx.link(Box(
                            dimensions["custom-2"],
                            "teal",
                            "1.5",
                            "lock",),href='/about',on_click=AppState.cyber_compo),
                        
                        rx.link(Box(
                            dimensions["custom-2"],
                            "red",
                            "1.5",
                            "calendar",),href='/about',on_click=AppState.event_compo),
                        
                        rx.link(Box(
                            dimensions["custom-1"],
                            "yellow",
                            "4",
                            "bell",),href='/about',on_click=AppState.rel_compo),
                        ),
                    rx.vstack(
                         rx.link(
                             Box(
                            dimensions["rectangle"],
                            "yellow",
                            "1.5",
                            "chat",),href='/about',on_click=AppState.chat_compo 
                         ),
                         rx.link(
                           Box(
                            dimensions["rectangle"],
                            "orange",
                            "1.75",
                            "phone",),href='/about',on_click=AppState.soft_compo   
                         )
                        ),
                ),
            rx.link(Box(
                dimensions["custom-2"],
                "grey",
                "3",
                "settings",
                ),href='/about',on_click=AppState.mech_compo),
            
            transition= "all 550ms ease",
            ),
            style= css['workSpace'],
        )
    )


app = rx.App()
app.add_page(index)
app.add_page(about,route='/about')
app.compile()