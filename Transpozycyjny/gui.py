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
    try:
        key = int(key_entry.get())
    except ValueError:
        messagebox.showerror("Błąd", "Klucz musi być liczbą całkowitą!")
        return

    if input_file and output_file and key:
        encrypt.encrypt_text_file(input_file, output_file, key)
        messagebox.showinfo("Sukces", "Plik został zaszyfrowany!")
    else:
        messagebox.showerror("Błąd", "Uzupełnij wszystkie pola!")

def decrypt_file():
    """Funkcja do obsługi deszyfrowania pliku."""
    input_file = input_file_entry.get()
    output_file = output_file_entry.get()
    try:
        key = int(key_entry.get())
    except ValueError:
        messagebox.showerror("Błąd", "Klucz musi być liczbą całkowitą!")
        return

    if input_file and output_file and key:
        decrypt.decrypt_text_file(input_file, output_file, key)
        messagebox.showinfo("Sukces", "Plik został odszyfrowany!")
    else:
        messagebox.showerror("Błąd", "Uzupełnij wszystkie pola!")

def encrypt_text_action():
    """Szyfruje tekst z pola tekstowego i zapisuje wynik w wybranym pliku."""
    text = text_entry.get("1.0", tk.END).strip()
    try:
        key = int(key_entry.get())
    except ValueError:
        messagebox.showerror("Błąd", "Klucz musi być liczbą całkowitą!")
        return

    if not text:
        messagebox.showerror("Błąd", "Pole tekstu do zaszyfrowania nie może być puste!")
        return

    output_file = filedialog.asksaveasfilename(title="Zapisz zaszyfrowany tekst jako", defaultextension=".txt")
    if output_file:
        encrypted_text = encrypt.encrypt_message(text, key)
        with open(output_file, 'w') as file:
            file.write(encrypted_text)
        messagebox.showinfo("Sukces", "Tekst został zaszyfrowany i zapisany w pliku!")

# Tworzenie GUI
window = tk.Tk()
window.title("Szyfrowanie i deszyfrowanie plików (Szyfr Transpozycyjny)")

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
tk.Label(window, text="Klucz szyfrowania (ilość kolumn):").grid(row=2, column=0, padx=10, pady=10)
key_entry = tk.Entry(window, width=40)
key_entry.grid(row=2, column=1, padx=10, pady=10)

# Pole tekstowe do wprowadzenia tekstu do zaszyfrowania
tk.Label(window, text="Tekst do szyfrowania:").grid(row=3, column=0, columnspan=3, padx=10, pady=10)
text_entry = tk.Text(window, height=10, width=50)
text_entry.grid(row=4, column=0, columnspan=3, padx=10, pady=10)

# Przyciski do szyfrowania i deszyfrowania plików
tk.Button(window, text="Szyfruj plik", command=encrypt_file).grid(row=5, column=0, padx=10, pady=10)
tk.Button(window, text="Deszyfruj plik", command=decrypt_file).grid(row=5, column=1, padx=10, pady=10)

# Przycisk do szyfrowania tekstu
tk.Button(window, text="Szyfruj tekst do pliku", command=encrypt_text_action).grid(row=6, column=0, padx=10, pady=10)

window.mainloop()
