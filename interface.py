import tkinter as tk
from tkinter import Label


def create_window():
    window = tk.Tk()  # Crée une nouvelle fenêtre
    window.title("Python Certif")
    window.geometry("720x540")  # Définit la taille de la fenêtre

    button = tk.Button(window, text="Clique", command=on_button_click)
    button.pack()

    monAffichage = Label(window, text="C’est ici que j’affiche mon premier texte !")

    monAffichage.pack()


    window.mainloop()

def on_button_click():
    import guess
    print(guess.guess_password('Aa'))


create_window()