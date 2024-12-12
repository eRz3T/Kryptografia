import os
import shutil
from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP


def decrypt_file_rsa(input_path, output_path, private_key):
    """
    Deszyfruje plik za pomocą RSA, odczytując bloki o odpowiednim rozmiarze.
    """
    temp_file = input_path + ".copy"  # Tworzymy kopię pliku tymczasowego
    shutil.copy(input_path, temp_file)

    key = RSA.import_key(private_key)
    cipher = PKCS1_OAEP.new(key)

    try:
        with open(temp_file, "rb") as infile, open(output_path, "wb") as outfile:
            while True:
                length_bytes = infile.read(4)  # Odczytujemy długość bloku (4 bajty)
                if not length_bytes:
                    break  # Koniec pliku
                block_length = int.from_bytes(length_bytes, "big")
                encrypted_chunk = infile.read(block_length)
                if len(encrypted_chunk) != block_length:
                    raise ValueError("Błąd podczas odczytu bloku.")
                decrypted_chunk = cipher.decrypt(encrypted_chunk)
                outfile.write(decrypted_chunk)

        print("Deszyfrowanie pliku zakończone.")
    except Exception as e:
        raise ValueError(f"Błąd podczas deszyfrowania pliku RSA: {e}")
    finally:
        # Usuwamy kopię pliku
        if os.path.exists(temp_file):
            os.remove(temp_file)
            
def decrypt_text_rsa(encrypted_text, private_key):
    """
    Deszyfruje tekst za pomocą RSA w blokach.
    """
    rsa_key = RSA.import_key(private_key)
    cipher = PKCS1_OAEP.new(rsa_key)
    block_size = rsa_key.size_in_bytes()

    decrypted_blocks = []
    i = 0
    while i < len(encrypted_text):
        block_length = int.from_bytes(encrypted_text[i:i+4], "big")  # Odczyt długości bloku (4 bajty)
        i += 4
        encrypted_block = encrypted_text[i:i+block_length]
        if len(encrypted_block) != block_length:
            raise ValueError("Błąd podczas odczytu bloku.")
        decrypted_block = cipher.decrypt(encrypted_block)
        decrypted_blocks.append(decrypted_block.decode("utf-8"))
        i += block_length

    return "".join(decrypted_blocks)
