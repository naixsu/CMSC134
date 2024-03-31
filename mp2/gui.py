import os
import customtkinter
# https://github.com/TomSchimansky/CustomTkinter/blob/master/examples/complex_example.py
# https://github.com/TomSchimansky/CustomTkinter/blob/master/examples/scrollable_frame_example.py

from generate_keypairs import generate_keypair, delete_files
from functions import encrypt_then_sign, verify_then_decrypt

customtkinter.set_appearance_mode("System")  # Modes: "System" (standard), "Dark", "Light"
customtkinter.set_default_color_theme("blue")  # Themes: "blue" (standard), "green", "dark-blue"


class ScrollableButtonFrame(customtkinter.CTkScrollableFrame):
    def __init__(self, master, type, **kwargs):
        super().__init__(master, **kwargs)
        self.textbox = None
        self.type = type
        self.button_list = []
        self.button_contents = None
    
    def init_textbox(self, textbox):
        self.textbox = textbox
    
    def init_items(self, item_list, type):
        # Too lazy to add the latest file in the list so imma just reuse this
        # function and remove everything on the list and add it back in
        # stonks
        if item_list:
            for item in item_list:
                self.remove_item(item)
                
        # type_files = [file for file in files if file.startswith(type)]
        for item in item_list:
            if item.startswith(type):
                self.add_item(item)

    def add_item(self, item):
        btn = customtkinter.CTkButton(self, text=item)
        btn.configure(command=lambda btn=btn: self.button_on_click(btn))
        btn.grid(row=len(self.button_list), column=0, padx=5, pady=5, sticky="nsew")
        self.button_list.append(btn)

    def remove_item(self, item):
        for btn in self.button_list:
            if item == btn.cget("text"):
                btn.destroy()
                self.button_list.remove(btn)
                return
    
    def button_on_click(self, btn):
        
        def _reset_buttons():
            for button in self.button_list:
                button.configure(state="normal")
        
        _reset_buttons()
        
        btn.configure(state="disabled")
        
        self.textbox.configure(state="normal") # set normal so it can be edited
        self.textbox.delete("0.0", "end")  # delete all text
        item = btn.cget("text")
        
        folder_name = "keys"
        path = os.path.join(folder_name, self.type)
        file_path = os.path.join(path, item)
        
        if os.path.exists(file_path):
            with open(file_path, "r") as file:
                file_contents = file.read()
            
            self.button_contents = file_contents
        
            self.textbox.insert("0.0", file_contents)
        self.textbox.configure(state="disabled") # set back to disabled for readonly
        

    def delete_item(self, file_num):
        if file_num == 0:
            for btn in self.button_list:
                btn.destroy()
                # self.button_list.remove(btn)
            self.button_list = []
            return
        
        for btn in self.button_list:
            btn_text = btn.cget("text")
            num = btn_text.split("_")[-1].split(".")[0]
            if file_num == int(num):
                btn.destroy()
                self.button_list.remove(btn)
                return

class App(customtkinter.CTk):
    def __init__(self):
        super().__init__()

        # configure window
        self.title("RSA Thingy.py")
        self.textbox_width = 300
        self.sidebar_width = 200
        self.scrollable_width = 200
        # self.geometry(f"{1100}x{580}")
        self.geometry(f"{1440}x{850}")

        # configure grid layout (4x4)
        # self.grid_columnconfigure(1, weight=1)
        # self.grid_columnconfigure((2, 3), weight=0)
        self.grid_columnconfigure(5, weight=1)
        self.grid_rowconfigure((2, 1), weight=1)
        
        # create sidebar frame with widgets
        self.sidebar_frame = customtkinter.CTkFrame(self, corner_radius=0)
        self.sidebar_frame.grid(row=0, column=0, rowspan=8, sticky="nsew")
        self.logo_label = customtkinter.CTkLabel(self.sidebar_frame, text="Button Thingies", font=customtkinter.CTkFont(size=20, weight="bold"))
        self.logo_label.grid(row=0, column=0, padx=20, pady=(20, 10))

        self.bytes_entry = customtkinter.CTkEntry(self.sidebar_frame, width=self.sidebar_width, placeholder_text="Bytes")
        self.bytes_entry.grid(row=1, column=0, padx=20, pady=(10, 5))
        
        self.generate_encryption_button = customtkinter.CTkButton(self.sidebar_frame, width=self.sidebar_width, text="Encryption", command=self.sidebar_generate_encryption)
        self.generate_encryption_button.grid(row=2, column=0, padx=20, pady=(10, 5))
        
        self.generate_signing_button = customtkinter.CTkButton(self.sidebar_frame, width=self.sidebar_width, text="Signing", command=self.sidebar_generate_signing)
        self.generate_signing_button.grid(row=3, column=0, padx=20, pady=(10, 5))
        
        self.file_num_entry = customtkinter.CTkEntry(self.sidebar_frame, width=self.sidebar_width, placeholder_text="File Number")
        self.file_num_entry.grid(row=10, column=0, padx=20, pady=(30, 5))
        
        self.delete_keypairs_button = customtkinter.CTkButton(self.sidebar_frame, width=self.sidebar_width, text="Delete Files", command=self.sidebar_delete_files)
        self.delete_keypairs_button.grid(row=11, column=0, padx=20, pady=(10, 5))
        
        self.text_entry = customtkinter.CTkTextbox(self.sidebar_frame, width=self.sidebar_width, height=100)
        self.text_entry.grid(row=6, column=0, padx=20, pady=(15, 5))
        self.text_entry.insert("0.0", "Text goes here")
        
        # self.sign_button = customtkinter.CTkButton(self.sidebar_frame, width=self.sidebar_width, text="Encrypt then Sign", command=self.sidebar_encrypt_then_sign)
        # self.sign_button.grid(row=7, column=0, padx=20, pady=(10, 5))
        # self.sign_button.configure(state="disabled") # disable initially
        self.verify_button = customtkinter.CTkButton(self.sidebar_frame, width=self.sidebar_width, text="Verify", command=self.sidebar_verify_then_decrypt)
        self.verify_button.grid(row=8, column=0, padx=20, pady=(10, 5))
        self.verify_button.configure(state="disabled") # disable initially
        
        self.message_text = """1. Enter a value for Bytes, generate the Encryption and Signing keys by pressing the respective buttons.\n
2. Select the desired keys to use, presented in the main window.\n
3. Enter a message to encrypt and sign.\n
4. Click verify to test out the encryption and decryption considering the selected keys."""
        self.message = customtkinter.CTkLabel(self.sidebar_frame, width=self.sidebar_width, height=90, wraplength=self.sidebar_width, text=self.message_text, justify="left")
        self.message.grid(row=9, column=0, padx=20, pady=(15, 5))
        
        ## Bottom Panel Frame
        self.bottom_panel_frame = customtkinter.CTkFrame(self, corner_radius=0)
        self.bottom_panel_frame.grid(row=11, column=0, columnspan=5, sticky="nsew")
        
        
        self.logs_textbox = customtkinter.CTkTextbox(self.bottom_panel_frame, width=1400, height=150)
        self.logs_textbox.grid(row=0, column=0, padx=20, pady=(15, 5), sticky="nsew")
        self.logs_textbox.insert("0.0", "Logs go here")
        self.logs_textbox.configure(state="disabled")
        
        
        ## Column 1
        self.logo_label_2 = customtkinter.CTkLabel(self, text="Encryption Keys", font=customtkinter.CTkFont(size=20, weight="bold"))
        self.logo_label_2.grid(row=0, column=1, padx=10, pady=(20, 10))
        self.encryption_private = ScrollableButtonFrame(self, type="private", label_text="Private", width=self.scrollable_width, corner_radius=0)
        self.encryption_private.grid(row=1, column=1, padx=15, pady=15, sticky="nsew")
        self.encryption_public = ScrollableButtonFrame(self, type="public", label_text="Public", width=self.scrollable_width, corner_radius=0)
        self.encryption_public.grid(row=2, column=1, padx=15, pady=15, sticky="nsew")
        
        ## Column 2
        self.logo_label_3 = customtkinter.CTkLabel(self, text="Preview", font=customtkinter.CTkFont(size=20, weight="bold"))
        self.logo_label_3.grid(row=0, column=2, padx=10, pady=(20, 10))
        
        ## Create textboxes
        ## Encryption
        self.textbox_encryption_private = customtkinter.CTkTextbox(self, width=self.textbox_width)
        self.textbox_encryption_private.grid(row=1, column=2, padx=15, pady=15, sticky="nsew")
        self.textbox_encryption_public = customtkinter.CTkTextbox(self, width=self.textbox_width)
        self.textbox_encryption_public.grid(row=2, column=2, padx=15, pady=15, sticky="nsew")

        ## Column 3
        self.logo_label_4 = customtkinter.CTkLabel(self, text="Signing Keys", font=customtkinter.CTkFont(size=20, weight="bold"))
        self.logo_label_4.grid(row=0, column=3, padx=10, pady=(20, 10))
        self.signing_private = ScrollableButtonFrame(self, type="private", label_text="Private", width=self.scrollable_width, corner_radius=0)
        self.signing_private.grid(row=1, column=3, padx=15, pady=15, sticky="nsew")
        self.signing_public = ScrollableButtonFrame(self, type="public", label_text="Public", width=self.scrollable_width, corner_radius=0)
        self.signing_public.grid(row=2, column=3, padx=15, pady=15, sticky="nsew")
        
        ## Column 4
        self.logo_label_5 = customtkinter.CTkLabel(self, text="Preview", font=customtkinter.CTkFont(size=20, weight="bold"))
        self.logo_label_5.grid(row=0, column=4, padx=10, pady=(20, 10))
        self.textbox_signing_private = customtkinter.CTkTextbox(self, width=self.textbox_width)
        self.textbox_signing_private.grid(row=1, column=4, padx=15, pady=15, sticky="nsew")
        self.textbox_signing_public = customtkinter.CTkTextbox(self, width=self.textbox_width)
        self.textbox_signing_public.grid(row=2, column=4, padx=15, pady=15, sticky="nsew")
        
        # ## Set Default Values
        self.init_keys()
        self.init_textboxes()
    
        ## Binds     
        self.bytes_entry.bind("<KeyRelease>", self.update_bytes_entry_button_states)
        self.file_num_entry.bind("<KeyRelease>", self.update_file_num_button_states)
        self.bind("<Button-1>", self.update_verify_button_states)

        # Disable initially
        self.generate_encryption_button.configure(state="disabled")
        self.generate_signing_button.configure(state="disabled")
        # self.delete_keypairs_button.configure(state="disabled")
        
    def init_textboxes(self):
        self.encryption_private.init_textbox(self.textbox_encryption_private)
        self.encryption_public.init_textbox(self.textbox_encryption_public)
        self.signing_private.init_textbox(self.textbox_signing_private)
        self.signing_public.init_textbox(self.textbox_signing_public)
        
    
    def init_keys(self):
        priv = "keys\private"
        if not os.path.exists(priv):
            os.makedirs(priv)
            
        pub = "keys\public"
        if not os.path.exists(pub):
            os.makedirs(pub)
        
        priv_files = os.listdir(priv)
        pub_files = os.listdir(pub)
        
        # self.scrollable_private.init_items(priv_files)
        # self.scrollable_public.init_items(pub_files)
        self.encryption_private.init_items(priv_files, type="encryption")
        self.signing_private.init_items(priv_files, type="signing")
        self.encryption_public.init_items(pub_files, type="encryption")
        self.signing_public.init_items(pub_files, type="signing")
        
    def update_verify_button_states(self, type, event=None):
        if None in [self.encryption_private.button_contents, self.encryption_public.button_contents, self.signing_private.button_contents, self.signing_public.button_contents]:
            self.verify_button.configure(state="disabled")
        else:
            self.verify_button.configure(state="normal")
            

    def update_file_num_button_states(self, type, event=None):
        entry = self.file_num_entry.get()
    
        if not entry.isdigit():
            self.delete_keypairs_button.configure(state="disabled")
        else:
            self.delete_keypairs_button.configure(state="normal")
                
    def update_bytes_entry_button_states(self, type, event=None):
        entry = self.bytes_entry.get()
    
        if not entry.isdigit():
            self.generate_encryption_button.configure(state="disabled")
            self.generate_signing_button.configure(state="disabled")
        else:
            self.generate_encryption_button.configure(state="normal")
            self.generate_signing_button.configure(state="normal")
            
    def is_rsa_keyl_invalid(self, input:str):
        if not input: # no input
            return True
        
        # test if valid int and less than 1024
        try:
            x = int(input)
            if x < 1024:
                return True
            else:
                return False
        except:
            return True

    def sidebar_generate_encryption(self):
        if self.is_rsa_keyl_invalid(self.bytes_entry.get()):
            num_bytes = 1024
            self.logs = {
                "status": "Warning",
                "warning_message": "RSA key length should be >=1024; Using 1024 RSA key length for generating Encryption Key."
            }
            self.update_logs()
            
        else:
            num_bytes = int(self.bytes_entry.get())
            self.logs = {
                "status": "Success",
                "message": "Generated encryption key with RSA key length " + str(num_bytes)
            }
            self.update_logs()

        generate_keypair(num_bytes=num_bytes, type="encryption")
        self.init_keys()
    
    def sidebar_generate_signing(self):
        if self.is_rsa_keyl_invalid(self.bytes_entry.get()):
            num_bytes = 1024
            self.logs = {
                "status": "Warning",
                "warning_message": "RSA key length should be >=1024; Using 1024 RSA key length for generating Signing Key."
            }
            self.update_logs()
            
        else:
            num_bytes = int(self.bytes_entry.get())
            self.logs = {
                "status": "Success",
                "message": "Generated signing key with RSA key length " + str(num_bytes)
            }
            self.update_logs()

        generate_keypair(num_bytes=num_bytes, type="signing")
        self.init_keys()
    
    def sidebar_delete_files(self):
        if not self.file_num_entry.get():
            file_num = 0
        else:
            file_num = int(self.file_num_entry.get())
        
        try:
            logs = delete_files(file_num=file_num)
            self.logs = {
                "status": "Success",
                "message": logs
            }
            self.update_logs()
        
        except Exception as e:
            self.logs = {
                "status": "Error",
                "error_message": str(e),
            }
            self.update_logs()
        
        self.encryption_private.delete_item(file_num=file_num)
        self.encryption_public.delete_item(file_num=file_num)
        self.signing_private.delete_item(file_num=file_num)
        self.signing_public.delete_item(file_num=file_num)
        
        

    def sidebar_encrypt_then_sign(self):
        # message = self.text_entry.get("0.0", "end")
        # Get the text from the text entry widget, excluding the trailing newline
        message = self.text_entry.get("1.0", "end-1c")
        pbk_encryption = self.encryption_public.button_contents
        pvk_signing = self.signing_private.button_contents
        
        try:
            encrypted_message, signature = encrypt_then_sign(
                message=message,
                pbk_encryption=pbk_encryption,
                pvk_signing=pvk_signing
            )
            self.logs = {
                "status": "Success",
                "encrypted_message": encrypted_message,
                "signature": signature,
            }
            # self.update_logs()
            return encrypted_message, signature
            
        except Exception as e:
            self.logs = {
                "status": "Error",
                "error_message": str(e),
            }
            self.update_logs()
    
    def sidebar_verify_then_decrypt(self):
        encrypted_message, signature = self.sidebar_encrypt_then_sign()
        pvk_encryption = self.encryption_private.button_contents
        pbk_signing = self.signing_public.button_contents
        

        try:
            decrypted_message = verify_then_decrypt(encrypted_message=encrypted_message,
                                signature=signature,
                                pvk_encryption=pvk_encryption,
                                pbk_signing=pbk_signing)
            
            self.logs = {
                "status": "Success",
                "decrypted_message": decrypted_message,
                **self.logs,
            }
        
        except Exception as e:
            self.logs = {
                "status": "Error",
                "error_message": str(e),
            }
        
        self.update_logs()
    
    def update_logs(self):
        self.logs_textbox.configure(state="normal")
        self.logs_textbox.delete("0.0", "end")  # delete all text
        
        if not self.logs:
            self.logs_textbox.insert("0.0", "Logs go here")
            return
        
        if self.logs["status"] == "Warning":
            self.logs_textbox.insert("0.0", self.logs["warning_message"])
        elif self.logs["status"] == "Success":
            line_num = 0
            for key, value in self.logs.items():
                if value == "Success":
                    continue
                if value is not None:
                    message = f"{key.capitalize().replace('_', ' ')}: {value}\n"
                    self.logs_textbox.insert(f"{line_num}.0", message) # insert at line line_num character 0
                    line_num += 1
                
        elif self.logs["status"] == "Error":
            self.logs_textbox.insert("0.0", self.logs["error_message"])     
        
if __name__ == "__main__":
    app = App()
    app.mainloop()