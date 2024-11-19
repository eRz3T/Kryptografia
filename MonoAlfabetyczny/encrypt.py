def create_cipher_dict(key):
    """
    Tworzy słownik szyfrujący na podstawie klucza.
    
    Parametry:
    - key: Klucz szyfrujący (26 znaków, odpowiadających każdej literze alfabetu).

    Zwraca:
    - Słownik, gdzie kluczem jest litera alfabetu, a wartością jej odpowiednik w kluczu.
    """
    if len(key) != 26:
        raise ValueError("Klucz szyfru monoalfabetycznego musi mieć dokładnie 26 znaków.")

    alphabet = "abcdefghijklmnopqrstuvwxyz"
    cipher = {}
    
    for i, letter in enumerate(alphabet):
        cipher[letter] = key[i]  # Tworzenie mapowania litery alfabetu na znak z klucza.
    
    return cipher

def encrypt_text_file(input_file, output_file, key):
    """
    Szyfruje zawartość pliku tekstowego za pomocą szyfru monoalfabetycznego.

    Parametry:
    - input_file: Ścieżka do pliku wejściowego.
    - output_file: Ścieżka do pliku wyjściowego.
    - key: Klucz szyfrujący.

    Działanie:
    - Odczytuje zawartość pliku wejściowego.
    - Szyfruje każdą literę zgodnie z kluczem.
    - Zapisuje zaszyfrowany tekst do pliku wyjściowego.
    """
    cipher_dict = create_cipher_dict(key)  # Tworzenie słownika szyfrującego.
    
    with open(input_file, 'r') as file:
        content = file.read().lower()  # Odczyt i konwersja na małe litery.
    
    encrypted_content = ''.join([cipher_dict.get(char, char) for char in content])  # Szyfrowanie liter.
    
    with open(output_file, 'w') as file:
        file.write(encrypted_content)  # Zapis zaszyfrowanej zawartości.

if __name__ == "__main__":
    key = "qwertyuiopasdfghjklzxcvbnm"  # Przykładowy klucz szyfrujący.
    try:
        encrypt_text_file('plain_text.txt', 'encrypted_text.txt', key)  # Szyfrowanie pliku.
    except ValueError as ve:
        print(f"Błąd: {ve}")
