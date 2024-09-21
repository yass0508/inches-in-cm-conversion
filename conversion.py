import tkinter as tk
from tkinter import messagebox

def convert_to_centimeters():
    try:
        inches = float(entry.get())
        centimeters = inches * 2.54
        result_label.config(text=f"{inches} inches = {centimeters:.2f} centimeters")
    except ValueError:
        messagebox.showerror("Invalid input", "Please enter a valid number.")


root = tk.Tk()
root.title("Inches to Centimeters Converter")
root.geometry("400x400")

input_label = tk.Label(root, text="Enter length in inches:")
input_label.pack(pady=10)


entry = tk.Entry(root)
entry.pack(pady=5)


convert_button = tk.Button(root, text="Convert", command=convert_to_centimeters)
convert_button.pack(pady=10)


result_label = tk.Label(root, text="")
result_label.pack(pady=10)


root.mainloop()
