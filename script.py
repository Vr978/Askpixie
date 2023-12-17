import reflex as rx

class State(rx.State):
    img: list[str] = []

    async def handle_upload(self, files: list[rx.UploadFile]):
        for file in files:
            # Here you would typically save file to server storage.
            # Then, you would store the URL or filename to render later.
            self.img.append(file.filename)

def index():
    return rx.vstack(
        rx.upload(
            "Upload",
            on_click=lambda: State.handle_upload(rx.upload_files())
        ),
        # Other components to display uploaded images...
    )

def display_images():
    return rx.responsive_grid(
        *[
            rx.image(src=f"/assets/{filename}")
            for filename in State.img
        ],
        min_child_width="150px",
        gap="1em"
    )

app = rx.App()
app.add_page(index)
app.compile()