
![](images/Pasted%20image%2020240801113557.png)

challenge description.

Yes, it's me again with another crypto challenge!

Have a look at the source code before moving on to Task 2.

You can review the source code by clicking on the Download Task Files button at the top of this task to download the required file.

first lets download the taskfile

This code contains a simple server that runs a game where the user has to guess a randomly generated key used to XOR (a type of encryption) a fake flag.

- The server encrypts a flag with a random key using XOR.
- The client receives the encrypted flag and has to guess the key.
- If the client guesses correctly, they get the flag. Otherwise, they get a message saying they're close but not quite right.

so we can code a simple python script to get the key.

```
import string
from pwn import *


charset = string.ascii_letters + string.digits
enc_flag = bytes.fromhex("06187a170863315b020c1728432d0c266454071b133e455f193e1c4e042d20244e5c0d2028781e05")
part_flag = b'THM{'

part_key = xor(enc_flag, part_flag)[:4]

#print(part_key)

for c in charset:
    key = part_key + c.encode()
    dec_flag = xor(enc_flag, key).decode()
    

    if dec_flag[-1] == '}':
        print(f"key: {key.decode()}")
        print(f"flag: {dec_flag}")
```

This code attempts to decrypt an XOR-encrypted flag by finding the key used for the encryption. Here's a simple explanation:

1. **Imports and Setup:**
    
    - The code imports necessary libraries:
        - `string` for generating a list of possible characters.
        - `pwn` for its `xor` function, which helps with the XOR operation.
    - `charset` is a string containing all uppercase and lowercase letters, plus digits.
    - `enc_flag` is the encrypted flag in hexadecimal form, converted to bytes.
    - `part_flag` is the beginning of the flag, known to be `THM{`.
2. **Partial Key Calculation:**
    
    - `part_key` is calculated by XORing the encrypted flag with `part_flag`. This gives the first part of the key.
3. **Brute Force Search:**
    
    - The code iterates through each character in `charset` to guess the remaining part of the key.
    - For each character:
        - The guessed key (`key`) is `part_key` followed by the character.
        - The code XORs the encrypted flag with the guessed key to attempt decryption.
        - If the decrypted flag ends with `}`, it prints the key and the decrypted flag.

**Summary:**

- The code tries to find the key used to encrypt the flag by using a known part of the flag and brute-forcing the remaining characters.
- When it finds a valid key, it prints the key and the decrypted flag.


![](images/Pasted%20image%2020240801124611.png)

