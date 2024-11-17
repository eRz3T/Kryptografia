from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes

def encrypt_stream(data, key):
    iv = get_random_bytes(16)  
    cipher = AES.new(key, AES.MODE_CFB, iv=iv)
    encrypted_data = iv  
    encrypted_data += cipher.encrypt(data)
    return encrypted_data
