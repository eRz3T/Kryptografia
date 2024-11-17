class TestIntegrationAESRSA(unittest.TestCase):
    def test_hybrid_encryption(self):
        from encrypt import encrypt_file_hybrid
        from decrypt import decrypt_file_hybrid
        from encrypt import generate_rsa_keys
        public_key, private_key = generate_rsa_keys()
        input_path = "test_plain.txt"
        encrypted_path = "test_hybrid_encrypted.aes"
        decrypted_path = "test_decrypted.txt"
        
        with open(input_path, 'wb') as f:
            f.write(b"Testowy tekst")

        encrypt_file_hybrid(input_path, encrypted_path, public_key)
        decrypt_file_hybrid(encrypted_path, decrypted_path, private_key)
        
        with open(input_path, 'rb') as f:
            original_content = f.read()
        with open(decrypted_path, 'rb') as f:
            decrypted_content = f.read()
        
        self.assertEqual(original_content, decrypted_content)

    def test_diffie_hellman_key_exchange(self):
        from diffie_hellman.simulation import generate_shared_key
        alice_public, alice_private = generate_shared_key()
        bob_public, bob_private = generate_shared_key()
        alice_shared = generate_shared_key(bob_public, alice_private)
        bob_shared = generate_shared_key(alice_public, bob_private)
        self.assertEqual(alice_shared, bob_shared)

if __name__ == "__main__":
    unittest.main()
