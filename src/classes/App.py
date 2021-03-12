from ursina import *

def App(title: str) -> Ursina:
    app = Ursina()
    window.exit_button.visible = False
    window.borderless = False
    window.title = title
    return app