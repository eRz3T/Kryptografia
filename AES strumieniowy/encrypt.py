from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes

def encrypt_stream(data, key):
    iv = get_random_bytes(16)  # 16 bajtowy wektor inicjalizacyjny
    cipher = AES.new(key, AES.MODE_CFB, iv=iv)
    encrypted_data = iv  # Dołączamy IV do początku zaszyfrowanych danych
    encrypted_data += cipher.encrypt(data)
    return encrypted_data
