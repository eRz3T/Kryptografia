import tkinter as tk
from tkinter import filedialog, messagebox
from encrypt import generate_hamak_keys, encrypt_text_hamak, encrypt_file_hamak
from decrypt import decrypt_text_hamak, decrypt_file_hamak
import pyperclip

key = None

# Funkcja generująca klucz

def generate_key():
    global key
    key = generate_hamak_keys()
    key_entry.delete("1.0", tk.END)
    key_entry.insert("1.0", str(key))
    messagebox.showinfo("Sukces", "Klucz Hamak został wygenerowany!")

# Funkcja kopiowania klucza

def copy_key():
    if key:
        pyperclip.copy(str(key))
        messagebox.showinfo("Sukces", "Klucz został skopiowany do schowka.")
    else:
        messagebox.showerror("Błąd", "Brak klucza do skopiowania.")

# Funkcja szyfrująca tekst wpisany w GUI i zapisująca go do pliku

def encrypt_text_to_file():
    if not key:
        messagebox.showerror("Błąd", "Najpierw wygeneruj klucz Hamak!")
        return
    text = text_entry.get("1.0", tk.END).strip()
    if not text:
        messagebox.showerror("Błąd", "Pole tekstowe jest puste!")
        return
    try:
        encrypted_text = encrypt_text_hamak(text, key)
        output_path = filedialog.asksaveasfilename(
            title="Zapisz zaszyfrowany tekst jako", defaultextension=".txt", filetypes=[("Text files", "*.txt"), ("All files", "*.*")]
        )
        if not output_path:
            return
        with open(output_path, 'wb') as f:
            f.write(encrypted_text)
        messagebox.showinfo("Sukces", "Tekst został zaszyfrowany i zapisany do pliku.")
    except Exception as e:
        messagebox.showerror("Błąd", f"Nie udało się zaszyfrować tekstu: {e}")

# Funkcja szyfrująca plik

def encrypt_file_action():
    if not key:
        messagebox.showerror("Błąd", "Najpierw wygeneruj klucz Hamak!")
        return
    file_path = filedialog.askopenfilename(title="Wybierz plik do zaszyfrowania")
    if not file_path:
        return
    output_path = filedialog.asksaveasfilename(title="Zapisz zaszyfrowany plik jako")
    if not output_path:
        return

    try:
        encrypt_file_hamak(file_path, output_path, key)
        messagebox.showinfo("Sukces", "Plik został zaszyfrowany i zapisany.")
    except Exception as e:
        messagebox.showerror("Błąd", f"Nie udało się zaszyfrować pliku: {e}")

# Funkcja deszyfrująca plik

def decrypt_file_action():
    if not key:
        messagebox.showerror("Błąd", "Najpierw wygeneruj klucz Hamak!")
        return
    input_path = filedialog.askopenfilename(title="Wybierz plik do odszyfrowania")
    if not input_path:
        return
    output_path = filedialog.asksaveasfilename(title="Zapisz odszyfrowany plik jako")
    if not output_path:
        return
    try:
        decrypt_file_hamak(input_path, output_path, key)
        messagebox.showinfo("Sukces", "Plik został odszyfrowany i zapisany.")
    except Exception as e:
        messagebox.showerror("Błąd", f"Nie udało się odszyfrować pliku: {e}")

# GUI

app = tk.Tk()
app.title("Hamac")
app.geometry("520x580")

key_frame = tk.LabelFrame(app, text="Klucz Hamak")
key_frame.pack(fill="x", padx=10, pady=10)

key_label = tk.Label(key_frame, text="Klucz Hamak (liczba całkowita):")
key_label.pack(anchor="center", pady=5)


key_entry = tk.Text(key_frame, height=1)
key_entry.pack(fill="x", padx=10, pady=5)

tk.Button(key_frame, text="Generuj klucz", command=generate_key).pack(fill="x", padx=10, pady=5)

tk.Button(key_frame, text="Kopiuj klucz", command=copy_key).pack(fill="x", padx=10, pady=5)

text_frame = tk.LabelFrame(app, text="Szyfrowanie tekstu")
text_frame.pack(fill="x", padx=10, pady=10)

tk.Label(text_frame, text="Tekst do zaszyfrowania:").pack(anchor="w", padx=10)
text_entry = tk.Text(text_frame, height=10)
text_entry.pack(fill="x", padx=10, pady=5)

tk.Button(text_frame, text="Zaszyfruj tekst i zapisz do pliku", command=encrypt_text_to_file).pack(fill="x", padx=10, pady=5)

file_frame = tk.LabelFrame(app, text="Operacje na plikach")
file_frame.pack(fill="x", padx=10, pady=10)

tk.Button(file_frame, text="Zaszyfruj plik", command=encrypt_file_action).pack(fill="x", padx=10, pady=5)
tk.Button(file_frame, text="Odszyfruj plik", command=decrypt_file_action).pack(fill="x", padx=10, pady=5)

app.mainloop()
