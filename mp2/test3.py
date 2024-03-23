from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad
from Crypto.Random import get_random_bytes


def generate_keypair(bytes):
    private_key = get_random_bytes(bytes)
    public_key = get_random_bytes(bytes)
    return private_key, public_key

def encrypt_then_sign(message, pbk_encryption, pvk_signing):
    if type(message) != bytes: # Convert to bytes
        message = str.encode(message)
    
    cipher = AES.new(pbk_encryption, AES.MODE_CBC)
    ciphertext = cipher.encrypt(pad(message, AES.block_size))
    
    return ciphertext, None
    

if __name__ == "__main__":
    b = 16
    private_key_encryption, public_key_encryption = generate_keypair(bytes=b)
    private_key_signing, public_key_signing = generate_keypair(bytes=b)
    
    message = "Hello"
    print(f"Original Message: {message}\n")
    
    encrypted_message, signature = encrypt_then_sign(message, public_key_encryption, private_key_signing)

    print(f"Encrypted message: {encrypted_message}\n")