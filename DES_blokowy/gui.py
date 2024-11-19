import tkinter as tk
from tkinter import filedialog, messagebox
from encrypt import encrypt_file
from decrypt import decrypt_file
import os

# Funkcja do pobierania klucza DES z pola tekstowego GUI.
def get_key():
    # Pobranie klucza i zakodowanie go jako bajty.
    key = key_entry.get().encode()
    
    # Sprawdzenie, czy długość klucza wynosi dokładnie 8 bajtów (64 bity).
    if len(key) != 8:
        messagebox.showerror("Error", "Klucz DES musi mieć 8 znaków!")
        return None  # Zwracamy `None`, jeśli klucz jest nieprawidłowy.
    return key

# Funkcja obsługująca szyfrowanie pliku.
def encrypt_file_action():
    # Wyświetlenie okna dialogowego do wyboru pliku wejściowego.
    file_path = filedialog.askopenfilename(title="Wybierz plik do zaszyfrowania")
    if not file_path:  # Jeśli użytkownik anulował wybór, kończymy funkcję.
        return
    
    # Wyświetlenie okna dialogowego do wyboru lokalizacji pliku wyjściowego.
    output_path = filedialog.asksaveasfilename(title="Zapisz zaszyfrowany plik jako")
    if not output_path:
        return
    
    # Pobranie klucza DES od użytkownika.
    key = get_key()
    if key:
        # Wywołanie funkcji szyfrującej.
        encrypt_file(file_path, output_path, key)
        
        # Powiadomienie użytkownika o sukcesie operacji.
        messagebox.showinfo("Sukces", "Plik został zaszyfrowany i zapisany.")

# Funkcja obsługująca deszyfrowanie pliku.
def decrypt_file_action():
    # Wyświetlenie okna dialogowego do wyboru pliku zaszyfrowanego.
    file_path = filedialog.askopenfilename(title="Wybierz plik do odszyfrowania")
    if not file_path:
        return
    
    # Wyświetlenie okna dialogowego do wyboru lokalizacji pliku odszyfrowanego.
    output_path = filedialog.asksaveasfilename(title="Zapisz odszyfrowany plik jako")
    if not output_path:
        return
    
    # Pobranie klucza DES od użytkownika.
    key = get_key()
    if key:
        # Wywołanie funkcji deszyfrującej.
        decrypt_file(file_path, output_path, key)
        
        # Powiadomienie użytkownika o sukcesie operacji.
        messagebox.showinfo("Sukces", "Plik został odszyfrowany i zapisany.")

# Funkcja obsługująca szyfrowanie tekstu wpisanego w GUI.
def encrypt_text_action():
    # Pobranie tekstu z pola tekstowego GUI.
    text = text_entry.get("1.0", tk.END).encode()
    
    # Sprawdzenie, czy tekst nie jest pusty.
    if not text.strip():
        messagebox.showerror("Error", "Tekst do zaszyfrowania nie może być pusty!")
        return
    
    # Wyświetlenie okna dialogowego do wyboru lokalizacji pliku wyjściowego.
    output_path = filedialog.asksaveasfilename(title="Zapisz zaszyfrowany tekst jako")
    if not output_path:
        return
    
    # Pobranie klucza DES od użytkownika.
    key = get_key()
    if key:
        # Tymczasowy zapis tekstu do pliku, aby można go było zaszyfrować.
        with open("temp_text.txt", "wb") as temp_file:
            temp_file.write(text)
        
        # Szyfrowanie pliku tymczasowego.
        encrypt_file("temp_text.txt", output_path, key)
        
        # Usunięcie pliku tymczasowego.
        os.remove("temp_text.txt")
        
        # Powiadomienie użytkownika o sukcesie operacji.
        messagebox.showinfo("Sukces", "Tekst został zaszyfrowany i zapisany w pliku.")

# Konfiguracja graficznego interfejsu użytkownika.
app = tk.Tk()
app.title("DES Encrypt/Decrypt")

# Pole do wprowadzania klucza DES.
key_label = tk.Label(app, text="Klucz DES (8 znaków):")
key_label.pack()

key_entry = tk.Entry(app, show="*")  # Pole ukrywające znaki wpisywane jako klucz.
key_entry.pack()

# Pole do wprowadzania tekstu do zaszyfrowania.
text_label = tk.Label(app, text="Tekst do zaszyfrowania:")
text_label.pack()

text_entry = tk.Text(app, height=10, width=40)
text_entry.pack()

# Przycisk do szyfrowania plików.
encrypt_button = tk.Button(app, text="Zaszyfruj plik", command=encrypt_file_action)
encrypt_button.pack()

# Przycisk do deszyfrowania plików.
decrypt_button = tk.Button(app, text="Odszyfruj plik", command=decrypt_file_action)
decrypt_button.pack()

# Przycisk do szyfrowania tekstu wpisanego w GUI.
encrypt_text_button = tk.Button(app, text="Zaszyfruj tekst do pliku", command=encrypt_text_action)
encrypt_text_button.pack()

# Ustawienie rozmiaru okna GUI.
app.geometry("400x400")
app.mainloop()
