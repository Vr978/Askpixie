import reflex as rx 



def navbar():
    return rx.hstack(
        rx.image(src="birdview.png",width='100px',height='100px'),
        rx.text("AskPixie",background_image="linear-gradient(271.68deg, #EE756A 0.75%, #756AEE 88.52%)",background_clip="text",font_weight="bold",
    font_size="2em"),
    )