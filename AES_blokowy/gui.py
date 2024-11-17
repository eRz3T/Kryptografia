import tkinter as tk
from tkinter import filedialog, messagebox
from encrypt import encrypt_file
from decrypt import decrypt_file
import os

def get_key():
    key = key_entry.get().encode()
    if len(key) != 32:
        messagebox.showerror("Error", "Klucz AES musi mieć 32 znaki (256 bitów)!")
        return None
    return key

def encrypt_file_action():
    file_path = filedialog.askopenfilename(title="Wybierz plik do zaszyfrowania")
    if not file_path:
        return
    output_path = filedialog.asksaveasfilename(title="Zapisz zaszyfrowany plik jako")
    if not output_path:
        return
    key = get_key()
    if key:
        encrypt_file(file_path, output_path, key)
        messagebox.showinfo("Sukces", "Plik został zaszyfrowany i zapisany.")

def decrypt_file_action():
    file_path = filedialog.askopenfilename(title="Wybierz plik do odszyfrowania")
    if not file_path:
        return
    output_path = filedialog.asksaveasfilename(title="Zapisz odszyfrowany plik jako")
    if not output_path:
        return
    key = get_key()
    if key:
        decrypt_file(file_path, output_path, key)
        messagebox.showinfo("Sukces", "Plik został odszyfrowany i zapisany.")

def encrypt_text_action():
    text = text_entry.get("1.0", tk.END).encode()
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
        encrypt_file("temp_text.txt", output_path, key)
        os.remove("temp_text.txt")
        messagebox.showinfo("Sukces", "Tekst został zaszyfrowany i zapisany w pliku.")

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
