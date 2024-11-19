from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP, AES
from Crypto.Util.Padding import unpad

# Funkcja deszyfrująca tekst za pomocą klucza prywatnego RSA.
def decrypt_text_rsa(encrypted_text, private_key):
    """
    Deszyfruje tekst za pomocą RSA.
    Parametry:
    - encrypted_text: zaszyfrowany tekst w postaci binarnej.
    - private_key: klucz prywatny RSA w formacie PEM.
    Zwraca:
    - Odszyfrowany tekst w postaci zwykłego stringa.
    """
    try:
        key = RSA.import_key(private_key)  # Import klucza prywatnego.
        cipher = PKCS1_OAEP.new(key)  # Tworzenie obiektu deszyfrującego.
        decrypted_text = cipher.decrypt(encrypted_text).decode('utf-8')  # Deszyfrowanie tekstu.
        return decrypted_text
    except Exception as e:
        raise ValueError(f"Błąd podczas deszyfrowania tekstu RSA: {e}")

# Funkcja hybrydowa deszyfrująca plik (RSA dla klucza AES, AES dla danych).
def decrypt_file_hybrid(input_path, output_path, private_key):
    """
    Hybrydowe deszyfrowanie: RSA dla klucza AES, AES dla danych.
    Parametry:
    - input_path: ścieżka pliku wejściowego.
    - output_path: ścieżka pliku wyjściowego.
    - private_key: klucz prywatny RSA w formacie PEM.
    """
    try:
        with open(input_path, 'rb') as f:
            encrypted_aes_key = f.read(256)  # Odczyt zaszyfrowanego klucza AES (256 bajtów dla RSA).
            nonce = f.read(16)               # Odczyt Nonce dla AES.
            tag = f.read(16)                 # Odczyt Taga dla AES.
            ciphertext = f.read()            # Odczyt zaszyfrowanych danych.

        # Odszyfrowanie klucza AES za pomocą RSA.
        rsa_key = RSA.import_key(private_key)
        if not rsa_key.has_private():
            raise ValueError("Podany klucz RSA nie jest kluczem prywatnym.")
        rsa_cipher = PKCS1_OAEP.new(rsa_key)
        aes_key = rsa_cipher.decrypt(encrypted_aes_key)  # Deszyfrowanie klucza AES.

        # Odszyfrowanie danych za pomocą AES.
        aes_cipher = AES.new(aes_key, AES.MODE_EAX, nonce=nonce)
        plaintext = unpad(aes_cipher.decrypt_and_verify(ciphertext, tag), AES.block_size)  # Usunięcie paddingu.

        # Zapisanie odszyfrowanych danych do pliku wyjściowego.
        with open(output_path, 'wb') as f:
            f.write(plaintext)
    except Exception as e:
        raise ValueError(f"Błąd podczas deszyfrowania hybrydowego: {e}")
