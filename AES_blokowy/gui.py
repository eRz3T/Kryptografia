import tkinter as tk
from tkinter import filedialog, messagebox
from AES_blokowy.encrypt import encrypt_file
from AES_blokowy.decrypt import decrypt_file
import os

# Funkcja do pobierania klucza AES z pola tekstowego GUI.
def get_key():
    key = key_entry.get().encode()  # Pobranie tekstu i zakodowanie jako bajty.
    if len(key) != 32:
        # Wyświetlenie błędu, jeśli klucz nie spełnia wymagań.
        messagebox.showerror("Error", "Klucz AES musi mieć 32 znaki (256 bitów)!")
        return None
    return key

# Funkcja obsługująca szyfrowanie pliku.
def encrypt_file_action(input_path=None, output_path=None, key=None):
    if not input_path or not output_path or not key:
        # Obsługa interakcji z GUI (wybór pliku).
        input_path = filedialog.askopenfilename(title="Wybierz plik do zaszyfrowania")
        if not input_path:
            return
        output_path = filedialog.asksaveasfilename(title="Zapisz zaszyfrowany plik jako")
        if not output_path:
            return
        key = get_key()
        if not key:
            return

    encrypt_file(input_path, output_path, key)
    # Informowanie użytkownika o sukcesie operacji.
    messagebox.showinfo("Sukces", "Plik został zaszyfrowany i zapisany.")

# Funkcja obsługująca deszyfrowanie pliku.
def decrypt_file_action(input_path=None, output_path=None, key=None):
    if not input_path or not output_path or not key:
        # Obsługa interakcji z GUI (wybór pliku).
        input_path = filedialog.askopenfilename(title="Wybierz plik do odszyfrowania")
        if not input_path:
            return
        output_path = filedialog.asksaveasfilename(title="Zapisz odszyfrowany plik jako")
        if not output_path:
            return
        key = get_key()
        if not key:
            return

    decrypt_file(input_path, output_path, key)
    # Informowanie użytkownika o sukcesie operacji.
    messagebox.showinfo("Sukces", "Plik został odszyfrowany i zapisany.")

# Funkcja obsługująca szyfrowanie tekstu i zapisanie go do pliku.
def encrypt_text_action():
    text = text_entry.get("1.0", tk.END).encode()  # Pobranie tekstu z pola tekstowego.
    if not text.strip():
        messagebox.showerror("Error", "Tekst do zaszyfrowania nie może być pusty!")
        return
    output_path = filedialog.asksaveasfilename(title="Zapisz zaszyfrowany tekst jako")
    if not output_path:
        return
    key = get_key()
    if key:
        # Tymczasowy zapis tekstu do pliku przed szyfrowaniem.
        with open("temp_text.txt", "wb") as temp_file:
            temp_file.write(text)
        encrypt_file("temp_text.txt", output_path, key)
        os.remove("temp_text.txt")  # Usunięcie pliku tymczasowego.
        messagebox.showinfo("Sukces", "Tekst został zaszyfrowany i zapisany w pliku.")

# Konfiguracja GUI.
app = tk.Tk()
app.title("AES Encrypt/Decrypt")

key_label = tk.Label(app, text="Klucz AES (32 znaki):")
key_label.pack()

key_entry = tk.Entry(app, show="*")
key_entry.pack()

text_label = tk.Label(app, text="Tekst do zaszyfrowania:")
text_label.pack()

text_entry = tk.Text(app, height=10, width=40)
text_entry.pack()

encrypt_button = tk.Button(app, text="Zaszyfruj plik", command=encrypt_file_action)
encrypt_button.pack()

decrypt_button = tk.Button(app, text="Odszyfruj plik", command=decrypt_file_action)
decrypt_button.pack()

encrypt_text_button = tk.Button(app, text="Zaszyfruj tekst do pliku", command=encrypt_text_action)
encrypt_text_button.pack()

app.geometry("400x400")
app.mainloop()

