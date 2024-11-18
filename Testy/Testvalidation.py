import sys
import os
import unittest  # Dodanie importu unittest
from Crypto.Random import get_random_bytes

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from AES_blokowy.gui import get_key
from AES_blokowy.encrypt import generate_rsa_keys, validate_mono_key

class TestValidation(unittest.TestCase):
    def test_aes_key_length(self):
        from gui import get_key
        invalid_key = "short_key"
        valid_key = "a" * 32
        
        # Sprawdzenie nieprawidłowego klucza
        with self.assertRaises(ValueError):
            get_key(invalid_key)
        
        # Sprawdzenie prawidłowego klucza
        self.assertEqual(get_key(valid_key), valid_key.encode())

    def test_rsa_key_format(self):
        from encrypt import generate_rsa_keys
        private_key, public_key = generate_rsa_keys()
        
        # Sprawdzenie, czy klucze są w formacie bajtowym
        self.assertTrue(isinstance(private_key, bytes))
        self.assertTrue(isinstance(public_key, bytes))

    def test_monoalphabetic_key_validation(self):
        from encrypt import validate_mono_key
        valid_key = "qwertyuiopasdfghjklzxcvbnm"  # Poprawny klucz
        invalid_key = "abcde"  # Niepoprawny klucz
        
        # Walidacja poprawnego klucza
        self.assertTrue(validate_mono_key(valid_key))
        
        # Walidacja niepoprawnego klucza
        with self.assertRaises(ValueError):
            validate_mono_key(invalid_key)

if __name__ == "__main__":
    unittest.main()
