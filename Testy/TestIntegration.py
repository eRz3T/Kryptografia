import unittest
import os
import sys

# Dodanie głównego katalogu projektu do ścieżki modułów
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from Diffie_Hellman.simulation import generate_shared_key
from Diffie_Hellman.RSA.encrypt import generate_rsa_keys
from Diffie_Hellman.RSA.encrypt import encrypt_file_hybrid
from Diffie_Hellman.RSA.decrypt import decrypt_file_hybrid


class TestIntegrationAESRSA(unittest.TestCase):
    def setUp(self):
        self.input_path = "test_plain.txt"
        self.encrypted_path = "test_hybrid_encrypted.aes"
        self.decrypted_path = "test_decrypted.txt"
        self.private_key, self.public_key = generate_rsa_keys()

        with open(self.input_path, 'wb') as f:
            f.write(b"Testowy tekst")
        with open("private_key.pem", "wb") as priv_file:
            priv_file.write(self.private_key)
        with open("public_key.pem", "wb") as pub_file:
            pub_file.write(self.public_key)

    def tearDown(self):
        for file_path in [self.input_path, self.encrypted_path, self.decrypted_path]:
            if os.path.exists(file_path):
                os.remove(file_path)

    def test_hybrid_encryption(self):
        encrypt_file_hybrid(self.input_path, self.encrypted_path, self.public_key)
        decrypt_file_hybrid(self.encrypted_path, self.decrypted_path, self.private_key)

        with open(self.input_path, 'rb') as f:
            original_content = f.read()
        with open(self.decrypted_path, 'rb') as f:
            decrypted_content = f.read()

        self.assertEqual(original_content, decrypted_content)

    def test_diffie_hellman_key_exchange(self):
        alice_public, alice_private = generate_shared_key()
        bob_public, bob_private = generate_shared_key()
        alice_shared = generate_shared_key(bob_public, alice_private)
        bob_shared = generate_shared_key(alice_public, bob_private)
        self.assertEqual(alice_shared, bob_shared)


if __name__ == "__main__":
    unittest.main()
