from Crypto.Cipher import AES

def decrypt_stream(encrypted_data, key):
    iv = encrypted_data[:16]  # Pobieranie IV z początku danych
    cipher = AES.new(key, AES.MODE_CFB, iv=iv)
    decrypted_data = cipher.decrypt(encrypted_data[16:])
    return decrypted_data
