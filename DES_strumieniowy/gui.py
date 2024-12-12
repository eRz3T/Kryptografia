import tkinter as tk
from tkinter import filedialog, messagebox
from encrypt import encrypt_stream
from decrypt import decrypt_stream
import time  # Dodano moduł do pomiaru czasu
import random
import string
import pyperclip  # Do obsługi schowka

# Funkcja do generowania losowego klucza DES.
def generate_key():
    key = ''.join(random.choices(string.ascii_letters + string.digits, k=8))
    key_entry.delete(0, tk.END)  # Wyczyść pole klucza
    key_entry.insert(0, key)  # Wstaw wygenerowany klucz

# Funkcja do kopiowania klucza do schowka.
def copy_key():
    key = key_entry.get()
    if key:
        pyperclip.copy(key)
        messagebox.showinfo("Sukces", "Klucz został skopiowany do schowka.")
    else:
        messagebox.showerror("Błąd", "Nie ma klucza do skopiowania!")

# Funkcja do pobierania klucza DES z pola tekstowego GUI.
def get_key():
    key = key_entry.get().encode()  # Pobranie klucza i zakodowanie jako bajty.
    if len(key) != 8:  # Sprawdzenie długości klucza.
        messagebox.showerror("Error", "Klucz DES musi mieć 8 znaków!")
        return None
    return key

# Funkcja obsługująca szyfrowanie pliku.
def encrypt_file_action():
    file_path = filedialog.askopenfilename(title="Wybierz plik do zaszyfrowania")
    if not file_path:
        return
    output_path = filedialog.asksaveasfilename(title="Zapisz zaszyfrowany plik jako")
    if not output_path:
        return
    key = get_key()
    if key:
        with open(file_path, 'rb') as f:
            data = f.read()
        
        # Pomiar czasu szyfrowania
        start_time = time.time()
        encrypted_data = encrypt_stream(data, key)
        end_time = time.time()
        elapsed_time = end_time - start_time

        with open(output_path, 'wb') as f:
            f.write(encrypted_data)
        
        print(f"Szyfrowanie pliku '{file_path}' zajęło: {elapsed_time:.2f} sekund.")
        messagebox.showinfo("Sukces", "Plik został zaszyfrowany i zapisany.")

# Funkcja obsługująca deszyfrowanie pliku.
def decrypt_file_action():
    file_path = filedialog.askopenfilename(title="Wybierz plik do odszyfrowania")
    if not file_path:
        return
    output_path = filedialog.asksaveasfilename(title="Zapisz odszyfrowany plik jako")
    if not output_path:
        return
    key = get_key()
    if key:
        with open(file_path, 'rb') as f:
            encrypted_data = f.read()
        
        # Pomiar czasu deszyfrowania
        start_time = time.time()
        decrypted_data = decrypt_stream(encrypted_data, key)
        end_time = time.time()
        elapsed_time = end_time - start_time

        with open(output_path, 'wb') as f:
            f.write(decrypted_data)
        
        print(f"Deszyfrowanie pliku '{file_path}' zajęło: {elapsed_time:.2f} sekund.")
        messagebox.showinfo("Sukces", "Plik został odszyfrowany i zapisany.")

# Konfiguracja graficznego interfejsu użytkownika.
app = tk.Tk()
app.title("DES Strumieniowy")

# Główny kontener
main_frame = tk.Frame(app, padx=10, pady=10)
main_frame.pack(fill="both", expand=True, padx=10, pady=10)

# Sekcja klucza
key_frame = tk.LabelFrame(main_frame, text="Klucz DES", padx=10, pady=10)
key_frame.pack(fill="x", pady=10)

key_label = tk.Label(key_frame, text="Klucz DES (8 znaków):")
key_label.pack(anchor="center", pady=5)

key_entry = tk.Entry(key_frame, show="*", width=50)
key_entry.pack(fill="x", pady=5)

generate_key_button = tk.Button(key_frame, text="Wygeneruj klucz", command=generate_key)
generate_key_button.pack(fill="x", pady=5)

copy_key_button = tk.Button(key_frame, text="Kopiuj klucz", command=copy_key)
copy_key_button.pack(fill="x", pady=5)

# Sekcja plików
file_frame = tk.LabelFrame(main_frame, text="Operacje na plikach", padx=10, pady=10)
file_frame.pack(fill="x", pady=10)

encrypt_button = tk.Button(file_frame, text="Zaszyfruj plik", command=encrypt_file_action)
encrypt_button.pack(fill="x", pady=5)

decrypt_button = tk.Button(file_frame, text="Odszyfruj plik", command=decrypt_file_action)
decrypt_button.pack(fill="x", pady=5)

# Rozmiar okna
app.geometry("520x400")
app.mainloop()
