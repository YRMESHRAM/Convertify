from tkinter import *
from tkinter import ttk
import tkinter.font as tkFont

def reset():
    input_field.delete(0, END)
    output_field.delete(0, END)
    input_value.set(SELECTIONS[0])
    output_value.set(SELECTIONS[0])
    input_field.focus_set()
    update_output_units()

def update_output_units(*args):
    selected_unit = input_value.get()

    if selected_unit in length_units:
        updated_options = length_units
    elif selected_unit in weight_units:
        updated_options = weight_units
    elif selected_unit in temperature_units:
        updated_options = temperature_units
    elif selected_unit in area_units:
        updated_options = area_units
    elif selected_unit in volume_units:
        updated_options = volume_units
    else:
        updated_options = [SELECTIONS[0]]

    output_menu['menu'].delete(0, 'end')
    for unit in updated_options:
        output_menu['menu'].add_command(label=unit, command=lambda value=unit: output_value.set(value))
    output_value.set(updated_options[0])

def convert():
    try:
        inputVal = float(input_field.get())
        input_unit = input_value.get()
        output_unit = output_value.get()

        conversion_factors = [
            input_unit in length_units and output_unit in length_units,
            input_unit in weight_units and output_unit in weight_units,
            input_unit in temperature_units and output_unit in temperature_units,
            input_unit in area_units and output_unit in area_units,
            input_unit in volume_units and output_unit in volume_units
        ]

        if any(conversion_factors):
            if input_unit == "celsius" and output_unit == "fahrenheit":
                output_field.delete(0, END)
                output_field.insert(0, (inputVal * 1.8) + 32)
            elif input_unit == "fahrenheit" and output_unit == "celsius":
                output_field.delete(0, END)
                output_field.insert(0, (inputVal - 32) * (5 / 9))
            else:
                output_field.delete(0, END)
                output_field.insert(0, round(inputVal * unitDict[input_unit] / unitDict[output_unit], 5))
        else:
            output_field.delete(0, END)
            output_field.insert(0, "ERROR")
    except ValueError:
        output_field.delete(0, END)
        output_field.insert(0, "Invalid Input")

def on_enter(event, btn):
    btn.config(bg="#66bb6a", relief=RAISED)

def on_leave(event, btn):
    btn.config(bg="#4caf50", relief=FLAT)

def reset_hover(event, btn):
    btn.config(bg="#e57373", relief=RAISED)

def reset_leave(event, btn):
    btn.config(bg="#f44336", relief=FLAT)

if __name__ == "__main__":
    unitDict = {
        "millimeter": 0.001,
        "centimeter": 0.01,
        "meter": 1.0,
        "kilometer": 1000.0,
        "foot": 0.3048,
        "mile": 1609.344,
        "yard": 0.9144,
        "inch": 0.0254,
        "square meter": 1.0,
        "square kilometer": 1000000.0,
        "square centimeter": 0.0001,
        "square millimeter": 0.000001,
        "are": 100.0,
        "hectare": 10000.0,
        "acre": 4046.856,
        "square mile": 2590000.0,
        "square foot": 0.0929,
        "cubic meter": 1000.0,
        "cubic centimeter": 0.001,
        "litre": 1.0,
        "millilitre": 0.001,
        "gallon": 3.785,
        "gram": 1.0,
        "kilogram": 1000.0,
        "milligram": 0.001,
        "quintal": 100000.0,
        "ton": 1000000.0,
        "pound": 453.592,
        "ounce": 28.3495
    }

    length_units = ["millimeter", "centimeter", "meter", "kilometer", "foot", "mile", "yard", "inch"]
    temperature_units = ["celsius", "fahrenheit"]
    area_units = ["square meter", "square kilometer", "square centimeter", "square millimeter", "are", "hectare", "acre", "square mile", "square foot"]
    volume_units = ["cubic meter", "cubic centimeter", "litre", "millilitre", "gallon"]
    weight_units = ["gram", "kilogram", "milligram", "quintal", "ton", "pound"]

    SELECTIONS = [
        "Select Unit", "millimeter", "centimeter", "meter", "kilometer", 
        "foot", "mile", "yard", "inch", "celsius", "fahrenheit", 
        "square meter", "square kilometer", "square centimeter", 
        "square millimeter", "are", "hectare", "acre", "square mile", 
        "square foot", "cubic meter", "cubic centimeter", "litre", 
        "millilitre", "gallon", "gram", "kilogram", "milligram", 
        "quintal", "ton", "pound"
    ]

    guiWindow = Tk()
    guiWindow.title("Modern Unit Converter")
    guiWindow.geometry("800x600")
    guiWindow.configure(bg="#1c1c1c")

    header_frame = Frame(guiWindow, bg="#262626", height=100)
    body_frame = Frame(guiWindow, bg="#1c1c1c")

    header_frame.pack(fill="x")
    body_frame.pack(expand=True, fill="both")

    header_label = Label(
        header_frame,
        text="Unit Converter",
        font=("Arial", 28, "bold"),
        bg="#262626",
        fg="#ffffff",
        pady=20
    )
    header_label.pack(expand=True)

    input_value = StringVar()
    output_value = StringVar()
    input_value.set(SELECTIONS[0])
    output_value.set(SELECTIONS[0])

    input_value.trace("w", update_output_units)

    input_label = Label(
        body_frame,
        text="Convert From:",
        font=("Arial", 16, "bold"),
        bg="#1c1c1c",
        fg="#ffffff"
    )
    output_label = Label(
        body_frame,
        text="Convert To:",
        font=("Arial", 16, "bold"),
        bg="#1c1c1c",
        fg="#ffffff"
    )

    input_label.grid(row=1, column=1, padx=20, pady=20, sticky=W)
    output_label.grid(row=2, column=1, padx=20, pady=20, sticky=W)

    input_field = Entry(body_frame, font=("Arial", 14), bg="#333333", fg="#ffffff", width=30, bd=0, relief=FLAT, insertbackground="#ffffff")
    output_field = Entry(body_frame, font=("Arial", 14), bg="#333333", fg="#ffffff", width=30, bd=0, relief=FLAT, insertbackground="#ffffff")

    input_field.grid(row=1, column=2, padx=10, pady=10)
    output_field.grid(row=2, column=2, padx=10, pady=10)

    input_menu = OptionMenu(body_frame, input_value, *SELECTIONS)
    output_menu = OptionMenu(body_frame, output_value, *SELECTIONS)

    input_menu.grid(row=1, column=3, padx=10, pady=10)
    output_menu.grid(row=2, column=3, padx=10, pady=10)

    input_menu.config(bg="#333333", fg="#ffffff", font=("Arial", 12), relief=FLAT, highlightbackground="#333333")
    output_menu.config(bg="#333333", fg="#ffffff", font=("Arial", 12), relief=FLAT, highlightbackground="#333333")

    button_font = tkFont.Font(family='Arial', size=14, weight='bold')

    convert_button = Button(
        body_frame,
        text="Convert",
        font=button_font,
        bg="#4caf50",
        fg="#ffffff",
        command=convert,
        bd=0,
        relief=FLAT,
        width=15,
        highlightbackground="#4caf50",
        activebackground="#66bb6a",
        activeforeground="#ffffff",
        borderwidth=0,
        highlightthickness=0
    )
    reset_button = Button(
        body_frame,
        text="Reset",
        font=button_font,
        bg="#f44336",
        fg="#ffffff",
        command=reset,
        bd=0,
        relief=FLAT,
        width=15,
        highlightbackground="#f44336",
        activebackground="#e57373",
        activeforeground="#ffffff",
        borderwidth=0,
        highlightthickness=0
    )

    # Align both buttons in the same row (row=3)
    convert_button.grid(row=3, column=2, pady=40)
    reset_button.grid(row=4, column=2, pady=20)  

    # Add hover effects for both buttons
    convert_button.bind("<Enter>", lambda e, btn=convert_button: on_enter(e, btn))
    convert_button.bind("<Leave>", lambda e, btn=convert_button: on_leave(e, btn))
    reset_button.bind("<Enter>", lambda e, btn=reset_button: reset_hover(e, btn))
    reset_button.bind("<Leave>", lambda e, btn=reset_button: reset_leave(e, btn))

    guiWindow.mainloop()
