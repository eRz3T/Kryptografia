from Crypto.Cipher import DES
from Crypto.Random import get_random_bytes

def encrypt_stream(data, key):
    iv = get_random_bytes(8)  
    cipher = DES.new(key, DES.MODE_CFB, iv=iv)
    encrypted_data = iv  
    for i in range(0, len(data), 8):
        block = data[i:i+8]
        encrypted_block = cipher.encrypt(block)
        encrypted_data += encrypted_block
    return encrypted_data
