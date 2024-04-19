Write a program that encrypts and decrypts a message using RSA-OAEP with authenticity.

Use the encrypt-then-sign scheme for authenticated encryption. Use a separate key for encryption and signing.

Do not implement crypto algorithms on your own. Make use of cryptographic libraries in implementing your program.

Your program must be able to:

    separately generate new keypairs for encryption and signing,
    encrypt-then-sign/verify-then-decrypt a short ASCII message (at most 140 chars) using RSA-OAEP.

Your deliverables are:

    a short narrative writeup/readme detailing your work and how to use it,
    your program and source code,
    sample inputs/files (generated keys, messages, ciphertexts).

Sample inputs:

Input 1
```
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
