from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes
from Crypto.Util.Padding import pad
import os

# Funkcja szyfrująca plik przy użyciu algorytmu AES.
def encrypt_file(input_path, output_path, key):
    # Upewniamy się, że klucz ma dokładnie 32 bajty (256 bitów), jak wymagane przez AES.
    if len(key) != 32:
        raise ValueError("Klucz AES musi mieć dokładnie 32 bajty (256 bitów).")

    try:
        # Odczytanie zawartości pliku wejściowego w trybie binarnym.
        with open(input_path, 'rb') as f:
            plaintext = f.read()

        # Utworzenie instancji szyfru AES w trybie EAX (zapewnia poufność i integralność).
        cipher = AES.new(key, AES.MODE_EAX)
        nonce = cipher.nonce  # Wektor inicjalizujący (IV) generowany automatycznie.
        # Szyfrowanie i generowanie znacznika uwierzytelnienia (tag).
        ciphertext, tag = cipher.encrypt_and_digest(pad(plaintext, AES.block_size))

        # Zapisanie zaszyfrowanej zawartości do pliku wyjściowego.
        with open(output_path, 'wb') as f:
            f.write(nonce)  # Nonce (16 bajtów) na początku pliku.
            f.write(tag)    # Tag (16 bajtów) po nonce.
            f.write(ciphertext)  # Zaszyfrowane dane.

    # Obsługa przypadku, gdy plik wejściowy nie istnieje.
    except FileNotFoundError:
        print(f"Plik {input_path} nie został znaleziony.")
    # Obsługa innych wyjątków.
    except Exception as e:
        print(f"Błąd podczas szyfrowania pliku: {e}")


if __name__ == "__main__":
    # Generowanie losowego 256-bitowego klucza AES do testów.
    key = get_random_bytes(32)  # Przykładowy klucz 256-bitowy
    try:
        # Wywołanie funkcji szyfrującej z przykładowymi plikami.
        encrypt_file('plain_file.txt', 'encrypted_file.aes', key)
    except ValueError as ve:
        # Wyświetlenie komunikatu o błędzie, jeśli klucz nie spełnia wymagań.
        print(f"Błąd: {ve}")
