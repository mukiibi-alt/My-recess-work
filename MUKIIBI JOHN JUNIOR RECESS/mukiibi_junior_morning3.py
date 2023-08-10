# tkinter learn 
# Assignment create a simple calculator program with a GUI interface.
# Make the title of the calculator program window with your name
import tkinter as tk

def calculate():
    try:
        num1 = float(entry_num1.get())
        num2 = float(entry_num2.get())
        operator = dropdown_operator.get()

        if operator == "+":
            result = num1 + num2
        elif operator == "-":
            result = num1 - num2
        elif operator == "*":
            result = num1 * num2
        elif operator == "/":
            result = num1 / num2

        result_text.config(text=str(result))
    except ValueError:
        result_text.config(text="Error: Invalid input")

# Create the main window
window = tk.Tk()
window.title("Junior's Calculator")

# Create input labels and entry fields
label_num1 = tk.Label(window, text="Number 1:")
label_num1.pack()
entry_num1 = tk.Entry(window)
entry_num1.pack()

label_operator = tk.Label(window, text="Operator:")
label_operator.pack()
dropdown_operator = tk.StringVar(window)
dropdown = tk.OptionMenu(window, dropdown_operator, "+", "-", "*", "/")
dropdown.pack()

label_num2 = tk.Label(window, text="Number 2:")
label_num2.pack()
entry_num2 = tk.Entry(window)
entry_num2.pack()

# Create the calculate button
button_calculate = tk.Button(window, text="Calculate", command=calculate)
button_calculate.pack()

# Create a label to display the result
result_text = tk.Label(window, text="Result: ")
result_text.pack()

# Start the GUI event loop
window.mainloop()
