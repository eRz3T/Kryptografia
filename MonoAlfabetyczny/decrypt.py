# decrypt.py

def create_reverse_cipher_dict(key):
    """Funkcja tworzy słownik odszyfrowujący na podstawie klucza."""
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    cipher = {}
    
    for i, letter in enumerate(key):
        cipher[letter] = alphabet[i]
    
    return cipher

def decrypt_text_file(input_file, output_file, key):
    """Odszyfrowuje zawartość pliku tekstowego za pomocą szyfru monoalfabetycznego."""
    reverse_cipher_dict = create_reverse_cipher_dict(key)
    
    with open(input_file, 'r') as file:
        content = file.read().lower()  # Odczyt zawartości i zamiana na małe litery
    
    decrypted_content = ''.join([reverse_cipher_dict.get(char, char) for char in content])  # Odszyfrowanie
    
    with open(output_file, 'w') as file:
        file.write(decrypted_content)  # Zapis odszyfrowanej treści

# Przykład wywołania
if __name__ == "__main__":
    key = "qwertyuiopasdfghjklzxcvbnm"  # Twój klucz szyfrujący
    decrypt_text_file('encrypted_text.txt', 'decrypted_text.txt', key)
