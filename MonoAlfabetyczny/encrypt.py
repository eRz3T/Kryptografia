def create_cipher_dict(key):
    if len(key) != 26:
        raise ValueError("Klucz szyfru monoalfabetycznego musi mieć dokładnie 26 znaków.")

    alphabet = "abcdefghijklmnopqrstuvwxyz"
    cipher = {}
    
    for i, letter in enumerate(alphabet):
        cipher[letter] = key[i]
    
    return cipher

def encrypt_text_file(input_file, output_file, key):
    cipher_dict = create_cipher_dict(key)  # Rzuci ValueError, jeśli klucz jest nieprawidłowy
    
    with open(input_file, 'r') as file:
        content = file.read().lower()  # Konwersja na małe litery
    
    encrypted_content = ''.join([cipher_dict.get(char, char) for char in content])  # Zamiana znaków
    
    with open(output_file, 'w') as file:
        file.write(encrypted_content)


if __name__ == "__main__":
    key = "qwertyuiopasdfghjklzxcvbnm"  # Przykładowy klucz
    try:
        encrypt_text_file('plain_text.txt', 'encrypted_text.txt', key)
    except ValueError as ve:
        print(f"Błąd: {ve}")
