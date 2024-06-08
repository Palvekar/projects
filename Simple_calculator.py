import tkinter as tk
from tkinter import font

def on_button_click(number):
    current = entry.get()
    entry.delete(0, tk.END)
    entry.insert(0, current + str(number))

def clear():
    entry.delete(0, tk.END)

def calculate():
    try:
        result = eval(entry.get())
        entry.delete(0, tk.END)
        entry.insert(0, result)
    except Exception:
        entry.delete(0, tk.END)
        entry.insert(0, "Error")

root = tk.Tk()
root.title("Simple Calculator")

entry = tk.Entry(root, width=30, borderwidth=5)
entry.grid(row=0, column=0, columnspan=4)

# Define a custom font for the buttons
button_font = font.Font(family="Comic Sans MS", size=16, weight="bold")

buttons = [
    ("7", 1, 0), ("8", 1, 1), ("9", 1, 2), ("/", 1, 3),
    ("4", 2, 0), ("5", 2, 1), ("6", 2, 2), ("*", 2, 3),
    ("1", 3, 0), ("2", 3, 1), ("3", 3, 2), ("-", 3, 3),
    ("0", 4, 0), (".", 4, 1), ("+", 4, 3),
]

button_colors = {
    "7": "lightgray", "8": "lightgray", "9": "lightgray", "/": "lightblue",
    "4": "lightgray", "5": "lightgray", "6": "lightgray", "*": "lightblue",
    "1": "lightgray", "2": "lightgray", "3": "lightgray", "-": "lightblue",
    "0": "lightgray", ".": "lightgray", "=": "lightblue", "+": "lightblue"
}

for (text, row, col) in buttons:
    button = tk.Button(root, text=text, padx=20, pady=20, font=button_font, bg=button_colors[text], command=lambda t=text: on_button_click(t))
    button.grid(row=row, column=col)

clear_button = tk.Button(root, text="C", padx=20, pady=20, font=button_font, bg="red", command=clear)
clear_button.grid(row=5, column=0)

calculate_button = tk.Button(root, text="=", padx=20, pady=20, font=button_font, bg="lightblue", command=calculate)
calculate_button.grid(row=5, column=2)

root.mainloop()
