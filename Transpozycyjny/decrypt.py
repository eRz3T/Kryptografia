def decrypt_message(message, key):
    """
    Odszyfrowuje wiadomość zaszyfrowaną szyfrem transpozycyjnym.

    Parametry:
    - message: Zaszyfrowana wiadomość.
    - key: Liczba kolumn w szyfrze transpozycyjnym.

    Zwraca:
    - Odszyfrowany tekst jako string.
    """
    # Obliczanie liczby kolumn i rzędów.
    num_of_columns = int(len(message) / key)
    num_of_rows = key
    num_of_shaded_boxes = (num_of_columns * num_of_rows) - len(message)

    # Tworzenie listy do przechowywania odszyfrowanych danych.
    plaintext = [''] * num_of_columns
    column = 0
    row = 0

    # Iteracja przez zaszyfrowaną wiadomość.
    for symbol in message:
        plaintext[column] += symbol
        column += 1

        # Przechodzenie do następnego wiersza w odpowiednim momencie.
        if (column == num_of_columns) or (column == num_of_columns - 1 and row >= num_of_rows - num_of_shaded_boxes):
            column = 0
            row += 1

    # Łączenie kolumn i usuwanie dodatkowych spacji.
    return ''.join(plaintext).rstrip() 

def decrypt_text_file(input_file, output_file, key):
    """
    Odszyfrowuje zawartość pliku tekstowego zaszyfrowanego szyfrem transpozycyjnym.

    Parametry:
    - input_file: Ścieżka do zaszyfrowanego pliku.
    - output_file: Ścieżka do pliku odszyfrowanego.
    - key: Liczba kolumn w szyfrze transpozycyjnym.
    """
    # Odczytanie zawartości pliku wejściowego.
    with open(input_file, 'r') as file:
        content = file.read()

    # Odszyfrowanie zawartości pliku.
    decrypted_content = decrypt_message(content, key)

    # Zapisanie odszyfrowanej zawartości do pliku wyjściowego.
    with open(output_file, 'w') as file:
        file.write(decrypted_content)

if __name__ == "__main__":
    key = 3  # Przykładowy klucz szyfrowania.
    decrypt_text_file('encrypted_text.txt', 'decrypted_text.txt', key)
