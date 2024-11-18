from Crypto.Cipher import AES
from Crypto.Util.Padding import unpad
import os

def decrypt_file(input_path, output_path, key):
    try:
        with open(input_path, 'rb') as f:
            nonce = f.read(16)
            tag = f.read(16)
            ciphertext = f.read()

        cipher = AES.new(key, AES.MODE_EAX, nonce=nonce)
        plaintext = unpad(cipher.decrypt_and_verify(ciphertext, tag), AES.block_size)

        with open(output_path, 'wb') as f:
            f.write(plaintext)
    except Exception as e:
        print(f"Błąd podczas deszyfrowania: {e}")
