from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP, AES
from Crypto.Util.Padding import unpad

def decrypt_text_rsa(encrypted_text, private_key):
    try:
        key = RSA.import_key(private_key)
        cipher = PKCS1_OAEP.new(key)
        decrypted_text = cipher.decrypt(encrypted_text).decode('utf-8')
        return decrypted_text
    except Exception as e:
        raise ValueError(f"Błąd podczas deszyfrowania tekstu RSA: {e}")

def decrypt_file_hybrid(input_path, output_path, private_key):
    """
    Hybrydowe deszyfrowanie: RSA dla klucza AES, AES dla danych.
    """
    try:
        with open(input_path, 'rb') as f:
            encrypted_aes_key = f.read(256)  # Klucz AES zaszyfrowany RSA
            nonce = f.read(16)               # Nonce dla AES
            tag = f.read(16)                 # Tag dla AES
            ciphertext = f.read()            # Zaszyfrowana zawartość

        rsa_key = RSA.import_key(private_key)
        if not rsa_key.has_private():
            raise ValueError("Podany klucz RSA nie jest kluczem prywatnym.")
        rsa_cipher = PKCS1_OAEP.new(rsa_key)
        aes_key = rsa_cipher.decrypt(encrypted_aes_key)

        aes_cipher = AES.new(aes_key, AES.MODE_EAX, nonce=nonce)
        plaintext = unpad(aes_cipher.decrypt_and_verify(ciphertext, tag), AES.block_size)

        with open(output_path, 'wb') as f:
            f.write(plaintext)

    except Exception as e:
        raise ValueError(f"Błąd podczas deszyfrowania hybrydowego: {e}")

def decrypt_file_rsa(input_path, output_path, private_key):
    try:
        with open(input_path, 'rb') as f:
            encrypted_data = f.read()

        rsa_key = RSA.import_key(private_key)
        if not rsa_key.has_private():
            raise TypeError("Podany klucz RSA nie jest kluczem prywatnym.")
        rsa_cipher = PKCS1_OAEP.new(rsa_key)
        decrypted_data = rsa_cipher.decrypt(encrypted_data)

        with open(output_path, 'wb') as f:
            f.write(decrypted_data)
    except Exception as e:
        raise ValueError(f"Błąd podczas deszyfrowania pliku RSA: {e}")
