class TestValidation(unittest.TestCase):
    def test_aes_key_length(self):
        from gui import get_key
        invalid_key = "short_key"
        valid_key = "a" * 32
        
        with self.assertRaises(ValueError):
            get_key(invalid_key)
        
        self.assertEqual(get_key(valid_key), valid_key.encode())

    def test_rsa_key_format(self):
        from encrypt import generate_rsa_keys
        private_key, public_key = generate_rsa_keys()
        self.assertTrue(isinstance(private_key, bytes))
        self.assertTrue(isinstance(public_key, bytes))

    def test_monoalphabetic_key_validation(self):
        from encrypt import validate_mono_key
        valid_key = "qwertyuiopasdfghjklzxcvbnm"
        invalid_key = "abcde"
        
        self.assertTrue(validate_mono_key(valid_key))
        with self.assertRaises(ValueError):
            validate_mono_key(invalid_key)

if __name__ == "__main__":
    unittest.main()
