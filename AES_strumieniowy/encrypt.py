from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes

# Funkcja szyfrująca dane w trybie strumieniowym AES (CFB - Cipher Feedback Mode).
def encrypt_stream(data, key):
    # Generowanie losowego wektora inicjalizującego (IV) o długości 16 bajtów.
    iv = get_random_bytes(16)
    
    # Utworzenie instancji szyfru AES w trybie CFB z podanym kluczem i IV.
    cipher = AES.new(key, AES.MODE_CFB, iv=iv)
    
    # Szyfrowanie danych. 
    # W trybie CFB dane wejściowe są szyfrowane strumieniowo, a IV jest wymagane do deszyfrowania.
    encrypted_data = iv  # Zapisanie IV na początku strumienia wyjściowego.
    encrypted_data += cipher.encrypt(data)  # Dołączenie zaszyfrowanych danych.

    # Zwrócenie pełnego strumienia: IV + zaszyfrowane dane.
    return encrypted_data
