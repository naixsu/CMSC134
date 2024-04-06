# Machine Problem 2

## Objectives

- Write a program that encrypts and decrypts a message using RSA-OAEP with authenticity
- Use the encrypt-then-sign scheme for authenticated encryption
- Use a separate key for encryption and signing
- Make use of cryptographic libraries

---

The machine problem is implemented in two forms:

- Graphical User Interface `gui.py` 
How to use GUI
    - Interactive application of the machine problem.
    - Allows for reuse of encryption and signing keys.
    - Allows for different RSA key sizes.
- Command Line Interface `mp2.py`
Explaining the process of encryption & signing, verifying & decryption
    - Simple testing of RSA-1024 encryption and SHA265 hashing.
    - New encryption and signing keys are used when the program is run.

# Graphical User Interface

![Untitled](mp2_writeup/Untitled.png)

To get the program to work, all you have to do is run the program in the terminal or in your preferred IDE; because an intuitive GUI was made.

```bash
python ./gui.py
```

The instructions are laid out on the left part of the interface but let’s explain it part by part. 

![Untitled](mp2_writeup/Untitled%201.png)

Input the number of bytes, the minimum value is 1024. This would be the RSA key length. After doing so, clicking `Encryption`/`Signing` will generate their respective private and public keys which go on the neighboring column. Clicking the `_#.pem` file will preview the respective key.

![Untitled](mp2_writeup/Untitled%202.png)

![Untitled](mp2_writeup/Untitled%203.png)

After selecting the respective keys, place a message to be encrypted in the “Text goes here” box. To perform the encryption/decryption, simply go back to the Button Thingies tab and click `Verify`.

Finally, the encrypted message and the decrypted message will show up in the log at the very bottom of the interface.

![Untitled](mp2_writeup/Untitled%204.png)

You may test out the same keys by clicking verify, change the encryption keys, signing keys, and or message. 

## Managing Keys

Enter the key number of the keys you want to delete in the text field File Number. 
Clicking `Delete Files` would delete all the keys with the corresponding file number.

![Untitled](mp2_writeup/Untitled%205.png)

To delete all the keys, use File Number `0` to remove all the keys. The keys may be found in the directory `./keys`

---

# Command Line Interface

- Explaining the process of encryption & signing, verifying & decryption

The program can be run using the terminal or any IDE

```bash
python ./mp2.py
```

The program would require an input for the message. Then the following would be performed:

## RSA Key Generation

Two pairs of asynchronous RSA keys are generated. One for encryption and the other for signing. Both operations would use the same RSA key length 1024; following the FIPS.

## Encrypting and Signing

Then the message is encrypt-then-sign; which involves the following steps. A cipher is generated based on the encryption key provided. Then using this cipher, the message is encrypted utilizing the Optimal Asymmetric Encryption Padding, resulting to the ciphertext.

After that, the resulting ciphertext is then signed using a signing key. First, the ciphertext is hashed using the SHA256 algorithm. Then using the hash and provided signing key, the signature is calculated.

## Verifying and Decrypting

Having received the ciphertext and signature. 

First, verifying the ciphertext. The hash of the ciphertext is calculated using SHA256. Then a comparison between the calculated hash and signature would be performed. When it is verified, the message is decrypted. Using the decryption key, a cipher is generated and used in decrypting the message.

When authentication fails (received signature does not match with the calculated hash). The message isn’t decrypted.

---

## Sample Input/Files

### Command Line Interface (mp2.py)

```markdown
> Enter message: your mom
### Generation of encryption and signing key pairs
+------------+------------------------------------------------------------------+------------------------------------------------------------------+
| Purpose    | Private Key                                                      | Public Key                                                       |
+============+==================================================================+==================================================================+
| Encryption | -----BEGIN RSA PRIVATE KEY-----                                  | -----BEGIN PUBLIC KEY-----                                       |
|            | MIICXAIBAAKBgQC4ANz9ihoH8ntq/sXN6Qh6j65OaafR3O08WFAjTmkg+z8VG5+F | MIGfMA0GCSqGSIb3DQEBAQUAA4GNADCBiQKBgQC4ANz9ihoH8ntq/sXN6Qh6j65O |
|            | vmx2MCzCL8hr7SkC/ynbVLc0NGxu3pJK3dVS06GPT0DYNkPFQUtMAiWBOqpJu53y | aafR3O08WFAjTmkg+z8VG5+Fvmx2MCzCL8hr7SkC/ynbVLc0NGxu3pJK3dVS06GP |
|            | 6Y1Czox5N56n1bdLK/O65w5Nnmfy6r4OjBJve21f+jL19/gtHjErppcRFwIDAQAB | T0DYNkPFQUtMAiWBOqpJu53y6Y1Czox5N56n1bdLK/O65w5Nnmfy6r4OjBJve21f |
|            | AoGAWYUN/woL3RbzRZxbBvFbjylNH9gWbitCfivnHS4+Rm4GBFJym2KIKT4J4JXX | +jL19/gtHjErppcRFwIDAQAB                                         |
|            | t+5jmBIlPpCqKytgH9aILQVdDYFfoYf1iJLrfpb09CcIRhWXWCDwvZ7tpsKpG33F | -----END PUBLIC KEY-----                                         |
|            | umcXgXiVcbcBE8KnaIy5hZuTkNj61zT7uRUb0oR7QqG3nH0CQQDGXKAreccqZd7A |                                                                  |
|            | DKYkRqej4UaUzWizaVmhV0DLI0sL3L3ZHyZ9XW25TgJdxyQMeJbpjZsw4aW2e7mw |                                                                  |
|            | Vjk/pxSDAkEA7Xgq9oSJx0t0rKUf+sNtEP6wM7K6UNWeZnOZsBJ0U68WL1Cb6IfH |                                                                  |
|            | t8Kkl2bQL8qgbDybNbGACaEZIPaocoV03QJAGNTHiCm6cOhHtirfMXNW0QEGYOJF |                                                                  |
|            | 1Q+/FJ9jkQpd/qInceKgYtkrPyMw0KR5MsZ1vc7oOnpE0E80s4pXqEw2GQJBAKy/ |                                                                  |
|            | XSml8wCawI6TNLdcEOxrCk0heG4zaB6Je8TdN+hklxPmZPR8SepA2zEUZuBNW/RB |                                                                  |
|            | BnvB2y2mFrynEpT0xrUCQGOa4nFrReLn9rIQ8QkW+BD2037gWgg6Xe7OuqCzwThQ |                                                                  |
|            | yhFAD5xQfyOer6Ukec4grzUZZOCf70YBA78nyEhSSjY=                     |                                                                  |
|            | -----END RSA PRIVATE KEY-----                                    |                                                                  |
+------------+------------------------------------------------------------------+------------------------------------------------------------------+
| Signing    | -----BEGIN RSA PRIVATE KEY-----                                  | -----BEGIN PUBLIC KEY-----                                       |
|            | MIICWwIBAAKBgQCx94FLARdCIimJrc4Lo9QefOYjX0BYceytuLJsfYQ1u9YEayZd | MIGfMA0GCSqGSIb3DQEBAQUAA4GNADCBiQKBgQCx94FLARdCIimJrc4Lo9QefOYj |
|            | MpU8wkpLmi9KpruZ3uLd5VRF97Z7yFyJTd1BOHKM48Hw/foW5SFladyx7bGJWhPN | X0BYceytuLJsfYQ1u9YEayZdMpU8wkpLmi9KpruZ3uLd5VRF97Z7yFyJTd1BOHKM |
|            | lRx3pRz1ZjdUM2KwSLe74VsehVi/Ise1mij42nJoGWduI3n+338GBwwiqQIDAQAB | 48Hw/foW5SFladyx7bGJWhPNlRx3pRz1ZjdUM2KwSLe74VsehVi/Ise1mij42nJo |
|            | AoGABsNxQSMkJHnyj4ObdmBzifUVNKLvacJqoZozWGGCH3NUCYxI7kx4f3v4IYdq | GWduI3n+338GBwwiqQIDAQAB                                         |
|            | j1u8JXeNslZ/gr6MoN0B0fYI7TFIaArORoaZMTWJlPj251nm71GEnpaDzXdzP0q3 | -----END PUBLIC KEY-----                                         |
|            | urJzjwaMvah7iwFW4xO8evDLozqOwIpjNGjATQtwr7/6ZQECQQC+NzgbqXeUIPa5 |                                                                  |
|            | IHmyplkJV3kZ9VD3WVV57dHiRh064BkDXdiLLJk1PzeeQ7HRjqb3cbYrfVzRQAkf |                                                                  |
|            | l1rqKrClAkEA74PULWhfJecfwRiCNBKu35goDLvNsuVCc3hzNe1efVlTWp36Xxpt |                                                                  |
|            | g28jwNxoYWrDRXizuxjJYIsLBKkfQjXmtQJAc2Nz+fPXwlgs0yjMKn+Wy3/wyrpy |                                                                  |
|            | H1pl681E4Qq/eJOxGMW5MtQfLJno120hVYo/5yNn6wHlaFp8LlnWoO68sQJAAux5 |                                                                  |
|            | CpTblHrdyF2kOT6BI/mXg5BHUoe55+7weRgMrzsH6XNEOyT3cUNKDHCkVYwYFiED |                                                                  |
|            | EKWcz7Di0Yu+9e/ygQJAE1C2QeOYP3f0f9sEWFOMBPYraFuWI952y3uLySK0kKar |                                                                  |
|            | HFWXYwaU0GyRS9LXFOrESKSgxmYMgtKvJ+LpGklOVQ==                     |                                                                  |
|            | -----END RSA PRIVATE KEY-----                                    |                                                                  |
+------------+------------------------------------------------------------------+------------------------------------------------------------------+

### encrypt_then_sign() returns the cipertext and signature
> Encrypted message: b'$\xa4\x15c$D\x03?\x85\xed}\x1b\x80\xf6D\xbbk\xd7c \xda\xceU\x9fK\xa5\x05\xe0`*"6\xde\x0b\xb5\xe6u\xc3\xa58%Y\xcf\xe2~\xdb5\\qd\xf2\xdb\xbf\xa2\x03\'tv\xb8xL=\x9cb\x85\xd0%\x0c\xadSk<\xb1\xe1\xb1\xae,So\x8f\x06\x1bLH\rpUi\x82\xebf\r\xfb\xd8\xfb=\x1cNlJ\x05D\xcc<\xd9|6\x03u4(\x88\x99\x85\xde\xd2J\xf9\x9bK\xcc\x0f\xc0z\xc7-l\xd2'
> Signature: b'.\xbb\x80\xf8v\xc2\x97\x8b\xa5\xc5\xc7~\xd5UKA.g\xb7\x04\xbb\x10i\x8f\x979\xbf\x9f$\xde\x10g\xaa\x9c^\xef4\xbcz\x18^\xfc\x04\x99\xbf\xdd\xa2\xbe\xf7?\xb1i\x10\xd8B\xe4E\xc6\x11\xd0\xfd<`\\\xfcjL\xaa\xba\xdb\xd2\xe2\x8d\xb2\x1b\xc8\x0b\xff\xe2\x02\xf0z\xf8\xb1\xa1\xb7<\xe2\xbd\x01\xa0\xf9\x80\xe3\x94:\xa8d\xc4\xb5\xaa\xb3Z\x15\xb3\x85m\xb5L>\xf7\x9e@h\x9e4EfX\xb9\x11)\xa1\x10(\x12\xd1\xca'

### verify_then_decrypt() returns the decrypted message after verifying the hash values
> Decrypted message: your mom
```

Input 2
```
> Enter message: Naname nanajyuunana-do no narabi de nakunaku inanaku nanahan nanadai nannaku narabete naganagame. Nyanyame nyanyajyuunyanya-do no nyarabi de nyakunyaku inyanyaku nyanyahan nyanyadai nyanynaku nyarabete nyaganyagame.
### Do not run due to limitation of at most 140 characters
> Damn, that's a lot of characters. I'm not running 😩
```

### Graphical User Interface (gui.py)

The keys used are included in the submission. Showing the log and screenshots for the following inputs:

- Input: `Sui-chan wa kyou mo kawaii` 
- Encryption & Signing Keys: `*_1.pem`

![Untitled](mp2_writeup/Untitled%206.png)

```
Encrypted message: b'$\xbcq\xeb\xb9\x04\x83\xd7\x96\x175f\x07P\x8e\xae"-\x1e\xe4h\xe2\x7fd\xb9\xf9\x1b\xfe2F\xa59\xdd\x01\xb4i>\xb8\xd1\xdd~\x1c<"\xef\xa1\xa7\xc6wh\xd5Mg\xd2\xb3\x19\xc5\x83R\x17\xf5j\x83\xd6\x15D\x8e\xa7`&\xed\x880\xd4\x12\r\x03Af\xc5\xcfK-\xb0\x11\xb7\xb2\xb70\x11\x06~\x8c\x18\x9e\xb7\xa8L\x11\x87w\x8ai\x1b!\xca|\x03\xed\xf2\xec\xfd\xbc\x89\xe5\x84\xa5N\xd9\x13\x83E\x01\xdd\x06QF\xe9'
Signature: b'T\xa6\xc3O|\xf5\xe7\xc7\x05i\xc0\x82\xe5*\x13>\xa6A\x19\xb39\xb6OZQ!\xed \xeb\xd6\xb0F\xa09p\xf6\xa8V\xcdi\xb9\xa9\xc0\xc0\xbd\x89\xb9P\x11\xf64n+\x875-\x87\xde(\xd8)\xa3\xd4\x14\xcf\xbc\xa4`\xf0\xb4\xfdZ\xc8\xc36k\xfc"\xcb\xe6\x88\x94\n\xe7\xd6\xf2\xbaa\xab\x16^|\x94\xcb\xc0\x04\xa5\xe8\xe7 \xab\xc3o\x82"\xf20\xfe\x90\xe7\xc4\xecR\xee\x1c\xe2\xd6r\xe8>\x96t\x91\x91+\xc0\x1d\xed'
Decrypted message: Sui-chan wa kyou mo kawaii
```

- Input: `3:12`
- Encryption & Signing Keys: `*_2.pem`

![Untitled](mp2_writeup/Untitled%207.png)

```
Encrypted message: b'w\xe4MB\xc8\xda\x9d\x0b\xf3\xaa\xb2+\x81\x1a$\xaa.\x1d_Hx\xa6\x07+\xb2x/\x97\xe1]9oT}\x7f\xc6\xa5\xbd\xbd\xfd\xc5\x17A)\x80\x10F7\xa8n\xa5\xee\xe1\xd7VdG\xc9\x8f\xa0$\xb2\xb5\x8cgH\x0f\x16\xd6BA\x13d\xb06\xc5ya\x16"\xe3:\xca\x92\xbdC\xf4\xf8\xf8:!l-\xed\xa6\x08\x0cF\xb6\xef\xc7\xd7o\x84\xb21\xd5Z\xd4\xa5\xe5\x99D\xb6\t_\x164s\xa2\x16\xbc\x9aoE\xe7\x06\xd1'
Signature: b':\xf9\xb6\xe5\x19p\xec\xba\xff-_\x94\xdeC\x92uP\xb6\xe5\x1c\x99o\xc9\xa3\x8f\xde\xa1\x95\x9b\x0f\xfb\xe2\xdc\x07C\x8d{\xc0\xca\xdc\x9f\xa1*\x1ahMW\xe1[\xbc\x8bI*\x13H*\xb6|N{M7\xec\x03\xc9J\x07s\x03^8\xfe\xaeC\xc3\xa1\xfb+\xd9\xc0\xbeBSo\xdd\xe7\x02/$\xec\xb8\xfb\xbfTF\x91m\x19\xa9\xabb_\x15U"\xee\xc2pMM\xa4l\'\xe2\xfe=\x87\x8a\x15\x07\x92Q^Q$p\x98\x88'
Decrypted message: 3:12
```

- Input: `It is what it is`
- Encryption Private Key: `encryption_1.pem`
- Encryption Public & Signing Keys: `*_2.pem`

![Untitled](mp2_writeup/Untitled%208.png)

```
Encrypted message: b'\x07b\xd9\x8a[\xe0\xa1Q\x0c\x02~\t\xad\x86\xe9\xb4\xc5~Mk\x19\x07\xcb\xa3\xdf\x1c\x813\xd4\xe9#\rJ\x98\xacQ\xe2J\x16\x85;Y\xaf.\xa9}s\t\xca\xce\xaa\xfaq"\xe1\xf7\xea\xb6Q\xb6X Lo-\xfaz\xa5\x8d\xdbb\xa0\x7f\x17CO\xa6B\xd9(Z|\x98kz\x1al\x02\r\x10\xadJ\x98\xfd>:\xff9\xfa\x9b\xaaO\xc2\x1e\xd0*\xb9A\\\x1c\xfa\xf5\x05\x8f\xf1\xda\x923\xad\x83\xa7K3\x14\xa9%yK'
Signature: b'D\xe2\x08\n\xc5\xc7F\x93!^y\xa7\xd7\xca\x9bu_\xf07P\xb3\x8f\xe9\x05\xfb\x94\x9f\xd1\xa7\xe6\xb1J\xfbTg\x8a\xfb\xcd\xbc\xbeu\x0f\xd3\x90|{o9gu\xac|\xb8v\xf1}o\xbd\xea\xb9o\xfd|[&\x85@\xd3\xaa_I\xa4\r\xd6\xe0\x11k\xcd\xcf\x18\xfc\xe7\x9d\x12\x9b\xf6k\x92!\xf0Y\xe8\xb9p\xd1\xad\x8f\x84q&\x88\xdd\x1f7?"\x99\xe2?\xd4\x8fy8\xb7\xb0h\x9b\xc0W\xbed\x80\x92\r\xa3\xe1\x1aq'
Decrypted message: Verification Failed. Keys might be different.
```

- Input: `Sweet Potato 1024`
- Signing Public Key: `signing_2.pem`
- Encryption & Signing Private Keys: `*_1.pem`

![Untitled](mp2_writeup/Untitled%209.png)

```
Encrypted message: b'm\xe1\x13\xe1\x8ej#\x14\x0c\xa8\x824\xc3\xb3\x9dl\x02$\x84\xcf&\xeb\xa7\xcc\xd2\x01\xd6\xe4\xa6S\x9f)\xbcQS\x0f!\xb35\xa4\xcdg\x90\xaf\x0f2X\x96\x99\xd2\x9asDY\x07\x83\x14\x88s\x87\xeb\xe3M\xfc\xae\xc4\xdd\xacs\xf9\xaa`\x10\x0f\xe4IA\xbbJ\xc8\xe2oA\x1c\xec9*\xe4\xe9"\x05\xee\xf0\x7f\x0f}\xab6\xc8\xdf\x1fU\xb0\x83(\xaf\xbaj\xd3\x8c6D\xa1\xca\xe8X\xf4q+\x1d0\'\xf0\xe6G\xd6X\x95'
Signature: b"\x13Kt\xd5^\xa6E\xc6\x13I$\xc0\xa4\x85I,\xba\x89\x12\xb4%n}\xa1(\xd4\x18L\x0b\x05\xe3\xbb\xd9\xaa*8m'\x0f\xac.\xf0\xe2a\x8e \x96\x1a`\xa0\xbc\xcc\xa6\xb6\x13\xb5\xe0\xdd\xd1Z\x0cj}{\xe9\x9c\x8f\xf4T\xb9('\xd8l\x0fv\xfa\x88\x9c\xad_\xac\xd7\xe5v\x97O\x91\xbf\xdf\xf1N\xd9\xf8\xc1\x9e\xf8TM\x96J3yH\x97\xa3\xae\x83\xae\x92\xd3\xc1\x7f1\xe5\xc5Si\x96*7\xa6\xdc\xf1\xbc`\xa6>"
Decrypted message: Verification Failed. Keys might be different.
```