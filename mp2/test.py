from Crypto.Random import get_random_bytes
from Crypto.Protocol.KDF import PBKDF2
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad

# simple_key = get_random_bytes(32)
# print(simple_key)

salt = b'W\xeaIg\xf5\x90\x138\x19\xad8Q\x85\xd5\xa1\x8e\xfa\xea\xa2\xb2\xfa\x8fsflmVv{\xe2)\xb9'
password = "mypassword"

key = PBKDF2(password, salt, dkLen=32)

message = b"Hello"

cipher = AES.new(key, AES.MODE_CBC)
ciphered_data = cipher.encrypt(pad(message, AES.block_size))


with open('encrypted.bin', 'wb') as f:
    f.write(cipher.iv)
    f.write(ciphered_data)
    
with open('encrypted.bin', 'rb') as f:
    iv = f.read(16)
    decrypt_data = f.read()
    
cipher = AES.new(key, AES.MODE_CBC, iv=iv)
original = unpad(cipher.decrypt(decrypt_data), AES.block_size)

print(original)

with open('key.bin', 'wb') as f:
    f.write(key)
