import os
import re

from Crypto.PublicKey import RSA

def generate_keypair(num_bytes: int = 1024,
                     store: bool = True,
                     type: str = "encryption") -> tuple[bytes, bytes]:
    """Generates a private and public keypair

    Args:
        num_bytes (int, optional): The number of bytes of the key. Defaults to 1024.
        store (bool, optional): Stores the keypairs in their respective directories

    Returns:
        tuple[bytes, bytes]: Returns a private and public keypair
    """
    
    if num_bytes < 1024: # RSA modulus length must be >= 1024
        num_bytes = 1024 
        
    key = RSA.generate(num_bytes)
    private_key = key.export_key()
    public_key = key.publickey().export_key()
    
    if store:
        folder_name = "keys"
        if not os.path.exists(folder_name):
            os.makedirs(folder_name)
        
        priv_path = os.path.join(folder_name, "private")
        pub_path = os.path.join(folder_name, "public")
        
        if not os.path.exists(priv_path):
            os.makedirs(priv_path)
        if not os.path.exists(pub_path):
            os.makedirs(pub_path)
            
        files = os.listdir(priv_path)
        # n = len(files) + 1
        
        # Filter files of the same type
        type_files = [file for file in files if file.startswith(type)]
        n = len(type_files) + 1

        priv_filename = f"{type}_{n}.pem"
        pub_filename = f"{type}_{n}.pem"
            
        with open(os.path.join(priv_path, priv_filename), "wb") as f:
            f.write(private_key)
        with open(os.path.join(pub_path, pub_filename), "wb") as f:
            f.write(public_key)

    return private_key, public_key

def delete_files(file_num: int = 0) -> list[str]:
    """Deletes the corresponding private and public key pairs identified by a file number.

    Args:
        file_num (int, optional): A positive integer uniquely identifying the keypair to be deleted.
        Defaults to 0, which deletes all the keypairs.
    """
    
    folder_name = "keys"

    if not os.path.exists(folder_name):
        print("Folder not found.")
        return
    
    if file_num == 0:
        for key_dir in os.listdir(folder_name):
            path = os.path.join(folder_name, key_dir)
            
            for filename in os.listdir(path):
                os.remove(os.path.join(path, filename))
        # print("Deleted all files.")
        return ["Deleted all files."]

    deleted_list = []
    for key_dir in os.listdir(folder_name):
        path = os.path.join(folder_name, key_dir)

        for filename in os.listdir(path):
            # Match the pattern 'type_number.pem'
            match = re.match(r'(encryption|signing)_(\d+)\.pem', filename)
            if match:
                if int(match.group(2)) == file_num:
                    os.remove(os.path.join(path, filename))
                    # print(f"Deleted: {path}\{filename}")
                    deleted_list.append(f"Deleted: {path}\{filename}")
                    
    return deleted_list