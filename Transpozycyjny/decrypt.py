# decrypt.py

def decrypt_message(message, key):
    """Odszyfrowuje wiadomość zaszyfrowaną szyfrem transpozycyjnym."""
    num_of_columns = int(len(message) / key)
    num_of_rows = key
    num_of_shaded_boxes = (num_of_columns * num_of_rows) - len(message)

    plaintext = [''] * num_of_columns
    column = 0
    row = 0

    for symbol in message:
        plaintext[column] += symbol
        column += 1

        if (column == num_of_columns) or (column == num_of_columns - 1 and row >= num_of_rows - num_of_shaded_boxes):
            column = 0
            row += 1

    return ''.join(plaintext).rstrip()  # Usuń nadmiarowe spacje, które mogły zostać dodane

def decrypt_text_file(input_file, output_file, key):
    """Odszyfrowuje zawartość pliku tekstowego zaszyfrowanego szyfrem transpozycyjnym."""
    with open(input_file, 'r') as file:
        content = file.read()

    decrypted_content = decrypt_message(content, key)

    with open(output_file, 'w') as file:
        file.write(decrypted_content)

# Przykład wywołania (możesz to usunąć, jeśli nie potrzebujesz)
if __name__ == "__main__":
    key = 3  # Klucz określający ilość kolumn
    decrypt_text_file('encrypted_text.txt', 'decrypted_text.txt', key)
