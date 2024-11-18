import unittest
import os
import sys
from Crypto.Random import get_random_bytes

# Dodanie głównego katalogu projektu do ścieżki modułów
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from AES_blokowy.encrypt import encrypt_file as aes_encrypt
from AES_blokowy.decrypt import decrypt_file as aes_decrypt
from MonoAlfabetyczny.encrypt import encrypt_text_file
from MonoAlfabetyczny.decrypt import decrypt_text_file
from Diffie_Hellman.RSA.encrypt import generate_rsa_keys, encrypt_text_rsa
from Diffie_Hellman.RSA.decrypt import decrypt_text_rsa


class TestAESEncryption(unittest.TestCase):
    def setUp(self):
        self.key = get_random_bytes(32)
        self.input_path = "test_plain.txt"
        self.encrypted_path = "test_encrypted.aes"
        self.decrypted_path = "test_decrypted.txt"

        with open(self.input_path, 'wb') as f:
            f.write(b"Testowy tekst")

    def tearDown(self):
        for file_path in [self.input_path, self.encrypted_path, self.decrypted_path]:
            if os.path.exists(file_path):
                os.remove(file_path)

    def test_aes_block_encryption_decryption(self):
        aes_encrypt(self.input_path, self.encrypted_path, self.key)
        aes_decrypt(self.encrypted_path, self.decrypted_path, self.key)

        with open(self.input_path, 'rb') as f:
            original_content = f.read()
        with open(self.decrypted_path, 'rb') as f:
            decrypted_content = f.read()

        self.assertEqual(original_content, decrypted_content)

    def test_invalid_aes_key_length(self):
        invalid_key = get_random_bytes(16)
        with self.assertRaises(ValueError):
            aes_encrypt(self.input_path, self.encrypted_path, invalid_key)


class TestRSAGeneration(unittest.TestCase):
    def test_rsa_key_generation(self):
        private_key, public_key = generate_rsa_keys()
        self.assertTrue(private_key)
        self.assertTrue(public_key)

    def test_rsa_encryption_decryption(self):
        private_key, public_key = generate_rsa_keys()
        original_text = "Testowy tekst RSA"
        encrypted_text = encrypt_text_rsa(original_text, public_key)
        decrypted_text = decrypt_text_rsa(encrypted_text, private_key)
        self.assertEqual(original_text, decrypted_text)


class TestMonoalphabeticCipher(unittest.TestCase):
    def test_monoalphabetic_cipher(self):
        key = "qwertyuiopasdfghjklzxcvbnm"
        input_text = "testowytekst"
        input_file = "test_plain.txt"
        encrypted_file = "test_encrypted.txt"
        decrypted_file = "test_decrypted.txt"

        with open(input_file, "w") as f:
            f.write(input_text)

        encrypt_text_file(input_file, encrypted_file, key)
        decrypt_text_file(encrypted_file, decrypted_file, key)

        with open(decrypted_file, "r") as f:
            decrypted_text = f.read()

        self.assertEqual(input_text, decrypted_text)

        for file_path in [input_file, encrypted_file, decrypted_file]:
            if os.path.exists(file_path):
                os.remove(file_path)

    def test_monoalphabetic_invalid_key_length(self):
        key = "abcdef"
        with self.assertRaises(ValueError):
            encrypt_text_file("test_plain.txt", "test_encrypted.txt", key)


if __name__ == "__main__":
    unittest.main()
