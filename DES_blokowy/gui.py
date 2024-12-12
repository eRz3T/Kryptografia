import tkinter as tk
from tkinter import filedialog, messagebox
from encrypt import encrypt_file
from decrypt import decrypt_file
import time  # Dodano moduł do pomiaru czasu
import psutil  # Dodano moduł do pomiaru pamięci RAM
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
        
        # Pomiar czasu i pamięci RAM podczas szyfrowania
        process = psutil.Process()
        start_time = time.time()
        start_memory = process.memory_info().rss  # Pamięć przed operacją

        encrypt_file(file_path, output_path, key)

        end_time = time.time()
        end_memory = process.memory_info().rss  # Pamięć po operacji
        elapsed_time = end_time - start_time
        memory_used = (end_memory - start_memory) / (1024 * 1024)  # Konwersja na MB

        print(f"Szyfrowanie pliku '{file_path}' zajęło: {elapsed_time:.2f} sekund.")
        print(f"Zużycie pamięci RAM: {memory_used:.2f} MB.")
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
        
        # Pomiar czasu i pamięci RAM podczas deszyfrowania
        process = psutil.Process()
        start_time = time.time()
        start_memory = process.memory_info().rss  # Pamięć przed operacją

        decrypt_file(file_path, output_path, key)

        end_time = time.time()
        end_memory = process.memory_info().rss  # Pamięć po operacji
        elapsed_time = end_time - start_time
        memory_used = (end_memory - start_memory) / (1024 * 1024)  # Konwersja na MB

        print(f"Deszyfrowanie pliku '{file_path}' zajęło: {elapsed_time:.2f} sekund.")
        print(f"Zużycie pamięci RAM: {memory_used:.2f} MB.")
        messagebox.showinfo("Sukces", "Plik został odszyfrowany i zapisany.")

# Funkcja obsługująca szyfrowanie tekstu wpisanego w GUI.
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
        with open("temp_text.txt", "wb") as temp_file:
            temp_file.write(text)
        
        # Pomiar czasu i pamięci RAM podczas szyfrowania
        process = psutil.Process()
        start_time = time.time()
        start_memory = process.memory_info().rss  # Pamięć przed operacją

        encrypt_file("temp_text.txt", output_path, key)

        end_time = time.time()
        end_memory = process.memory_info().rss  # Pamięć po operacji
        elapsed_time = end_time - start_time
        memory_used = (end_memory - start_memory) / (1024 * 1024)  # Konwersja na MB

        os.remove("temp_text.txt")
        print(f"Szyfrowanie tekstu zajęło: {elapsed_time:.2f} sekund.")
        print(f"Zużycie pamięci RAM: {memory_used:.2f} MB.")
        messagebox.showinfo("Sukces", "Tekst został zaszyfrowany i zapisany w pliku.")

# Konfiguracja graficznego interfejsu użytkownika.
app = tk.Tk()
app.title("DES Blokowy")

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

# Sekcja tekstu
text_frame = tk.LabelFrame(main_frame, text="Operacje na tekście", padx=10, pady=10)
text_frame.pack(fill="x", pady=10)

text_label = tk.Label(text_frame, text="Tekst do zaszyfrowania:")
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
app.geometry("520x680")
app.mainloop()