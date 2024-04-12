import itertools
import threading
import time
from tkinter import END

MAX_PASSWORD_LENGTH = 64
CHARS = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890&é"(-è_çà)=\'$*ù%£µ!:;,?./§^#@<>|`[]{}\\'


def guess_password(real, password_display):
    def update_display(message):
        password_display.insert(END, message)
        password_display.see(END)
        password_display.update_idletasks()

    def run():
        attempts = 0
        start_time = time.perf_counter()
        try:
            for password_length in range(6, MAX_PASSWORD_LENGTH):
                for guess in itertools.product(CHARS, repeat=password_length):
                    attempts += 1
                    guess = ''.join(guess)
                    if guess == real:
                        end_time = time.perf_counter()
                        time_taken = round(end_time - start_time, 3)
                        result = f'\n\nLe mot de passe est {guess}. \nTrouvé après {attempts} tentatives. \nDurée: {time_taken} secondes.\n'
                        update_display(result)
                        return
                    update_display(f'{guess}\n')
        finally:
            update_display("Finis le MDP n'a pas été trouvé\n")

    threading.Thread(target=run).start()
