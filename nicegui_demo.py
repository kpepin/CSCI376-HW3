from nicegui import ui 

with ui.row():
    with ui.card.classes("mx-auto"):
        ui.label("Hello world! Making changes").classes("text-xl")
    
    with ui.card():
        ui.label("Hello world making changes")

ui.run()