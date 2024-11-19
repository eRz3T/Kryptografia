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


def generate_shared_key(public=None, private=None):
    """
    Funkcja wspomagająca generowanie kluczy lub obliczanie klucza współdzielonego.

    Parametry:
    - public: klucz publiczny (opcjonalny).
    - private: klucz prywatny (opcjonalny).

    Jeśli oba parametry są None, generuje klucz publiczny i prywatny.
    Jeśli oba parametry są podane, oblicza klucz współdzielony.
    
    Zwraca:
    - Klucz publiczny i prywatny lub klucz współdzielony w zależności od trybu.
    """
    prime = 23  # Przykładowa liczba pierwsza (moduł p).
    base = 5  # Generator (g).

    if public is None and private is None:
        # Generowanie kluczy publicznych i prywatnych.
        private_key = random.randint(1, prime - 1)
        public_key = pow(base, private_key, prime)
        return public_key, private_key
    elif public is not None and private is not None:
        # Obliczanie klucza współdzielonego.
        shared_key = pow(public, private, prime)
        return shared_key
    else:
        # Jeśli niepoprawne argumenty, zgłaszamy błąd.
        raise ValueError("Podaj zarówno klucz publiczny, jak i prywatny, aby obliczyć klucz współdzielony.")


def simulate_diffie_hellman():
    """
    Symulacja protokołu Diffiego-Hellmana z wykorzystaniem przykładowych parametrów.
    Wyświetla wynik w oknie dialogowym.
    """
    p = 23  # Przykładowa liczba pierwsza (moduł).
    g = 5  # Przykładowy generator (podstawa).

    try:
        # Wywołanie funkcji do symulacji Diffiego-Hellmana.
        shared_key = diffie_hellman(p, g)
        # Wyświetlenie wyniku: wspólny klucz obliczony przez Alicję i Boba.
        messagebox.showinfo("Wynik", f"Alicja i Bob dzielą wspólny klucz: {shared_key}")
    except AssertionError as e:
        # Wyświetlenie błędu, jeśli klucze się nie zgadzają.
        messagebox.showerror("Błąd", str(e))


# Konfiguracja graficznego interfejsu użytkownika (GUI).
app = tk.Tk()
app.title("Symulacja protokołu Diffiego-Hellmana")

# Etykieta wyświetlana w oknie GUI.
label = tk.Label(app, text="Kliknij 'Symuluj', aby wygenerować wspólny klucz.")
label.pack(pady=10)

# Przycisk uruchamiający symulację Diffiego-Hellmana.
simulate_button = tk.Button(app, text="Symuluj", command=simulate_diffie_hellman)
simulate_button.pack(pady=10)

# Ustawienie rozmiaru okna GUI.
app.geometry("300x150")

# Uruchomienie pętli głównej GUI.
app.mainloop()
