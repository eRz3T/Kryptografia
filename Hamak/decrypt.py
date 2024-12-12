import shutil
import os

def decrypt_text_hamak(encrypted_text, key):
    """
    Deszyfruje tekst za pomocą prostego przesunięcia bajtowego.
    """
    decrypted_text = bytearray()
    for char in encrypted_text:
        decrypted_char = (char - key) % 256
        decrypted_text.append(decrypted_char)
    return decrypted_text.decode('utf-8')

def decrypt_file_hamak(input_path, output_path, key):
    """
    Deszyfruje plik przy użyciu prostego przesunięcia bajtowego.
    """
    temp_file = input_path + ".copy"
    shutil.copy(input_path, temp_file)

    try:
        with open(temp_file, "rb") as infile, open(output_path, "wb") as outfile:
            while chunk := infile.read(1024):
                decrypted_chunk = bytes((byte - key) % 256 for byte in chunk)
                outfile.write(decrypted_chunk)
    except Exception as e:
        raise ValueError(f"Błąd podczas deszyfrowania pliku: {e}")
    finally:
        if os.path.exists(temp_file):
            os.remove(temp_file)
