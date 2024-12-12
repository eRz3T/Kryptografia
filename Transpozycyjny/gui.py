import tkinter as tk
from tkinter import filedialog, messagebox
import encrypt
import decrypt
import time  # Dodano moduł do pomiaru czasu
import random
import string
import pyperclip  # Do obsługi schowka

# Funkcja do generowania losowego klucza transpozycyjnego.
def generate_key():
    key = random.randint(2, 50)  # Generowanie losowego klucza w zakresie 2-50 (liczba kolumn).
    key_entry.delete(0, tk.END)  # Wyczyść pole klucza
    key_entry.insert(0, str(key))  # Wstaw wygenerowany klucz

# Funkcja do kopiowania klucza do schowka.
def copy_key():
    key = key_entry.get()
    if key:
        pyperclip.copy(key)
        messagebox.showinfo("Sukces", "Klucz został skopiowany do schowka.")
    else:
        messagebox.showerror("Błąd", "Nie ma klucza do skopiowania!")

# Funkcja do pobierania klucza transpozycyjnego z pola tekstowego GUI.
def get_key():
    try:
        key = int(key_entry.get())
        if key < 2:
            raise ValueError
    except ValueError:
        messagebox.showerror("Błąd", "Klucz musi być liczbą całkowitą większą od 1!")
        return None
    return key

# Funkcja obsługująca szyfrowanie pliku.
def encrypt_file_action():
    file_path = filedialog.askopenfilename(title="Wybierz plik do zaszyfrowania")
    if not file_path:
        return
    output_path = filedialog.asksaveasfilename(title="Zapisz zaszyfrowany plik jako", defaultextension=".txt")
    if not output_path:
        return
    key = get_key()
    if key:
        with open(file_path, 'r') as f:
            data = f.read()

        start_time = time.time()
        encrypted_data = encrypt.encrypt_message(data, key)
        end_time = time.time()

        with open(output_path, 'w') as f:
            f.write(encrypted_data)

        elapsed_time = end_time - start_time
        print(f"Szyfrowanie pliku '{file_path}' zajęło: {elapsed_time:.2f} sekund.")
        messagebox.showinfo("Sukces", "Plik został zaszyfrowany i zapisany.")

# Funkcja obsługująca deszyfrowanie pliku.
def decrypt_file_action():
    file_path = filedialog.askopenfilename(title="Wybierz plik do odszyfrowania")
    if not file_path:
        return
    output_path = filedialog.asksaveasfilename(title="Zapisz odszyfrowany plik jako", defaultextension=".txt")
    if not output_path:
        return
    key = get_key()
    if key:
        with open(file_path, 'r') as f:
            data = f.read()

        start_time = time.time()
        decrypted_data = decrypt.decrypt_message(data, key)
        end_time = time.time()

        with open(output_path, 'w') as f:
            f.write(decrypted_data)

        elapsed_time = end_time - start_time
        print(f"Deszyfrowanie pliku '{file_path}' zajęło: {elapsed_time:.2f} sekund.")
        messagebox.showinfo("Sukces", "Plik został odszyfrowany i zapisany.")

# Funkcja obsługująca szyfrowanie tekstu wpisanego w GUI.
def encrypt_text_action():
    text = text_entry.get("1.0", tk.END).strip()
    if not text:
        messagebox.showerror("Błąd", "Pole tekstu do zaszyfrowania nie może być puste!")
        return
    output_path = filedialog.asksaveasfilename(title="Zapisz zaszyfrowany tekst jako", defaultextension=".txt")
    if not output_path:
        return
    key = get_key()
    if key:
        start_time = time.time()
        encrypted_text = encrypt.encrypt_message(text, key)
        end_time = time.time()

        with open(output_path, 'w') as f:
            f.write(encrypted_text)

        elapsed_time = end_time - start_time
        print(f"Szyfrowanie tekstu zajęło: {elapsed_time:.2f} sekund.")
        messagebox.showinfo("Sukces", "Tekst został zaszyfrowany i zapisany w pliku!")

# Konfiguracja graficznego interfejsu użytkownika.
app = tk.Tk()
app.title("Szyfr Transpozycyjny")

# Główny kontener
main_frame = tk.Frame(app, padx=10, pady=10)
main_frame.pack(fill="both", expand=True, padx=10, pady=10)

# Sekcja klucza
key_frame = tk.LabelFrame(main_frame, text="Klucz transpozycyjny", padx=10, pady=10)
key_frame.pack(fill="x", pady=10)

key_label = tk.Label(key_frame, text="Klucz (liczba kolumn):")
key_label.pack(anchor="center", pady=5)

key_entry = tk.Entry(key_frame, width=50)
key_entry.pack(fill="x", pady=5)

generate_key_button = tk.Button(key_frame, text="Wygeneruj klucz", command=generate_key)
generate_key_button.pack(fill="x", pady=5)

copy_key_button = tk.Button(key_frame, text="Kopiuj klucz", command=copy_key)
copy_key_button.pack(fill="x", pady=5)

# Sekcja tekstu
text_frame = tk.LabelFrame(main_frame, text="Operacje na tekście", padx=10, pady=10)
text_frame.pack(fill="x", pady=10)

text_label = tk.Label(text_frame, text="Tekst do szyfrowania:")
text_label.pack(anchor="w", pady=5)

text_entry = tk.Text(text_frame, height=10, width=50)
text_entry.pack(fill="x", pady=5)

encrypt_text_button = tk.Button(text_frame, text="Zaszyfruj tekst do pliku", command=encrypt_text_action)
encrypt_text_button.pack(fill="x", pady=5)

# Sekcja plików
file_frame = tk.LabelFrame(main_frame, text="Operacje na plikach", padx=10, pady=10)
file_frame.pack(fill="x", pady=10)

encrypt_button = tk.Button(file_frame, text="Zaszyfruj plik", command=encrypt_file_action)
encrypt_button.pack(fill="x", pady=5)

decrypt_button = tk.Button(file_frame, text="Odszyfruj plik", command=decrypt_file_action)
decrypt_button.pack(fill="x", pady=5)

# Rozmiar okna
app.geometry("520x700")
app.mainloop()