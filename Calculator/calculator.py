import tkinter as tk
from tkinter import messagebox

def button_click(number):
    current = entry.get()
    entry.delete(0, tk.END)
    entry.insert(tk.END, str(current) + str(number))

def button_clear():
    entry.delete(0, tk.END)

def button_equal():
    try:
        result = eval(entry.get())
        entry.delete(0, tk.END)
        entry.insert(tk.END, result)
    except:
        messagebox.showerror("Error", "Invalid Input")

root = tk.Tk()
root.title("Calculator")

entry = tk.Entry(root, width=35, borderwidth=5)
entry.grid(row=0, column=0, columnspan=4, padx=10, pady=10)

buttons = [
    ("7", 1, 0), ("8", 1, 1), ("9", 1, 2), ("/", 1, 3),
    ("4", 2, 0), ("5", 2, 1), ("6", 2, 2), ("*", 2, 3),
    ("1", 3, 0), ("2", 3, 1), ("3", 3, 2), ("-", 3, 3),
    ("0", 4, 0), (".", 4, 1), ("=", 4, 2), ("+", 4, 3),
    ("C", 5, 0), ("(", 5, 1), (")", 5, 2), ("^", 5, 3)
]

for (text, row, column) in buttons:
    button = tk.Button(root, text=text, padx=30, pady=20, command=lambda text=text: button_click(text))
    button.grid(row=row, column=column)

clear_button = tk.Button(root, text="Clear", padx=60, pady=20, command=button_clear)
clear_button.grid(row=6, column=0, columnspan=2)

equal_button = tk.Button(root, text="=", padx=30, pady=20, command=button_equal)
equal_button.grid(row=6, column=2, columnspan=2)

root.mainloop()

