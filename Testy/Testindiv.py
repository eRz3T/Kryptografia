import unittest
from Crypto.Random import get_random_bytes
from encrypt import encrypt_file as aes_encrypt
from decrypt import decrypt_file as aes_decrypt

class TestAESEncryption(unittest.TestCase):
    def setUp(self):
        self.key = get_random_bytes(32)  # 32-bajtowy klucz dla AES
        self.input_path = "test_plain.txt"
        self.encrypted_path = "test_encrypted.aes"
        self.decrypted_path = "test_decrypted.txt"
        
        with open(self.input_path, 'wb') as f:
            f.write(b"Testowy tekst")

    def test_aes_block_encryption_decryption(self):
        aes_encrypt(self.input_path, self.encrypted_path, self.key)
        aes_decrypt(self.encrypted_path, self.decrypted_path, self.key)
        
        with open(self.input_path, 'rb') as f:
            original_content = f.read()
        with open(self.decrypted_path, 'rb') as f:
            decrypted_content = f.read()
            
        self.assertEqual(original_content, decrypted_content)

    def test_invalid_aes_key_length(self):
        invalid_key = get_random_bytes(16)  # 16-bajtowy klucz zamiast 32
        with self.assertRaises(ValueError):
            aes_encrypt(self.input_path, self.encrypted_path, invalid_key)

class TestRSAGeneration(unittest.TestCase):
    def test_rsa_key_generation(self):
        from encrypt import generate_rsa_keys
        private_key, public_key = generate_rsa_keys()
        self.assertTrue(private_key)
        self.assertTrue(public_key)

    def test_rsa_encryption_decryption(self):
        from encrypt import encrypt_text_rsa
        from decrypt import decrypt_text_rsa
        private_key, public_key = generate_rsa_keys()
        original_text = "Testowy tekst RSA"
        encrypted_text = encrypt_text_rsa(original_text, public_key)
        decrypted_text = decrypt_text_rsa(encrypted_text, private_key)
        self.assertEqual(original_text, decrypted_text)

class TestMonoalphabeticCipher(unittest.TestCase):
    def test_monoalphabetic_cipher(self):
        from encrypt import encrypt_text_file
        from decrypt import decrypt_text_file
        key = "qwertyuiopasdfghjklzxcvbnm"
        input_text = "testowytekst"
        with open("test_plain.txt", "w") as f:
            f.write(input_text)
        encrypt_text_file("test_plain.txt", "test_encrypted.txt", key)
        decrypt_text_file("test_encrypted.txt", "test_decrypted.txt", key)
        with open("test_decrypted.txt", "r") as f:
            decrypted_text = f.read()
        self.assertEqual(input_text, decrypted_text)

    def test_monoalphabetic_invalid_key_length(self):
        key = "abcdef"  # Krótszy niż wymagane 26 znaków
        with self.assertRaises(ValueError):
            encrypt_text_file("test_plain.txt", "test_encrypted.txt", key)

if __name__ == "__main__":
    unittest.main()
