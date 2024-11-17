class TestFunctionalEncryptionGUI(unittest.TestCase):
    def test_gui_encrypt_action(self):
        from gui import encrypt_file_action
        import os
        input_path = "test_plain.txt"
        output_path = "test_encrypted_gui.aes"
        
        with open(input_path, 'wb') as f:
            f.write(b"Testowy tekst")

        encrypt_file_action(input_path, output_path, get_random_bytes(32))
        
        self.assertTrue(os.path.exists(output_path))

    def test_gui_decrypt_action(self):
        from gui import decrypt_file_action
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
            
        self.assertEqual(original_content, decrypted_content)

if __name__ == "__main__":
    unittest.main()
