from Crypto.Cipher import AES

# Funkcja odszyfrowująca dane w trybie strumieniowym AES (CFB - Cipher Feedback Mode).
def decrypt_stream(encrypted_data, key):
    # Wyodrębnienie wektora inicjalizującego (IV) z pierwszych 16 bajtów strumienia.
    iv = encrypted_data[:16]
    
    # Utworzenie instancji szyfru AES w trybie CFB z podanym kluczem i IV.
    cipher = AES.new(key, AES.MODE_CFB, iv=iv)
    
    # Odszyfrowanie danych.
    # Pomijamy pierwsze 16 bajtów (IV) i odszyfrowujemy resztę strumienia.
    decrypted_data = cipher.decrypt(encrypted_data[16:])
    
    # Zwrócenie odszyfrowanych danych.
    return decrypted_data
