import os
import rsa


class Generator:
    def __init__(self):
        self.key_dir = "mp2/keys"
        self.public_file = "public.pem"
        self.private_file = "private.pem"
        self.message_dir = "mp2/messages"
        self.message_file = "encrypted.message"
        self.public_path = None
        self.private_path = None
        self.message_path = None
        self.public_key = None
        self.private_key = None
        self.sign_dir = "mp2/signatures"
        self.sign_file = "signature"
        self.signature_path = None
    
    def generate_keys(self, bytes=1024) -> None:
        public_key, private_key = rsa.newkeys(bytes)
        self.public_path = os.path.join(self.key_dir, self.public_file)
        self.private_path = os.path.join(self.key_dir, self.private_file)

        with open(self.public_path, "wb") as f:
            f.write(public_key.save_pkcs1("PEM"))
            
        with open(self.private_path, "wb") as f:
            f.write(private_key.save_pkcs1("PEM"))  
        
        print("Keys generated")
        self.set_keys()
    
    def generate_messages(self, message) -> None:
        self.message_path = os.path.join(self.message_dir, self.message_file)

        encrypted_message = rsa.encrypt(message.encode(), self.public_key)

        with open(self.message_path, "wb") as f:
            f.write(encrypted_message)
        
        print("Message generated")
    
    def set_keys(self) -> None:
        with open(self.public_path, "rb") as f:
            public_key = rsa.PublicKey.load_pkcs1(f.read())
            
        with open(self.private_path, "rb") as f:
            private_key = rsa.PrivateKey.load_pkcs1(f.read())
        
        self.public_key = public_key
        self.private_key = private_key
            
        print("Keys set")
        


class IDK:
    def __init__(self, generator:Generator):
        self.generator = generator
    
    def __str__(self):
        # return f"{self.public_key.data} | {self.private_key.data}"
        return f"{self.public_key} | {self.private_key}"
    
    def get_message(self) -> bytes:  
        # with open(self.generator.private_path, "rb") as f:
        #     private_key = rsa.PrivateKey.load_pkcs1(f.read())

        encrypted_message = open(self.generator.message_path, "rb").read()

        clear_message = rsa.decrypt(encrypted_message, 
                                    self.generator.private_key)

        # print(clear_message.decode())
        return clear_message

    def sign_message(self, message) -> None:
        hash_alg = "SHA-256"
        signature = rsa.sign(message.encode(), 
                             self.generator.private_key, 
                             hash_alg)
        
        self.generator.signature_path =\
            os.path.join(self.generator.sign_dir, 
                        self.generator.sign_file)
        
        with open(self.generator.signature_path, "wb") as f:
            f.write(signature)
        
        print("Signed")
    
    def verify_message(self, message) -> None:
        with open(self.generator.signature_path, "rb") as f:
            signature = f.read()
        
        # print(f"Verified? {flag}")   
        try:
            flag = rsa.verify(message.encode(), signature, 
                          self.generator.public_key)     
            
            print(f"Verified message with: {flag}")
        except rsa.VerificationError:
            print("Verification failed!")
            


if __name__ == "__main__":
    # Generate keys and messages
    generator = Generator()
    _bytes = 1024
    generator.generate_keys(_bytes)
    message = "Hello World!"
    generator.generate_messages(message)
    
    # Get message
    idk = IDK(generator)
    clear_message = idk.get_message()
    print(clear_message.decode())
    
    # Sign message
    message_2 = "This is a new message"
    idk.sign_message(message_2)
    
    # Verify message
    # message_2 = "This is a new message"
    message_2 = "This is a new message"
    idk.verify_message(message_2)
    
    # New keys
    generator.generate_keys(_bytes)
    # Verifying the same message will result in verification failed
    message_2 = "This is a new message"
    idk.verify_message(message_2)
    