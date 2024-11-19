def create_reverse_cipher_dict(key):
    """
    Tworzy słownik odszyfrowujący na podstawie klucza.

    Parametry:
    - key: Klucz szyfrujący (26 znaków, odpowiadających każdej literze alfabetu).

    Zwraca:
    - Słownik, gdzie kluczem jest znak z klucza, a wartością odpowiadająca mu litera alfabetu.
    """
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    cipher = {}
    
    for i, letter in enumerate(key):
        cipher[letter] = alphabet[i]  # Tworzenie odwrotnego mapowania.

    return cipher

def decrypt_text_file(input_file, output_file, key):
    """
    Odszyfrowuje zawartość pliku tekstowego za pomocą szyfru monoalfabetycznego.

    Parametry:
    - input_file: Ścieżka do pliku wejściowego (zaszyfrowany tekst).
    - output_file: Ścieżka do pliku wyjściowego (odszyfrowany tekst).
    - key: Klucz szyfrujący.

    Działanie:
    - Odczytuje zawartość pliku wejściowego.
    - Odszyfrowuje każdą literę zgodnie z kluczem.
    - Zapisuje odszyfrowany tekst do pliku wyjściowego.
    """
    reverse_cipher_dict = create_reverse_cipher_dict(key)  # Tworzenie słownika odszyfrowującego.
    
    with open(input_file, 'r') as file:
        content = file.read().lower()  # Odczyt i konwersja na małe litery.
    
    decrypted_content = ''.join([reverse_cipher_dict.get(char, char) for char in content])  # Odszyfrowanie liter.
    
    with open(output_file, 'w') as file:
        file.write(decrypted_content)  # Zapis odszyfrowanej zawartości.

if __name__ == "__main__":
    key = "qwertyuiopasdfghjklzxcvbnm"  # Przykładowy klucz szyfrujący.
    decrypt_text_file('encrypted_text.txt', 'decrypted_text.txt', key)  # Odszyfrowanie pliku.
