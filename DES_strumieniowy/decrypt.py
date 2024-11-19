from Crypto.Cipher import DES

# Funkcja odszyfrowująca dane w trybie strumieniowym DES (CFB - Cipher Feedback Mode)
def decrypt_stream(encrypted_data, key):
    # Wyodrębnienie wektora inicjalizującego (IV) z pierwszych 8 bajtów strumienia zaszyfrowanego.
    iv = encrypted_data[:8]
    
    # Tworzenie instancji szyfru DES w trybie CFB z podanym kluczem i IV.
    cipher = DES.new(key, DES.MODE_CFB, iv=iv)
    
    # Zmienna przechowująca odszyfrowane dane.
    decrypted_data = b""
    
    # Odszyfrowywanie danych w blokach po 8 bajtów.
    for i in range(8, len(encrypted_data), 8):
        encrypted_block = encrypted_data[i:i+8]  # Wyodrębnienie zaszyfrowanego bloku.
        decrypted_block = cipher.decrypt(encrypted_block)  # Odszyfrowanie bloku.
        decrypted_data += decrypted_block  # Dodanie odszyfrowanego bloku do wyniku.
    
    # Zwrócenie odszyfrowanych danych.
    return decrypted_data
