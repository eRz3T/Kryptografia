from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes
from Crypto.Util.Padding import pad
import os

def encrypt_file(input_path, output_path, key):
    if len(key) != 32:
        raise ValueError("Klucz AES musi mieć dokładnie 32 bajty (256 bitów).")

    try:
        with open(input_path, 'rb') as f:
            plaintext = f.read()

        cipher = AES.new(key, AES.MODE_EAX)
        nonce = cipher.nonce
        ciphertext, tag = cipher.encrypt_and_digest(pad(plaintext, AES.block_size))

        with open(output_path, 'wb') as f:
            f.write(nonce)
            f.write(tag)
            f.write(ciphertext)

    except FileNotFoundError:
        print(f"Plik {input_path} nie został znaleziony.")
    except Exception as e:
        print(f"Błąd podczas szyfrowania pliku: {e}")


if __name__ == "__main__":
    key = get_random_bytes(32)  # Przykładowy klucz 256-bitowy
    try:
        encrypt_file('plain_file.txt', 'encrypted_file.aes', key)
    except ValueError as ve:
        print(f"Błąd: {ve}")
