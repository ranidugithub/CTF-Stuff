
![](images/Pasted%20image%2020240730163915.png)

This is basic forensic challenge, where we can improve our data verification skills using checksum.

what is checksum?
A checksum, also known as a hash, is ==a unique value that can be used to verify the integrity and authenticity of data==.

In this scenario, where you need to identify and retrieve a flag (a hidden string) by solving a series of tasks. Here’s a step-by-step breakdown of what is happening:

![](images/Pasted%20image%2020240730164327.png)

You list the files in the current directory, revealing three items: `checksum.txt`, `decrypt.sh`, and a directory named `files`.

view the contents of `checksum.txt`, which contains a SHA-256 hash: `5848768e56185707f76c1d74f34f4e03fb0573ecc1ca7b11238007226654bcda`.

calculate the SHA-256 checksums for all files in the `files` directory and use `grep` to find the file that matches the hash from `checksum.txt`. The output indicates that the file `8eee7195` matches the hash.

list the files in the `files` directory. This step is redundant since you already matched the checksum to `8eee7195`.

run the `decrypt.sh` script with the file `8eee7195` as an argument. The script processes the file and reveals the flag: `picoCTF{trust_but_verify_8eee7195}`.

