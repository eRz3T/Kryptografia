from Crypto.Cipher import DES
from Crypto.Util.Padding import pad
import os

def encrypt_file(input_path, output_path, key):
    with open(input_path, 'rb') as f:
        plaintext = f.read()
    
    cipher = DES.new(key, DES.MODE_ECB)
    ciphertext = cipher.encrypt(pad(plaintext, DES.block_size))

    with open(output_path, 'wb') as f:
        f.write(ciphertext)
