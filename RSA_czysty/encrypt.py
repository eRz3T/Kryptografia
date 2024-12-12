import os
import shutil
from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP

def encrypt_file_rsa(input_path, output_path, public_key):
    """
    Szyfruje plik za pomocą RSA, dzieląc go na odpowiednie bloki, pracując na kopii pliku.
    """
    temp_file = input_path + ".copy"  # Tworzymy kopię pliku tymczasowego
    shutil.copy(input_path, temp_file)

    key = RSA.import_key(public_key)
    cipher = PKCS1_OAEP.new(key)
    max_chunk_size = key.size_in_bytes() - 42  # Maksymalny rozmiar bloku dla RSA z paddingiem OAEP

    try:
        with open(temp_file, "rb") as infile, open(output_path, "wb") as outfile:
            while chunk := infile.read(max_chunk_size):
                encrypted_chunk = cipher.encrypt(chunk)
                # Zapisujemy długość bloku zaszyfrowanego i jego zawartość
                outfile.write(len(encrypted_chunk).to_bytes(4, "big"))
                outfile.write(encrypted_chunk)

        print("Szyfrowanie pliku zakończone.")
    except Exception as e:
        raise ValueError(f"Błąd podczas szyfrowania pliku RSA: {e}")
    finally:
        # Usuwamy kopię pliku
        if os.path.exists(temp_file):
            os.remove(temp_file)

# Funkcja generująca klucze RSA
def generate_rsa_keys():
    key = RSA.generate(2048)
    private_key = key.export_key()
    public_key = key.publickey().export_key()
    return private_key, public_key


def encrypt_text_rsa(text, public_key):
    """
    Szyfruje tekst za pomocą RSA i zapisuje w blokach.
    """
    rsa_key = RSA.import_key(public_key)
    cipher = PKCS1_OAEP.new(rsa_key)
    block_size = rsa_key.size_in_bytes() - 42  # Maksymalny rozmiar dla PKCS1_OAEP

    encrypted_blocks = []
    for i in range(0, len(text), block_size):
        block = text[i:i + block_size].encode("utf-8")  # Konwersja bloku do bajtów
        encrypted_block = cipher.encrypt(block)
        block_length = len(encrypted_block).to_bytes(4, "big")  # Długość bloku (4 bajty)
        encrypted_blocks.append(block_length + encrypted_block)

    return b"".join(encrypted_blocks)
