import tkinter as tk
from tkinter import filedialog, messagebox
from encrypt import generate_rsa_keys, encrypt_text_rsa, encrypt_file_hybrid
from decrypt import decrypt_file_hybrid, decrypt_file_rsa

# Funkcja generująca klucze RSA i zapisująca je do plików.
def generate_keys():
    global private_key, public_key
    private_key, public_key = generate_rsa_keys()  # Generowanie kluczy.

    # Zapis kluczy do plików.
    with open("private_key.pem", "wb") as priv_file:
        priv_file.write(private_key)
    with open("public_key.pem", "wb") as pub_file:
        pub_file.write(public_key)

    messagebox.showinfo("Sukces", "Klucze RSA zostały wygenerowane i zapisane!")

# Funkcja szyfrująca tekst wpisany w GUI i zapisująca go do pliku.
def encrypt_text_to_file():
    if not public_key:
        messagebox.showerror("Błąd", "Najpierw wygeneruj klucze RSA!")
        return
    text = text_entry.get("1.0", tk.END).strip()
    if not text:
        messagebox.showerror("Błąd", "Pole tekstowe jest puste!")
        return
    encrypted_text = encrypt_text_rsa(text, public_key)
    output_path = filedialog.asksaveasfilename(
        title="Zapisz zaszyfrowany tekst jako", defaultextension=".txt", filetypes=[("Text files", "*.txt"), ("All files", "*.*")]
    )
    if not output_path:
        return
    with open(output_path, 'wb') as f:
        f.write(encrypted_text)
    messagebox.showinfo("Sukces", "Tekst został zaszyfrowany i zapisany do pliku.")

# Funkcja szyfrująca plik.
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
        encrypt_file_hybrid(file_path, output_path, public_key)
        messagebox.showinfo("Sukces", "Plik został zaszyfrowany i zapisany.")
    except Exception as e:
        messagebox.showerror("Błąd", f"Nie udało się zaszyfrować pliku: {e}")

# Funkcja deszyfrująca plik.
def decrypt_file_action():
    if not private_key:
        messagebox.showerror("Błąd", "Najpierw wygeneruj klucze RSA!")
        return
    file_path = filedialog.askopenfilename(title="Wybierz plik do odszyfrowania")
    if not file_path:
        return
    output_path = filedialog.asksaveasfilename(title="Zapisz odszyfrowany plik jako")
    if not output_path:
        return

    method = messagebox.askyesno("Wybór metody odszyfrowania", "Czy plik został zaszyfrowany hybrydowo (RSA + AES)?")
    try:
        if method:
            decrypt_file_hybrid(file_path, output_path, private_key)
        else:
            decrypt_file_rsa(file_path, output_path, private_key)
        messagebox.showinfo("Sukces", "Plik został odszyfrowany i zapisany.")
    except Exception as e:
        messagebox.showerror("Błąd", f"Nie udało się odszyfrować pliku: {e}")

# Konfiguracja GUI.
private_key = None
public_key = None

app = tk.Tk()
app.title("RSA Encrypt/Decrypt")

generate_button = tk.Button(app, text="Generuj klucze RSA", command=generate_keys)
generate_button.pack(pady=5)

text_label = tk.Label(app, text="Tekst do zaszyfrowania i zapisania do pliku:")
text_label.pack()
text_entry = tk.Text(app, height=10, width=40)
text_entry.pack()

encrypt_text_button = tk.Button(app, text="Zaszyfruj tekst i zapisz do pliku", command=encrypt_text_to_file)
encrypt_text_button.pack(pady=5)

encrypt_file_button = tk.Button(app, text="Zaszyfruj plik", command=encrypt_file_action)
encrypt_file_button.pack(pady=5)

decrypt_file_button = tk.Button(app, text="Odszyfruj plik", command=decrypt_file_action)
decrypt_file_button.pack(pady=5)

app.geometry("400x500")
app.mainloop()
