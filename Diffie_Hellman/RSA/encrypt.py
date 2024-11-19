from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP, AES
from Crypto.Random import get_random_bytes
from Crypto.Util.Padding import pad

# Funkcja generująca parę kluczy RSA (prywatny i publiczny).
def generate_rsa_keys():
    """
    Generuje parę kluczy RSA (2048-bitowe).
    Zwraca:
    - Klucz prywatny w formacie PEM.
    - Klucz publiczny w formacie PEM.
    """
    key = RSA.generate(2048)  # Generowanie klucza RSA o długości 2048 bitów.
    private_key = key.export_key()  # Eksport klucza prywatnego.
    public_key = key.publickey().export_key()  # Eksport klucza publicznego.
    return private_key, public_key

# Funkcja szyfrująca tekst za pomocą klucza publicznego RSA.
def encrypt_text_rsa(text, public_key):
    """
    Szyfruje tekst za pomocą RSA.
    Parametry:
    - text: tekst do zaszyfrowania.
    - public_key: klucz publiczny RSA w formacie PEM.
    Zwraca:
    - Zaszyfrowany tekst w postaci binarnej.
    """
    key = RSA.import_key(public_key)  # Import klucza publicznego.
    cipher = PKCS1_OAEP.new(key)  # Tworzenie obiektu szyfrującego.
    encrypted_text = cipher.encrypt(text.encode())  # Szyfrowanie tekstu.
    return encrypted_text

# Funkcja hybrydowa szyfrująca plik (RSA dla klucza AES, AES dla danych).
def encrypt_file_hybrid(input_path, output_path, public_key):
    """
    Hybrydowe szyfrowanie pliku za pomocą RSA i AES.
    Parametry:
    - input_path: ścieżka pliku wejściowego.
    - output_path: ścieżka pliku wyjściowego.
    - public_key: klucz publiczny RSA w formacie PEM.
    """
    try:
        aes_key = get_random_bytes(32)  # Generowanie klucza AES (256-bitowego).
        nonce = get_random_bytes(16)   # Generowanie Nonce dla AES.

        # Szyfrowanie danych za pomocą AES.
        aes_cipher = AES.new(aes_key, AES.MODE_EAX, nonce=nonce)  # AES w trybie EAX.
        with open(input_path, 'rb') as f:
            file_data = f.read()
        ciphertext, tag = aes_cipher.encrypt_and_digest(pad(file_data, AES.block_size))  # Szyfrowanie danych z paddingiem.

        # Szyfrowanie klucza AES za pomocą RSA.
        rsa_key = RSA.import_key(public_key)
        rsa_cipher = PKCS1_OAEP.new(rsa_key)
        encrypted_aes_key = rsa_cipher.encrypt(aes_key)  # Klucz AES jest szyfrowany RSA.

        # Zapisanie zaszyfrowanych danych do pliku wyjściowego.
        with open(output_path, 'wb') as f:
            f.write(encrypted_aes_key + nonce + tag + ciphertext)  # Zapis klucza AES, Nonce, Taga i zaszyfrowanych danych.
    except Exception as e:
        raise ValueError(f"Błąd podczas szyfrowania hybrydowego: {e}")
