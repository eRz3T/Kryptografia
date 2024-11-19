def encrypt_message(message, key):
    """
    Szyfruje wiadomość za pomocą szyfru transpozycyjnego.
    
    Parametry:
    - message: Tekst, który ma zostać zaszyfrowany.
    - key: Liczba kolumn w szyfrze transpozycyjnym.

    Zwraca:
    - Zaszyfrowany tekst jako string.
    """
    # Dodawanie pustych znaków, aby długość wiadomości była wielokrotnością klucza.
    while len(message) % key != 0:
        message += ' '
    
    # Tworzenie pustej listy, która przechowuje zaszyfrowane kolumny.
    ciphertext = [''] * key

    # Iteracja przez każdą kolumnę w szyfrze.
    for column in range(key):
        current_index = column

        # Przechodzenie przez kolumny i dodawanie liter do odpowiednich kolumn.
        while current_index < len(message):
            ciphertext[column] += message[current_index]
            current_index += key

    # Łączenie zaszyfrowanych kolumn w jeden ciąg tekstowy.
    return ''.join(ciphertext)

def encrypt_text_file(input_file, output_file, key):
    """
    Szyfruje zawartość pliku tekstowego za pomocą szyfru transpozycyjnego.

    Parametry:
    - input_file: Ścieżka do pliku wejściowego (plain text).
    - output_file: Ścieżka do pliku wyjściowego (zaszyfrowany tekst).
    - key: Liczba kolumn w szyfrze transpozycyjnym.
    """
    # Odczytanie zawartości pliku wejściowego.
    with open(input_file, 'r') as file:
        content = file.read()

    # Szyfrowanie zawartości pliku.
    encrypted_content = encrypt_message(content, key)

    # Zapisanie zaszyfrowanej zawartości do pliku wyjściowego.
    with open(output_file, 'w') as file:
        file.write(encrypted_content)

if __name__ == "__main__":
    key = 3  # Przykładowy klucz szyfrowania.
    encrypt_text_file('plain_text.txt', 'encrypted_text.txt', key)
