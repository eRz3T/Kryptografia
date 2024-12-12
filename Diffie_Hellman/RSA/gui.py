import tkinter as tk
from tkinter import filedialog, messagebox
from encrypt import generate_rsa_keys, encrypt_text_rsa, encrypt_file_hybrid
from decrypt import decrypt_file_hybrid, decrypt_text_rsa
import time  # Dodano moduł do pomiaru czasu
import psutil  # Dodano moduł do pomiaru pamięci RAM
import pyperclip

# Globalne klucze
private_key = None
public_key = None

# Funkcja generująca klucze RSA i zapisująca je do pól oraz plików.
def generate_keys():
    global private_key, public_key
    private_key, public_key = generate_rsa_keys()  # Generowanie kluczy.

    private_key_entry.delete("1.0", tk.END)
    private_key_entry.insert("1.0", private_key.decode())

    public_key_entry.delete("1.0", tk.END)
    public_key_entry.insert("1.0", public_key.decode())

    messagebox.showinfo("Sukces", "Klucze RSA zostały wygenerowane!")

# Funkcja kopiowania kluczy
def copy_key(key_type):
    if key_type == "private":
        key = private_key_entry.get("1.0", tk.END).strip()
    else:
        key = public_key_entry.get("1.0", tk.END).strip()
    if key:
        pyperclip.copy(key)
        messagebox.showinfo("Sukces", f"{key_type.capitalize()} klucz został skopiowany do schowka.")
    else:
        messagebox.showerror("Błąd", f"Brak {key_type.capitalize()} klucza do skopiowania.")

# Funkcja szyfrująca tekst wpisany w GUI i zapisująca go do pliku.
def encrypt_text_to_file():
    if not public_key:
        messagebox.showerror("Błąd", "Najpierw wygeneruj klucze RSA!")
        return
    text = text_entry.get("1.0", tk.END).strip()
    if not text:
        messagebox.showerror("Błąd", "Pole tekstowe jest puste!")
        return
    try:
        process = psutil.Process()
        start_time = time.time()  # Pomiar czasu rozpoczęcia
        start_memory = process.memory_info().rss  # Pamięć przed operacją

        encrypted_text = encrypt_text_rsa(text, public_key)

        end_time = time.time()  # Pomiar czasu zakończenia
        end_memory = process.memory_info().rss  # Pamięć po operacji

        elapsed_time = end_time - start_time
        memory_used = (end_memory - start_memory) / (1024 * 1024)  # Konwersja na MB

        output_path = filedialog.asksaveasfilename(
            title="Zapisz zaszyfrowany tekst jako", defaultextension=".txt", filetypes=[("Text files", "*.txt"), ("All files", "*.*")]
        )
        if not output_path:
            return
        with open(output_path, 'wb') as f:
            f.write(encrypted_text)

        print(f"Szyfrowanie tekstu zajęło: {elapsed_time:.2f} sekund.")
        print(f"Zużycie pamięci RAM: {memory_used:.2f} MB.")
        messagebox.showinfo("Sukces", "Tekst został zaszyfrowany i zapisany do pliku.")
    except Exception as e:
        messagebox.showerror("Błąd", f"Nie udało się zaszyfrować tekstu: {e}")

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
        process = psutil.Process()
        start_time = time.time()  # Pomiar czasu rozpoczęcia
        start_memory = process.memory_info().rss  # Pamięć przed operacją

        encrypt_file_hybrid(file_path, output_path, public_key)

        end_time = time.time()  # Pomiar czasu zakończenia
        end_memory = process.memory_info().rss  # Pamięć po operacji

        elapsed_time = end_time - start_time
        memory_used = (end_memory - start_memory) / (1024 * 1024)  # Konwersja na MB

        print(f"Szyfrowanie pliku '{file_path}' zajęło: {elapsed_time:.2f} sekund.")
        print(f"Zużycie pamięci RAM: {memory_used:.2f} MB.")
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
        process = psutil.Process()
        start_time = time.time()  # Pomiar czasu rozpoczęcia
        start_memory = process.memory_info().rss  # Pamięć przed operacją

        if method:
            decrypt_file_hybrid(file_path, output_path, private_key)
        else:
            with open(file_path, 'rb') as f:
                encrypted_text = f.read()
            decrypted_text = decrypt_text_rsa(encrypted_text, private_key)
            with open(output_path, 'w') as f:
                f.write(decrypted_text)

        end_time = time.time()  # Pomiar czasu zakończenia
        end_memory = process.memory_info().rss  # Pamięć po operacji

        elapsed_time = end_time - start_time
        memory_used = (end_memory - start_memory) / (1024 * 1024)  # Konwersja na MB

        print(f"Deszyfrowanie pliku '{file_path}' zajęło: {elapsed_time:.2f} sekund.")
        print(f"Zużycie pamięci RAM: {memory_used:.2f} MB.")
        messagebox.showinfo("Sukces", "Plik został odszyfrowany i zapisany.")
    except Exception as e:
        messagebox.showerror("Błąd", f"Nie udało się odszyfrować pliku: {e}")

# Konfiguracja GUI
app = tk.Tk()
app.title("RSA + AES")
app.geometry("520x880")

main_frame = tk.Frame(app, padx=10, pady=10)
main_frame.pack(fill="both", expand=True, padx=10, pady=10)

# Sekcja kluczy
key_frame = tk.LabelFrame(main_frame, text="Klucz RSA", padx=10, pady=10)
key_frame.pack(fill="x", pady=10)

key_generate_button = tk.Button(key_frame, text="Generuj klucze", command=generate_keys)
key_generate_button.pack(fill="x", pady=5)

private_key_label = tk.Label(key_frame, text="Klucz prywatny:")
private_key_label.pack(anchor="w", pady=5)
private_key_entry = tk.Text(key_frame, height=5)
private_key_entry.pack(fill="x", pady=5)
private_key_copy_button = tk.Button(key_frame, text="Kopiuj klucz prywatny", command=lambda: copy_key("private"))
private_key_copy_button.pack(fill="x", pady=5)

public_key_label = tk.Label(key_frame, text="Klucz publiczny:")
public_key_label.pack(anchor="w", pady=5)
public_key_entry = tk.Text(key_frame, height=5)
public_key_entry.pack(fill="x", pady=5)
public_key_copy_button = tk.Button(key_frame, text="Kopiuj klucz publiczny", command=lambda: copy_key("public"))
public_key_copy_button.pack(fill="x", pady=5)

# Sekcja szyfrowania tekstu
text_frame = tk.LabelFrame(main_frame, text="Szyfrowanie tekstu", padx=10, pady=10)
text_frame.pack(fill="x", pady=10)

text_label = tk.Label(text_frame, text="Tekst do zaszyfrowania:")
text_label.pack(anchor="w")
text_entry = tk.Text(text_frame, height=10)
text_entry.pack(fill="x", pady=5)

encrypt_text_button = tk.Button(text_frame, text="Zaszyfruj tekst i zapisz do pliku", command=encrypt_text_to_file)
encrypt_text_button.pack(fill="x", pady=5)

# Sekcja szyfrowania/deszyfrowania plików
file_frame = tk.LabelFrame(main_frame, text="Operacje na plikach", padx=10, pady=10)
file_frame.pack(fill="x", pady=10)

encrypt_file_button = tk.Button(file_frame, text="Zaszyfruj plik", command=encrypt_file_action)
encrypt_file_button.pack(fill="x", pady=5)

decrypt_file_button = tk.Button(file_frame, text="Odszyfruj plik", command=decrypt_file_action)
decrypt_file_button.pack(fill="x", pady=5)

app.mainloop()
