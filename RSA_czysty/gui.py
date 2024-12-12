import tkinter as tk
from tkinter import filedialog, messagebox
from encrypt import generate_rsa_keys, encrypt_file_rsa, encrypt_text_rsa
from decrypt import decrypt_file_rsa, decrypt_text_rsa
import pyperclip

private_key = None
public_key = None

# Funkcja generująca klucze
def generate_keys():
    global private_key, public_key
    private_key, public_key = generate_rsa_keys()
    private_key_entry.delete("1.0", tk.END)
    private_key_entry.insert("1.0", private_key.decode())
    public_key_entry.delete("1.0", tk.END)
    public_key_entry.insert("1.0", public_key.decode())
    messagebox.showinfo("Sukces", "Klucze RSA zostały wygenerowane!")

# Funkcja kopiowania kluczy
def copy_key(key_type):
    key = private_key if key_type == "private" else public_key
    if key:
        pyperclip.copy(key.decode())
        messagebox.showinfo("Sukces", f"{key_type.capitalize()} klucz został skopiowany do schowka.")
    else:
        messagebox.showerror("Błąd", f"Brak {key_type.capitalize()} klucza do skopiowania.")

# Funkcja szyfrująca plik
def encrypt_file_action():
    if not public_key:
        messagebox.showerror("Błąd", "Najpierw wygeneruj klucze RSA!")
        return
    file_path = filedialog.askopenfilename(title="Wybierz plik do zaszyfrowania")
    if not file_path:
        return
    output_path = filedialog.asksaveasfilename(title="Zapisz zaszyfrowany plik jako")
    if not output_path:
        return

    try:
        encrypt_file_rsa(file_path, output_path, public_key)
        messagebox.showinfo("Sukces", "Plik został zaszyfrowany i zapisany.")
    except Exception as e:
        messagebox.showerror("Błąd", f"Nie udało się zaszyfrować pliku: {e}")

# Funkcja deszyfrująca plik
def decrypt_file_action():
    if not private_key:
        messagebox.showerror("Błąd", "Najpierw wygeneruj klucze RSA!")
        return
    input_path = filedialog.askopenfilename(title="Wybierz plik do odszyfrowania")
    if not input_path:
        return
    output_path = filedialog.asksaveasfilename(title="Zapisz odszyfrowany plik jako")
    if not output_path:
        return
    decrypt_file_rsa(input_path, output_path, private_key)
    messagebox.showinfo("Sukces", "Plik został odszyfrowany i zapisany.")

def encrypt_text_to_file():
    if not public_key:
        messagebox.showerror("Błąd", "Najpierw wygeneruj klucze RSA!")
        return
    text = text_entry.get("1.0", tk.END).strip()
    if not text:
        messagebox.showerror("Błąd", "Pole tekstowe jest puste!")
        return
    try:
        encrypted_text = encrypt_text_rsa(text, public_key)
        output_path = filedialog.asksaveasfilename(
            title="Zapisz zaszyfrowany tekst jako", defaultextension=".txt", filetypes=[("Text files", "*.txt"), ("All files", "*.*")]
        )
        if not output_path:
            return
        with open(output_path, "wb") as f:
            f.write(encrypted_text)
        messagebox.showinfo("Sukces", "Tekst został zaszyfrowany i zapisany do pliku.")
    except Exception as e:
        messagebox.showerror("Błąd", f"Nie udało się zaszyfrować tekstu: {e}")


# GUI
app = tk.Tk()
app.title("RSA")
app.geometry("520x780")

key_frame = tk.LabelFrame(app, text="Klucze RSA")
key_frame.pack(fill="x", padx=10, pady=10)

tk.Button(key_frame, text="Generuj klucze", command=generate_keys).pack(fill="x", padx=10, pady=5)

tk.Label(key_frame, text="Klucz prywatny:").pack(anchor="w", padx=10)
private_key_entry = tk.Text(key_frame, height=5)
private_key_entry.pack(fill="x", padx=10, pady=5)
tk.Button(key_frame, text="Kopiuj klucz prywatny", command=lambda: copy_key("private")).pack(fill="x", padx=10, pady=5)

tk.Label(key_frame, text="Klucz publiczny:").pack(anchor="w", padx=10)
public_key_entry = tk.Text(key_frame, height=5)
public_key_entry.pack(fill="x", padx=10, pady=5)
tk.Button(key_frame, text="Kopiuj klucz publiczny", command=lambda: copy_key("public")).pack(fill="x", padx=10, pady=5)

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
