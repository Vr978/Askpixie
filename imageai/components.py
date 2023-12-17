import reflex as rx
from .state import AppState


class Box(rx.Container):
    def __init__(
        self,
        shape: str,
        border_color:str,
        size: str,
        icon: str="bell",
        function: callable= AppState.emptyFunction,
    )->None:
        super().__init__(
            style= shape,
            border= f"5px double {border_color}",
            cursor= "pointer",
            border_radius= "10px",
            on_click=function,
            children=[
                rx.icon(
                    tag= icon,
                    transform= f"Scale({size})",
                    _light={"color": "rgba(255,255,255,0.81)"},
                )
            ]
        )