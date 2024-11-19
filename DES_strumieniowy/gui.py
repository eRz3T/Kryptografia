import tkinter as tk
from tkinter import filedialog, messagebox
from encrypt import encrypt_stream
from decrypt import decrypt_stream

# Funkcja do pobierania klucza DES z pola tekstowego GUI.
def get_key():
    # Pobranie klucza z pola tekstowego i zakodowanie go jako bajty.
    key = key_entry.get().encode()
    
    # Sprawdzenie, czy klucz ma dokładnie 8 znaków (64 bity).
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
        # Odczytanie zawartości pliku w trybie binarnym.
        with open(file_path, 'rb') as f:
            data = f.read()
        
        # Szyfrowanie danych za pomocą funkcji `encrypt_stream`.
        encrypted_data = encrypt_stream(data, key)
        
        # Zapisanie zaszyfrowanych danych do pliku wyjściowego.
        with open(output_path, 'wb') as f:
            f.write(encrypted_data)
        
        # Powiadomienie użytkownika o sukcesie operacji.
        messagebox.showinfo("Sukces", "Plik został zaszyfrowany i zapisany.")

# Funkcja obsługująca deszyfrowanie pliku.
def decrypt_file_action():
    # Wyświetlenie okna dialogowego do wyboru pliku zaszyfrowanego.
    file_path = filedialog.askopenfilename(title="Wybierz plik do odszyfrowania")
    if not file_path:
        return
    
    # Wyświetlenie okna dialogowego do wyboru lokalizacji pliku wyjściowego.
    output_path = filedialog.asksaveasfilename(title="Zapisz odszyfrowany plik jako")
    if not output_path:
        return
    
    # Pobranie klucza DES od użytkownika.
    key = get_key()
    if key:
        # Odczytanie zawartości pliku zaszyfrowanego w trybie binarnym.
        with open(file_path, 'rb') as f:
            encrypted_data = f.read()
        
        # Deszyfrowanie danych za pomocą funkcji `decrypt_stream`.
        decrypted_data = decrypt_stream(encrypted_data, key)
        
        # Zapisanie odszyfrowanych danych do pliku wyjściowego.
        with open(output_path, 'wb') as f:
            f.write(decrypted_data)
        
        # Powiadomienie użytkownika o sukcesie operacji.
        messagebox.showinfo("Sukces", "Plik został odszyfrowany i zapisany.")

# Konfiguracja graficznego interfejsu użytkownika.
app = tk.Tk()
app.title("DES Encrypt/Decrypt Stream")

# Pole do wprowadzania klucza DES.
key_label = tk.Label(app, text="Klucz DES (8 znaków):")
key_label.pack()

key_entry = tk.Entry(app, show="*")  # Pole ukrywające znaki wpisywane jako klucz.
key_entry.pack()

# Przycisk do szyfrowania plików.
encrypt_button = tk.Button(app, text="Zaszyfruj plik", command=encrypt_file_action)
encrypt_button.pack()

# Przycisk do deszyfrowania plików.
decrypt_button = tk.Button(app, text="Odszyfruj plik", command=decrypt_file_action)
decrypt_button.pack()

# Ustawienia rozmiaru okna GUI.
app.geometry("400x200")  # Rozmiar okna (szerokość x wysokość).
app.mainloop()  # Uruchomienie pętli głównej interfejsu.
