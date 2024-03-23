from typing import Union

from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP
from Crypto.Signature import pkcs1_15
from Crypto.Hash import SHA256

def generate_keypair(num_bytes: int) -> tuple[bytes, bytes]:
    if num_bytes < 1024: # RSA modulus length must be >= 1024
        num_bytes = 1024 
    key = RSA.generate(num_bytes)
    private_key = key.export_key()
    public_key = key.publickey().export_key()
    return private_key, public_key

def encrypt_then_sign(message: Union[str, bytes], 
                      pbk_encryption: bytes, 
                      pvk_signing: bytes) -> tuple[bytes, bytes]:
    
    ## Encryption part
    if isinstance(message, str): # Convert string to bytes if it's a string
        message = message.encode()  
    
    key = RSA.import_key(pbk_encryption)
    cipher = PKCS1_OAEP.new(key)
    ciphertext = cipher.encrypt(message)
    
    ## Signature part
    key = RSA.import_key(pvk_signing)
    hash = SHA256.new(ciphertext)
    signature = pkcs1_15.new(key).sign(hash)

    return ciphertext, signature

def verify_then_decrypt(encrypted_message: bytes,
                        signature: bytes,
                        pvk_encryption: bytes,
                        pbk_signing: bytes) -> str:
    
    key = RSA.import_key(pbk_signing)
    hash = SHA256.new(encrypted_message)
    
    try:
        pkcs1_15.new(key).verify(hash, signature)
        # Verified
        key = RSA.import_key(pvk_encryption)
        cipher = PKCS1_OAEP.new(key)
        decrypted_message = cipher.decrypt(encrypted_message).decode()
        return decrypted_message

    except (ValueError, TypeError):
        return "Verification Failed"
    

def main() -> None:
    num_bytes = 1024 # Keep this at >=1024. Idk why it's at min 1024
    private_key_encryption, public_key_encryption = generate_keypair(num_bytes=num_bytes)
    private_key_signing, public_key_signing = generate_keypair(num_bytes=num_bytes)
    
    message = input("Enter message: ")
    if len(message) > 140:
        print("Damn, that's a lot of characters. I'm not running 😩")
        return 

    print(f"Original Message: {message}\n")
    
    encrypted_message, signature = encrypt_then_sign(
        message=message,
        pbk_encryption=public_key_encryption,
        pvk_signing=private_key_signing
    )

    print(f"Encrypted message: {encrypted_message}\n")
    print(f"Signature: {signature}\n")
    
    decrypted_message = verify_then_decrypt(
        encrypted_message=encrypted_message,
        signature=signature,
        pvk_encryption=private_key_encryption,
        pbk_signing=public_key_signing
    )
    
    print(f"Decrypted message: {decrypted_message}\n")

if __name__ == "__main__":
    main()