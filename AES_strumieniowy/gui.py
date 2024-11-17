import tkinter as tk
from tkinter import filedialog, messagebox
from encrypt import encrypt_stream
from decrypt import decrypt_stream

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
        with open(file_path, 'rb') as f:
            data = f.read()
        encrypted_data = encrypt_stream(data, key)
        with open(output_path, 'wb') as f:
            f.write(encrypted_data)
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
        with open(file_path, 'rb') as f:
            encrypted_data = f.read()
        decrypted_data = decrypt_stream(encrypted_data, key)
        with open(output_path, 'wb') as f:
            f.write(decrypted_data)
        messagebox.showinfo("Sukces", "Plik został odszyfrowany i zapisany.")

app = tk.Tk()
app.title("AES Encrypt/Decrypt Stream")

key_label = tk.Label(app, text="Klucz AES (32 znaki):")
key_label.pack()

key_entry = tk.Entry(app, show="*")
key_entry.pack()

encrypt_button = tk.Button(app, text="Zaszyfruj plik", command=encrypt_file_action)
encrypt_button.pack()

decrypt_button = tk.Button(app, text="Odszyfruj plik", command=decrypt_file_action)
decrypt_button.pack()

app.geometry("400x200")
app.mainloop()
