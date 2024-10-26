from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes
from Crypto.Util.Padding import pad
import os

def encrypt_file(input_path, output_path, key):
    with open(input_path, 'rb') as f:
        plaintext = f.read()

    cipher = AES.new(key, AES.MODE_EAX)
    nonce = cipher.nonce
    ciphertext, tag = cipher.encrypt_and_digest(pad(plaintext, AES.block_size))

    with open(output_path, 'wb') as f:
        f.write(nonce)
        f.write(tag)
        f.write(ciphertext)
