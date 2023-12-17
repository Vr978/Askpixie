from typing import Any, Dict
css: dict={
    "_light": {
        "bg" : "white",
        "box_shadow": "Opx 8px 16px 0px rgba(0, 0, 0, 0.35)",
        "padding":["1rem"],
    },
    "app": {
        "_dark": {"bg": "#1f2128"},
        "_light": {"bg": "#312e2a"},
        "font-family": "Gill Sans",
    },
    "header":{
        "width": "100%",
        "height": "7vh",
        "box_shadow": "Opx 8px 16px 0px rgba(0, 0, 0, 0.35)",
        "justify_content": "center",
        "padding": ["0 1rem", "O 1rem", "O 1rem", "o 4rem", "O 10rem"],
        "transition": "all 400ms ease", 

    "_dark": {
        "bg":"#1f2128",
    },
   "_light": {
        "bg" : "white",
        "box_shadow": "Opx 8px 16px 0px rgba(0, 0, 0, 0.35)",
        "padding":["1rem"],
    },
    },
    
    "content": {
    "width": "100%",
    "display": "flex",
    "flex-wrap":"wrap",
    "align_item": "center",
    "justify_content": "center",
    },

    "workSpace": {
        "width" : "100%",
        "display": "flex",
        "align_item": "center",
        "justify_content": "center",
        "height": "100vh",
    },
    "main": {
    "width": "100%",
    "display": "flex",
    "align_item": "center",
    "justify_content": "center",
    "height": "100vh",
},
    
    "navbar":{
      "color": "white",
      "margin":"2em",
    },
    
}

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
    "rectangle": create_box_dimensions ("5em", "10.5em"),
    "custom-1": create_box_dimensions ("10.5em", "10.5em"),
    "custom-2": create_box_dimensions ("10.5em", "5em"),
    "square": create_box_dimensions("5em", "5em"),
}
    


# blinking animation for display cursor
blink: dict = {
    "@keyframes blink": {
        "0%": {"opacity": "0"},
        "50%":{"opacity": "1"},
        "100%": {"opacity": "0"},
    },
"animation": "blink 0.9s infinite",
}