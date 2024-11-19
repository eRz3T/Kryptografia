from Crypto.Cipher import DES
from Crypto.Random import get_random_bytes

# Funkcja szyfrująca dane w trybie strumieniowym DES (CFB - Cipher Feedback Mode)
def encrypt_stream(data, key):
    # Generowanie losowego wektora inicjalizującego (IV) o długości 8 bajtów.
    iv = get_random_bytes(8)
    
    # Tworzenie instancji szyfru DES w trybie CFB z podanym kluczem i IV.
    cipher = DES.new(key, DES.MODE_CFB, iv=iv)
    
    # Zapisanie IV jako początkowej części zaszyfrowanego strumienia.
    encrypted_data = iv
    
    # Szyfrowanie danych w blokach po 8 bajtów.
    for i in range(0, len(data), 8):
        block = data[i:i+8]  # Wyodrębnienie bloku danych o maksymalnej długości 8 bajtów.
        encrypted_block = cipher.encrypt(block)  # Szyfrowanie bloku.
        encrypted_data += encrypted_block  # Dodanie zaszyfrowanego bloku do wyniku.
    
    # Zwrócenie pełnego strumienia: IV + zaszyfrowane dane.
    return encrypted_data
