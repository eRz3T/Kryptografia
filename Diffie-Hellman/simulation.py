import tkinter as tk
from tkinter import messagebox
import random

def diffie_hellman(p, g):
    x = random.randint(1, p - 1)
    A = pow(g, x, p)
    y = random.randint(1, p - 1)
    B = pow(g, y, p)
    K_alice = pow(B, x, p)
    K_bob = pow(A, y, p)
    assert K_alice == K_bob, "Klucze się nie zgadzają!"
    return K_alice

def simulate_diffie_hellman():
    p = 23
    g = 5
    try:
        shared_key = diffie_hellman(p, g)
        messagebox.showinfo("Wynik", f"Alicja i Bob dzielą wspólny klucz: {shared_key}")
    except AssertionError as e:
        messagebox.showerror("Błąd", str(e))

app = tk.Tk()
app.title("Symulacja protokołu Diffiego-Hellmana")

label = tk.Label(app, text="Kliknij 'Symuluj', aby wygenerować wspólny klucz.")
label.pack(pady=10)

simulate_button = tk.Button(app, text="Symuluj", command=simulate_diffie_hellman)
simulate_button.pack(pady=10)

app.geometry("300x150")
app.mainloop()
