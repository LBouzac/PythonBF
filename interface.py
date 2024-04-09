import tkinter as tk
from tkinter import *
import styles

def create_window():

    window = tk.Tk()
    styles.interface_style(window)

    table = tk.Frame(window)
    styles.table_style(table)


    button_frame = tk.Frame(window)
    styles.button_frame_style(button_frame)


    button = tk.Button(button_frame, text="Clique", command=on_button_click)
    button.pack(side=tk.LEFT)
    styles.style_button(button)

    button_exit = tk.Button(button_frame, text="Exit", command=exit_program)
    button_exit.pack(side=tk.LEFT, padx=(10, 0))
    styles.style_button_exit(button_exit)

    monAffichage = Label(window, text="")
    monAffichage.pack()

    global password_display
    password_display = Text(window)
    password_display.pack()

    window.mainloop()

def on_button_click():
    import guess
    guess.guess_password('Aa', password_display)

def exit_program():  # Renommez la fonction ici
    exit()

create_window()