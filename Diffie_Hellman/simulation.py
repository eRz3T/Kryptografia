import tkinter as tk
from tkinter import messagebox
import random


def diffie_hellman(p, g):
    """
    Implementacja protokołu Diffiego-Hellmana do generowania wspólnego klucza.
    """
    x = random.randint(1, p - 1)  # Klucz prywatny Alicji
    A = pow(g, x, p)  # Klucz publiczny Alicji
    y = random.randint(1, p - 1)  # Klucz prywatny Boba
    B = pow(g, y, p)  # Klucz publiczny Boba
    K_alice = pow(B, x, p)  # Klucz współdzielony obliczony przez Alicję
    K_bob = pow(A, y, p)  # Klucz współdzielony obliczony przez Boba
    assert K_alice == K_bob, "Klucze się nie zgadzają!"
    return K_alice


def generate_shared_key(public=None, private=None):
    """
    Funkcja wspomagająca testy. Może generować klucze publiczne i prywatne
    lub obliczać klucz współdzielony.
    """
    prime = 23  # Przykładowa liczba pierwsza (p)
    base = 5  # Generator (g)

    if public is None and private is None:
        # Generowanie kluczy prywatnych i publicznych
        private_key = random.randint(1, prime - 1)
        public_key = pow(base, private_key, prime)
        return public_key, private_key
    elif public is not None and private is not None:
        # Obliczanie klucza współdzielonego
        shared_key = pow(public, private, prime)
        return shared_key
    else:
        raise ValueError("Zarówno klucz publiczny, jak i prywatny muszą być podane, aby obliczyć klucz współdzielony.")


def simulate_diffie_hellman():
    """
    Symulacja protokołu Diffiego-Hellmana z GUI.
    """
    p = 23  # Liczba pierwsza
    g = 5  # Generator
    try:
        shared_key = diffie_hellman(p, g)
        messagebox.showinfo("Wynik", f"Alicja i Bob dzielą wspólny klucz: {shared_key}")
    except AssertionError as e:
        messagebox.showerror("Błąd", str(e))


# Interfejs graficzny
app = tk.Tk()
app.title("Symulacja protokołu Diffiego-Hellmana")

label = tk.Label(app, text="Kliknij 'Symuluj', aby wygenerować wspólny klucz.")
label.pack(pady=10)

simulate_button = tk.Button(app, text="Symuluj", command=simulate_diffie_hellman)
simulate_button.pack(pady=10)

app.geometry("300x150")
app.mainloop()
