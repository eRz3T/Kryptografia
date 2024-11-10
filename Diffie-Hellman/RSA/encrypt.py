from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP, AES
from Crypto.Random import get_random_bytes
import os

def generate_rsa_keys():
    key = RSA.generate(2048)
    private_key = key.export_key()
    public_key = key.publickey().export_key()
    return private_key, public_key

def encrypt_text_rsa(text, public_key):
    key = RSA.import_key(public_key)
    cipher = PKCS1_OAEP.new(key)
    encrypted_text = cipher.encrypt(text.encode())
    return encrypted_text

def encrypt_file_hybrid(input_path, output_path, public_key):
    # 1. Wygenerowanie losowego klucza AES
    aes_key = get_random_bytes(32)  # Klucz AES 256-bitowy
    iv = get_random_bytes(16)       # Wektor inicjalizacyjny dla AES

    # 2. Szyfrowanie pliku przy użyciu AES
    aes_cipher = AES.new(aes_key, AES.MODE_CFB, iv=iv)
    
    with open(input_path, 'rb') as f:
        file_data = f.read()
    encrypted_data = aes_cipher.encrypt(file_data)

    # 3. Zaszyfrowanie klucza AES przy użyciu RSA
    rsa_key = RSA.import_key(public_key)
    rsa_cipher = PKCS1_OAEP.new(rsa_key)
    encrypted_aes_key = rsa_cipher.encrypt(aes_key)

    # 4. Zapisanie zaszyfrowanego klucza AES, wektora IV oraz zaszyfrowanych danych do pliku wyjściowego
    with open(output_path, 'wb') as f:
        f.write(encrypted_aes_key + iv + encrypted_data)
