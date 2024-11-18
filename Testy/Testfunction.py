import unittest
import os
import sys
from Crypto.Random import get_random_bytes

# Dodanie głównego katalogu do ścieżki modułów
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from AES_blokowy.gui import encrypt_file_action, decrypt_file_action


class TestFunctionalEncryptionGUI(unittest.TestCase):
    def test_gui_encrypt_action(self):
        """Testuje poprawność szyfrowania pliku przez GUI"""
        input_path = "test_plain.txt"
        output_path = "test_encrypted_gui.aes"

        with open(input_path, 'wb') as f:
            f.write(b"Testowy tekst")

        encrypt_file_action(input_path, output_path, get_random_bytes(32))
        self.assertTrue(os.path.exists(output_path), "Plik zaszyfrowany nie został utworzony")

        os.remove(input_path)
        os.remove(output_path)

    def test_gui_decrypt_action(self):
        """Testuje poprawność odszyfrowania pliku przez GUI"""
        input_path = "test_encrypted_gui.aes"
        output_path = "test_decrypted_gui.txt"
        key = get_random_bytes(32)

        with open("test_plain.txt", 'wb') as f:
            f.write(b"Testowy tekst")

        encrypt_file_action("test_plain.txt", input_path, key)
        decrypt_file_action(input_path, output_path, key)

        with open("test_plain.txt", 'rb') as f:
            original_content = f.read()
        with open(output_path, 'rb') as f:
            decrypted_content = f.read()

        self.assertEqual(original_content, decrypted_content, "Odszyfrowana treść nie jest zgodna z oryginałem")

        os.remove("test_plain.txt")
        os.remove(input_path)
        os.remove(output_path)


if __name__ == "__main__":
    unittest.main()
