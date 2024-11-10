import tkinter as tk
from tkinter import messagebox
import random

# Funkcja do symulacji protokołu Diffiego-Hellmana
def diffie_hellman(p, g):
    # Alicja wybiera sekret x
    x = random.randint(1, p - 1)
    A = pow(g, x, p)  # A = g^x mod p

    # Bob wybiera sekret y
    y = random.randint(1, p - 1)
    B = pow(g, y, p)  # B = g^y mod p

    # Alicja oblicza wspólny klucz K = B^x mod p
    K_alice = pow(B, x, p)

    # Bob oblicza wspólny klucz K = A^y mod p
    K_bob = pow(A, y, p)

    # Wspólny klucz powinien być identyczny
    assert K_alice == K_bob, "Klucze się nie zgadzają!"

    return K_alice

# Funkcja obsługująca kliknięcie przycisku
def simulate_diffie_hellman():
    # Parametry protokołu (publiczne)
    p = 23  # liczba pierwsza
    g = 5   # baza

    try:
        # Symulacja protokołu Diffiego-Hellmana
        shared_key = diffie_hellman(p, g)
        messagebox.showinfo("Wynik", f"Alicja i Bob dzielą wspólny klucz: {shared_key}")
    except AssertionError as e:
        messagebox.showerror("Błąd", str(e))

# Konfiguracja GUI
app = tk.Tk()
app.title("Symulacja protokołu Diffiego-Hellmana")

label = tk.Label(app, text="Kliknij 'Symuluj', aby wygenerować wspólny klucz.")
label.pack(pady=10)

simulate_button = tk.Button(app, text="Symuluj", command=simulate_diffie_hellman)
simulate_button.pack(pady=10)

app.geometry("300x150")
app.mainloop()
