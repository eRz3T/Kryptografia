import tkinter as tk
from tkinter import messagebox
import random


def diffie_hellman(p, g):
    """
    Implementacja protokołu Diffiego-Hellmana do generowania wspólnego klucza.
    
    Parametry:
    - p: liczba pierwsza (moduł).
    - g: generator (podstawa potęgowania w grupie modulo p).
    
    Zwraca:
    - Klucz współdzielony, który jest identyczny dla obu stron (Alicji i Boba).
    """
    # Alicja generuje swój klucz prywatny (losowa liczba 1 <= x < p).
    x = random.randint(1, p - 1)
    # Alicja oblicza swój klucz publiczny: A = g^x mod p.
    A = pow(g, x, p)

    # Bob generuje swój klucz prywatny (losowa liczba 1 <= y < p).
    y = random.randint(1, p - 1)
    # Bob oblicza swój klucz publiczny: B = g^y mod p.
    B = pow(g, y, p)

    # Alicja oblicza wspólny klucz na podstawie klucza publicznego Boba i swojego klucza prywatnego.
    K_alice = pow(B, x, p)
    # Bob oblicza wspólny klucz na podstawie klucza publicznego Alicji i swojego klucza prywatnego.
    K_bob = pow(A, y, p)

    # Weryfikacja, czy obliczone klucze są zgodne.
    assert K_alice == K_bob, "Klucze współdzielone nie zgadzają się!"

    # Zwracamy wspólny klucz (ten sam dla obu stron).
    return K_alice


def simulate_diffie_hellman():
    """
    Symulacja protokołu Diffiego-Hellmana z wykorzystaniem przykładowych parametrów.
    Wyświetla wynik w sekcji przebiegu i klucza.
    """
    progress_text.delete("1.0", tk.END)  # Czyszczenie okna przebiegu

    p = 23  # Przykładowa liczba pierwsza (moduł).
    g = 5  # Przykładowy generator (podstawa).

    try:
        x = random.randint(1, p - 1)
        y = random.randint(1, p - 1)
        A = pow(g, x, p)
        B = pow(g, y, p)
        shared_key = pow(B, x, p)

        # Wyświetlanie przebiegu
        progress_text.insert(tk.END, f"Parametry protokołu: p = {p}, g = {g}\n")
        progress_text.insert(tk.END, f"Alicja wybiera klucz prywatny x = {x}\n")
        progress_text.insert(tk.END, f"Bob wybiera klucz prywatny y = {y}\n")
        progress_text.insert(tk.END, f"Alicja oblicza klucz publiczny A = g^x mod p = {A}\n")
        progress_text.insert(tk.END, f"Bob oblicza klucz publiczny B = g^y mod p = {B}\n")
        progress_text.insert(tk.END, f"Alicja oblicza wspólny klucz K = B^x mod p = {shared_key}\n")
        progress_text.insert(tk.END, f"Bob oblicza wspólny klucz K = A^y mod p = {shared_key}\n")

        # Wyświetlanie klucza
        key_text.set(f"Wspólny klucz: {shared_key}")
    except AssertionError as e:
        messagebox.showerror("Błąd", str(e))


# Konfiguracja GUI
app = tk.Tk()
app.title("Diffie-Hellman - symulacja")
app.geometry("700x500")

# Główny kontener
main_frame = tk.Frame(app, padx=10, pady=10)
main_frame.pack(fill="both", expand=True, padx=10, pady=10)

# Sekcja generowania
generate_frame = tk.LabelFrame(main_frame, text="Generowanie", padx=10, pady=10)
generate_frame.pack(fill="x", pady=10)

generate_button = tk.Button(generate_frame, text="Symuluj Diffie-Hellman", command=simulate_diffie_hellman)
generate_button.pack()

# Sekcja przebiegu
progress_frame = tk.LabelFrame(main_frame, text="Przebieg protokołu", padx=10, pady=10)
progress_frame.pack(fill="both", expand=True, pady=10)

progress_text = tk.Text(progress_frame, wrap=tk.WORD, height=15, width=80)
progress_text.pack(fill="both", expand=True)

# Sekcja klucza
key_frame = tk.LabelFrame(main_frame, text="Klucz", padx=10, pady=10)
key_frame.pack(fill="x", pady=10)

key_text = tk.StringVar()
key_label = tk.Label(key_frame, textvariable=key_text, wraplength=650, justify="center")
key_label.pack()

# Uruchomienie aplikacji
app.mainloop()
