# encrypt.py

def create_cipher_dict(key):
    """Funkcja tworzy słownik szyfru monoalfabetycznego na podstawie klucza."""
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    cipher = {}
    
    for i, letter in enumerate(alphabet):
        cipher[letter] = key[i]
    
    return cipher

def encrypt_text_file(input_file, output_file, key):
    """Szyfruje zawartość pliku tekstowego za pomocą szyfru monoalfabetycznego."""
    cipher_dict = create_cipher_dict(key)
    
    with open(input_file, 'r') as file:
        content = file.read().lower()  # Odczyt zawartości i zamiana na małe litery
    
    encrypted_content = ''.join([cipher_dict.get(char, char) for char in content])  # Szyfrowanie
    
    with open(output_file, 'w') as file:
        file.write(encrypted_content)  # Zapis zaszyfrowanej treści

# Przykład wywołania
if __name__ == "__main__":
    key = "qwertyuiopasdfghjklzxcvbnm"  # Twój klucz szyfrujący
    encrypt_text_file('plain_text.txt', 'encrypted_text.txt', key)
