import tkinter as tk
def style_button(button):
    button.config(width=10, height=2, font=("Arial", 12), bg="lightblue")

def style_button_exit(button_exit):
    button_exit.config(width=10, height=2, font=("Arial", 12), bg="lightcoral")

def button_frame_style(button_frame):
    button_frame.config(bg="lightgray")
    button_frame.pack(side=tk.BOTTOM, pady=20)

def interface_style(window):
    window.title("Python Certif")
    window.geometry("720x540")
    window.resizable(False, False)
    window.config(bg="lightgray")

def table_style(table):
    table.config(bg="red")
    table.pack(expand=True, fill=tk.BOTH)