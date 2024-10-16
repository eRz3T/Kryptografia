# encrypt.py

def encrypt_message(message, key):
    """Szyfruje wiadomość za pomocą szyfru transpozycyjnego."""
    # Uzupełnij tekst spacjami, jeśli długość nie dzieli się przez klucz
    while len(message) % key != 0:
        message += ' '
    
    ciphertext = [''] * key

    for column in range(key):
        current_index = column

        while current_index < len(message):
            ciphertext[column] += message[current_index]
            current_index += key

    return ''.join(ciphertext)

def encrypt_text_file(input_file, output_file, key):
    """Szyfruje zawartość pliku tekstowego za pomocą szyfru transpozycyjnego."""
    with open(input_file, 'r') as file:
        content = file.read()

    encrypted_content = encrypt_message(content, key)

    with open(output_file, 'w') as file:
        file.write(encrypted_content)

# Przykład wywołania (możesz to usunąć, jeśli nie potrzebujesz)
if __name__ == "__main__":
    key = 3  # Klucz określający ilość kolumn
    encrypt_text_file('plain_text.txt', 'encrypted_text.txt', key)
