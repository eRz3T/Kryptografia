import shutil
import os
import random

def generate_hamak_keys():
    """
    Generuje jeden klucz do szyfrowania i deszyfrowania.
    Klucz jest liczbą całkowitą w przedziale 1-255.
    """
    return random.randint(1, 255)

def encrypt_text_hamak(text, key):
    """
    Szyfruje tekst za pomocą prostego przesunięcia bajtowego.
    """
    encrypted_text = bytearray()
    for char in text.encode('utf-8'):
        encrypted_char = (char + key) % 256
        encrypted_text.append(encrypted_char)
    return bytes(encrypted_text)

def encrypt_file_hamak(input_path, output_path, key):
    """
    Szyfruje plik przy użyciu prostego przesunięcia bajtowego.
    """
    temp_file = input_path + ".copy"
    shutil.copy(input_path, temp_file)

    try:
        with open(temp_file, "rb") as infile, open(output_path, "wb") as outfile:
            while chunk := infile.read(1024):
                encrypted_chunk = bytes((byte + key) % 256 for byte in chunk)
                outfile.write(encrypted_chunk)
    except Exception as e:
        raise ValueError(f"Błąd podczas szyfrowania pliku: {e}")
    finally:
        if os.path.exists(temp_file):
            os.remove(temp_file)
