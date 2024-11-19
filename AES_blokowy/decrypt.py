from Crypto.Cipher import AES
from Crypto.Util.Padding import unpad
import os

# Funkcja odszyfrowująca plik przy użyciu algorytmu AES.
def decrypt_file(input_path, output_path, key):
    try:
        # Odczytanie zawartości pliku zaszyfrowanego w trybie binarnym.
        with open(input_path, 'rb') as f:
            nonce = f.read(16)  # Odczytanie wektora inicjalizującego (nonce).
            tag = f.read(16)    # Odczytanie znacznika uwierzytelnienia (tag).
            ciphertext = f.read()  # Odczytanie zaszyfrowanych danych.

        # Utworzenie instancji szyfru AES w trybie EAX z odczytanym nonce.
        cipher = AES.new(key, AES.MODE_EAX, nonce=nonce)
        # Odszyfrowanie i weryfikacja integralności danych.
        plaintext = unpad(cipher.decrypt_and_verify(ciphertext, tag), AES.block_size)

        # Zapisanie odszyfrowanej zawartości do pliku wyjściowego.
        with open(output_path, 'wb') as f:
            f.write(plaintext)
    # Obsługa błędów.
    except Exception as e:
        print(f"Błąd podczas deszyfrowania: {e}")
