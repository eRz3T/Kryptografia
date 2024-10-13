# gui.py

import tkinter as tk
from tkinter import filedialog, messagebox
import encrypt
import decrypt

def browse_file(entry):
    """Pozwala użytkownikowi wybrać plik."""
    filename = filedialog.askopenfilename(title="Wybierz plik tekstowy", filetypes=[("Pliki tekstowe", "*.txt")])
    entry.delete(0, tk.END)
    entry.insert(0, filename)

def encrypt_file():
    """Funkcja do obsługi szyfrowania pliku."""
    input_file = input_file_entry.get()
    output_file = output_file_entry.get()
    key = key_entry.get()
    
    if input_file and output_file and key:
        encrypt.encrypt_text_file(input_file, output_file, key)
        messagebox.showinfo("Sukces", "Plik został zaszyfrowany!")
    else:
        messagebox.showerror("Błąd", "Uzupełnij wszystkie pola!")

def decrypt_file():
    """Funkcja do obsługi deszyfrowania pliku."""
    input_file = input_file_entry.get()
    output_file = output_file_entry.get()
    key = key_entry.get()
    
    if input_file and output_file and key:
        decrypt.decrypt_text_file(input_file, output_file, key)
        messagebox.showinfo("Sukces", "Plik został odszyfrowany!")
    else:
        messagebox.showerror("Błąd", "Uzupełnij wszystkie pola!")

# Tworzenie GUI
window = tk.Tk()
window.title("Szyfrowanie i deszyfrowanie plików")

# Pole wyboru pliku wejściowego
tk.Label(window, text="Plik wejściowy:").grid(row=0, column=0, padx=10, pady=10)
input_file_entry = tk.Entry(window, width=40)
input_file_entry.grid(row=0, column=1, padx=10, pady=10)
tk.Button(window, text="Wybierz", command=lambda: browse_file(input_file_entry)).grid(row=0, column=2, padx=10, pady=10)

# Pole wyboru pliku wyjściowego
tk.Label(window, text="Plik wyjściowy:").grid(row=1, column=0, padx=10, pady=10)
output_file_entry = tk.Entry(window, width=40)
output_file_entry.grid(row=1, column=1, padx=10, pady=10)
tk.Button(window, text="Wybierz", command=lambda: browse_file(output_file_entry)).grid(row=1, column=2, padx=10, pady=10)

# Pole na klucz szyfrowania
tk.Label(window, text="Klucz szyfrowania:").grid(row=2, column=0, padx=10, pady=10)
key_entry = tk.Entry(window, width=40)
key_entry.grid(row=2, column=1, padx=10, pady=10)

# Przyciski do szyfrowania i deszyfrowania
tk.Button(window, text="Szyfruj", command=encrypt_file).grid(row=3, column=0, padx=10, pady=10)
tk.Button(window, text="Deszyfruj", command=decrypt_file).grid(row=3, column=1, padx=10, pady=10)

window.mainloop()
