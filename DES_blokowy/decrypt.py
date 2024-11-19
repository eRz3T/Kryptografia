from Crypto.Cipher import DES
from Crypto.Util.Padding import unpad
import os

# Funkcja do deszyfrowania pliku za pomocą algorytmu DES w trybie ECB.
def decrypt_file(input_path, output_path, key):
    # Otwieramy plik zaszyfrowany w trybie binarnym i odczytujemy jego zawartość.
    with open(input_path, 'rb') as f:
        ciphertext = f.read()
    
    # Tworzymy instancję szyfru DES w trybie ECB (Electronic Codebook).
    cipher = DES.new(key, DES.MODE_ECB)
    
    # Odszyfrowujemy dane:
    # - Najpierw deszyfrujemy dane z pliku.
    # - Następnie usuwamy wyrównanie za pomocą funkcji `unpad`.
    plaintext = unpad(cipher.decrypt(ciphertext), DES.block_size)

    # Zapisujemy odszyfrowane dane do pliku wyjściowego w trybie binarnym.
    with open(output_path, 'wb') as f:
        f.write(plaintext)
