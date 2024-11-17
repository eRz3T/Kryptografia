import tkinter as tk
from subprocess import Popen
import os

# Funkcje uruchamiające poszczególne GUI
def run_aes_block_gui():
    Popen(["python", os.path.join("AES_blokowy", "gui.py")])

def run_aes_stream_gui():
    Popen(["python", os.path.join("AES_strumieniowy", "gui.py")])

def run_des_block_gui():
    Popen(["python", os.path.join("DES_blokowy", "gui.py")])

def run_des_stream_gui():
    Popen(["python", os.path.join("DES_strumieniowy", "gui.py")])

def run_rsa_gui():
    Popen(["python", os.path.join("Diffie-Hellman", "RSA", "gui.py")])

def run_diffie_hellman_gui():
    Popen(["python", os.path.join("Diffie-Hellman", "simulation.py")])

def run_monoalphabetic_gui():
    Popen(["python", os.path.join("MonoAlfabetyczny", "gui.py")])

def run_transposition_gui():
    Popen(["python", os.path.join("Transpozycyjny", "gui.py")])

# Główne okno aplikacji
app = tk.Tk()
app.title("Launcher - Kryptografia")
app.geometry("400x500")

# Nagłówek
header_label = tk.Label(app, text="Wybierz algorytm szyfrowania", font=("Arial", 14))
header_label.pack(pady=20)

# Lista przycisków dla każdego algorytmu
buttons = [
    ("AES Blokowy", run_aes_block_gui),
    ("AES Strumieniowy", run_aes_stream_gui),
    ("DES Blokowy", run_des_block_gui),
    ("DES Strumieniowy", run_des_stream_gui),
    ("RSA", run_rsa_gui),
    ("Diffie-Hellman", run_diffie_hellman_gui),
    ("Szyfr Monoalfabetyczny", run_monoalphabetic_gui),
    ("Szyfr Transpozycyjny", run_transposition_gui),
]

for text, command in buttons:
    button = tk.Button(app, text=text, command=command, width=30, height=2)
    button.pack(pady=10)

# Uruchomienie pętli głównej
app.mainloop()
