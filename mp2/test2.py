from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP
from Crypto.Signature import pkcs1_15
from Crypto.Hash import SHA256
from Crypto.Signature import PKCS1_v1_5

def generate_keypair():
    key = RSA.generate(1024)
    private_key = key.export_key()
    public_key = key.publickey().export_key()
    return private_key, public_key

def encrypt_then_sign(message, public_key_encryption, private_key_signing):
    cipher_rsa = PKCS1_OAEP.new(RSA.import_key(public_key_encryption))
    encrypted_message = cipher_rsa.encrypt(message.encode())

    hash_obj = SHA256.new(encrypted_message)
    signer = PKCS1_v1_5.new(RSA.import_key(private_key_signing))
    signature = signer.sign(hash_obj)

    return encrypted_message, signature

def verify_then_decrypt(encrypted_message, signature, public_key_encryption, public_key_signing):
    verifier = PKCS1_v1_5.new(RSA.import_key(public_key_signing))
    hash_obj = SHA256.new(encrypted_message)

    try:
        verifier.verify(hash_obj, signature)
        cipher_rsa = PKCS1_OAEP.new(RSA.import_key(public_key_encryption))
        decrypted_message = cipher_rsa.decrypt(encrypted_message).decode()
        return decrypted_message
    except (ValueError, TypeError):
        return None

# Example usage
if __name__ == "__main__":
    private_key_encryption, public_key_encryption = generate_keypair()
    private_key_signing, public_key_signing = generate_keypair()
    
    # print(f"PvKE {private_key_encryption} \nPbKE {public_key_encryption}\n")
    # print(f"PvKS {private_key_signing} \nPbKS {public_key_signing}\n")

    message = "Hello"
    print("Original Message:", message)
    print()

    encrypted_message, signature = encrypt_then_sign(message, public_key_encryption, private_key_signing)
    print("Encrypted Message:", encrypted_message)
    print()
    print("Signature:", signature)
    print()

    decrypted_message = verify_then_decrypt(encrypted_message, signature, public_key_encryption, public_key_signing)
    if decrypted_message:
        print("Decrypted Message:", decrypted_message)
    else:
        print("Failed to verify and decrypt the message.")


def decrypt_message(encrypted_message: bytes, private_key: bytes) -> str:
    key = RSA.import_key(private_key)
    cipher = PKCS1_OAEP.new(key)
    decrypted_message = cipher.decrypt(encrypted_message).decode()
    return decrypted_message