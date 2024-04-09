import tkinter as tk
from tkinter import Label, Text, END

def create_window():
    window = tk.Tk()  # Crée une nouvelle fenêtre
    window.title("Python Certif")
    window.geometry("720x540")  # Définit la taille de la fenêtre

    button = tk.Button(window, text="Clique", command=on_button_click)
    button.pack()

    button_exit = tk.Button(window, text="Exit", command=exit_program)  # Utilisez le nouveau nom de la fonction ici
    button_exit.pack()

    monAffichage = Label(window, text="C’est ici que j’affiche mon premier texte !")
    monAffichage.pack()

    # Ajoutez ce widget Text
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