from Crypto.Cipher import DES

def decrypt_stream(encrypted_data, key):
    iv = encrypted_data[:8]  
    cipher = DES.new(key, DES.MODE_CFB, iv=iv)
    decrypted_data = b""
    for i in range(8, len(encrypted_data), 8):
        encrypted_block = encrypted_data[i:i+8]
        decrypted_block = cipher.decrypt(encrypted_block)
        decrypted_data += decrypted_block
    return decrypted_data
