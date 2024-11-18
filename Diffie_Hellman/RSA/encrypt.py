from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP, AES
from Crypto.Random import get_random_bytes
from Crypto.Util.Padding import pad

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
    try:
        aes_key = get_random_bytes(32)  # Klucz AES
        nonce = get_random_bytes(16)   # Nonce dla AES

        # Szyfrowanie danych za pomocą AES
        aes_cipher = AES.new(aes_key, AES.MODE_EAX, nonce=nonce)
        with open(input_path, 'rb') as f:
            file_data = f.read()
        ciphertext, tag = aes_cipher.encrypt_and_digest(pad(file_data, AES.block_size))

        # Szyfrowanie klucza AES za pomocą RSA
        rsa_key = RSA.import_key(public_key)
        rsa_cipher = PKCS1_OAEP.new(rsa_key)
        encrypted_aes_key = rsa_cipher.encrypt(aes_key)

        # Zapisanie zaszyfrowanych danych do pliku
        with open(output_path, 'wb') as f:
            f.write(encrypted_aes_key + nonce + tag + ciphertext)
    except Exception as e:
        raise ValueError(f"Błąd podczas szyfrowania hybrydowego: {e}")
