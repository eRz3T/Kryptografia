from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP, AES

def decrypt_text_rsa(encrypted_text, private_key):
    key = RSA.import_key(private_key)
    cipher = PKCS1_OAEP.new(key)
    decrypted_text = cipher.decrypt(encrypted_text).decode()
    return decrypted_text

def decrypt_file_hybrid(input_path, output_path, private_key):
    with open(input_path, 'rb') as f:
        encrypted_aes_key = f.read(256)  
        iv = f.read(16)                 
        encrypted_data = f.read()        

    rsa_key = RSA.import_key(private_key)
    rsa_cipher = PKCS1_OAEP.new(rsa_key)
    aes_key = rsa_cipher.decrypt(encrypted_aes_key)

    aes_cipher = AES.new(aes_key, AES.MODE_CFB, iv=iv)
    decrypted_data = aes_cipher.decrypt(encrypted_data)

    with open(output_path, 'wb') as f:
        f.write(decrypted_data)

def decrypt_file_rsa(input_path, output_path, private_key):
    with open(input_path, 'rb') as f:
        encrypted_data = f.read()

    rsa_key = RSA.import_key(private_key)
    rsa_cipher = PKCS1_OAEP.new(rsa_key)
    decrypted_data = rsa_cipher.decrypt(encrypted_data)

    with open(output_path, 'wb') as f:
        f.write(decrypted_data)
