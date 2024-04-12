import tkinter as tk
import tkinter.font as tkFont


def get_font():
    available_fonts = tkFont.families()
    if "Aptos" in available_fonts:
        return "Aptos"
    else:
        return "Arial"


def style_button(button):
    font = get_font()
    button.config(width=10, height=2, font=(font, 12), bg="lightblue")


def style_button_exit(button_exit):
    font = get_font()
    button_exit.config(width=10, height=2, font=(font, 12), bg="lightcoral")


def style_label(label):
    font = get_font()
    label.config(font=(font, 24), bg="lightgray")


def button_frame_style(button_frame):
    button_frame.config(bg="lightgray")
    button_frame.pack(side=tk.BOTTOM, pady=20)


def interface_style(window):
    window.title("Python Certif")
    window.geometry("+5+5")
    window.geometry("250x300")
    window.config(bg="lightgray")


def table_style(table):
    table.config(bg="lightgray")
    table.pack(side=tk.TOP, pady=20)
