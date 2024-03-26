from typing import Union

from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP
from Crypto.Signature import pkcs1_15
from Crypto.Hash import SHA256


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
        return "Verification Failed. Keys might be different."