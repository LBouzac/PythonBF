import tkinter as tk
from tkinter import messagebox
import styles
import threading
import guess
import os
import ctypes


class Application:
    ES_CONTINUOUS = 0x80000000
    ES_SYSTEM_REQUIRED = 0x00000001

    def __init__(self):
        self.window = tk.Tk()
        self.stop_threads = False
        self.password_display = None
        self.set_awake()
        self.create_window()

    def set_awake(self):
        if os.name == 'nt':
            # Pour Windows
            ctypes.windll.kernel32.SetThreadExecutionState(
                Application.ES_CONTINUOUS | Application.ES_SYSTEM_REQUIRED)
        elif os.name == 'posix':
            # Pour linux et mac os
            os.system('caffeine &')

    def __init__(self):
        self.window = tk.Tk()
        self.stop_threads = False
        self.password_display = None
        self.create_window()

    def create_window(self):
        styles.interface_style(self.window)

        table = tk.Frame(self.window)
        styles.table_style(table)

        label = tk.Label(table, text="Python Certif")
        styles.style_label(label)
        label.pack()

        button_frame = tk.Frame(self.window)
        styles.button_frame_style(button_frame)

        button = tk.Button(button_frame, text="Clique", command=self.on_button_click)
        button.pack(side=tk.LEFT)
        styles.style_button(button)

        button_exit = tk.Button(button_frame, text="Sortie", command=self.exit_program)
        button_exit.pack(side=tk.LEFT, padx=(10, 0))
        styles.style_button_exit(button_exit)

        self.password_display = tk.Text(self.window)
        self.password_display.pack()

        self.window.mainloop()

    def on_button_click(self):
        if self.stop_threads:
            return

        num_threads = os.cpu_count() or 1

        thread = threading.Thread(target=self.run_brute_force)
        thread.start()

        thread.join()

        print(num_threads)

    def run_brute_force(self):
        try:
            guess.guess_password(guess, self.password_display)
        except Exception as e:
            messagebox.showerror("Error", str(e))

    def exit_program(self):
        self.stop_threads = True
        self.window.quit()


app = Application()