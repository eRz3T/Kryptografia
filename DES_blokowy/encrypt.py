from Crypto.Cipher import DES
from Crypto.Util.Padding import pad
import os

# Funkcja do szyfrowania pliku za pomocą algorytmu DES w trybie ECB.
def encrypt_file(input_path, output_path, key):
    # Otwieramy plik wejściowy w trybie binarnym i odczytujemy jego zawartość.
    with open(input_path, 'rb') as f:
        plaintext = f.read()
    
    # Tworzymy instancję szyfru DES w trybie ECB (Electronic Codebook).
    cipher = DES.new(key, DES.MODE_ECB)
    
    # Szyfrowanie danych:
    # - Najpierw wyrównujemy dane do wielokrotności bloku DES (8 bajtów) za pomocą funkcji `pad`.
    # - Następnie szyfrujemy wyrównane dane.
    ciphertext = cipher.encrypt(pad(plaintext, DES.block_size))

    # Zapisujemy zaszyfrowane dane do pliku wyjściowego w trybie binarnym.
    with open(output_path, 'wb') as f:
        f.write(ciphertext)
