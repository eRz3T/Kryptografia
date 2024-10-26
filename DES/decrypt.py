from Crypto.Cipher import DES
from Crypto.Util.Padding import unpad
import os

def decrypt_file(input_path, output_path, key):
    with open(input_path, 'rb') as f:
        ciphertext = f.read()
    
    cipher = DES.new(key, DES.MODE_ECB)
    plaintext = unpad(cipher.decrypt(ciphertext), DES.block_size)

    with open(output_path, 'wb') as f:
        f.write(plaintext)
