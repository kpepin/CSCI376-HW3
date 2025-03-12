from nicegui import ui

ui.colors(
    primary = '#b30f33',
    secondary = '#e7c84d',
    accent = '#3a5e9c',
    dark = '#850623',
    positive = '#21BA45',
    negative = '#ff0000',
    info = '#ffffff',
    warning = '#ff7b00'
)

def convert():
    try: 
        temp = float(input_field.value)
        if conversion_type.value == "Celsius to Fahrenheit":
            result_label.set_text(f"{temp}°C = {temp * 9/5 + 32:.2f}°F")
        else:
            result_label.set_text(f"{temp}°F = {(temp - 32) * 5/9:.2f}°C")
        result_label.classes("text-lg font-semibold !text-positive mt-4")
        # text-positive: the text is colored in the positive color
    except ValueError:
        result_label.set_text("Please enter a valid number.")
        result_label.classes("text-lg font-semibold text-negative mt-4")
        # text-negative: the text is colored in the negative color

def convertv2():
    try: 
        temp = float(temp2.value)
        if conversion_type2.value == "Celsius to Fahrenheit":
            result_label2.set_text(f"{temp}°C = {temp * 9/5 + 32:.2f}°F")
        else:
            result_label2.set_text(f"{temp}°F = {(temp - 32) * 5/9:.2f}°C")
        result_label2.classes("text-lg font-semibold !text-positive mt-4")
    except ValueError:
        result_label2.set_text("Please enter a valid number.")
        result_label2.classes("text-lg font-semibold text-negative mt-4")


with ui.row().classes("mx-auto"):
    with ui.card().classes("w-100 p-6 shadow-xl mx-auto mt-10 rounded-xl"):
        # w-100: Set element width to be fixed at 100
        # p-6: Adds 1.5rem (24px) of padding to all four sides of the element
        # shadow-xl: shadow-xl applies a large box-shadow to an element
        # mx-auto: creates automatic horizontal margins to center an element within its container
        # mt-10: applies a top margin of 2.5rem (40px) to element
        # rounded-xl: large border-radius to an element, giving it rounded corners
        ui.label("Temperature Converter").classes("text-2xl font-bold text-accent mb-4")
        # text-2xl: sets the font size in the element to 1.5rem (24px) 
        # font-bold: applies bold to the text within the element
        # text-accent: applies the accent color declared at the top of the page to text in element
        # mb-4: applies a 1rem (16px) marbin to the bottom of an element
        input_field = ui.input("Enter Temperature").props('type="number"').classes("w-full mb-4 p-2 text-lg border rounded")
        # w-full: sets tghe width of the element to 100% of the container it is inside of
        # border: applies the default border to the element
        # rounded: makes the element have rounded corners, with a default of 4px of roundness
        conversion_type = ui.radio(["Celsius to Fahrenheit", "Fahrenheit to Celsius"], value="Celsius to Fahrenheit").classes("mb-4")
        convert_button = ui.button("Convert", on_click=convert).classes("text-white font-bold py-2 px-4 rounded")
        # text-white: sets the font color of the text in the element to white
        # py-2: adds padding to the top and bottom of the element, with a default of 8px
        # px-4: adds 16px of padding to the left and right of the element
        result_label = ui.label("").classes("text-lg mt-4")
    with ui.card().classes("w-100 p-6 shadow-xl mx-auto mt-10 rounded-xl"):
        ui.label("Temperature Converter #2").classes("text-2xl font-bold text-accent mb-4")
        temp2 = ui.number(label='Number', value=0, format='%.2f', on_change=convertv2)
        conversion_type2= ui.radio(["Celsius to Fahrenheit", "Fahrenheit to Celsius"], value="Celsius to Fahrenheit", on_change = convertv2,).classes("mb-4")
        result_label2 = ui.label("").classes("text-lg mt-4")

ui.run(port=8081)