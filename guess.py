import itertools
from tkinter import END


def guess_password(real, password_display):
    chars = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890&é"(-è_çà)=\'$*ù%£µ!:;,?./§^#@<>|`[]{}\\'
    attempts = 0
    for password_length in range(1, 64):
        for guess in itertools.product(chars, repeat=password_length):
            attempts += 1
            guess = ''.join(guess)
            if guess == real:
                return 'MDP est {}. trouvé en {} essaies.'.format(guess, attempts)
            password_display.insert(END, f'{guess}\n')  # Met à jour le widget Text avec le nouveau mot de passe
            password_display.see(END)  # Fait défiler le widget Text pour montrer le dernier mot de passe