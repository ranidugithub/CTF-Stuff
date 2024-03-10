It is used to embed and extract secret messages in images. It supports all the general formats of images like .png, .jpg etc.

### Installation

```
$ sudo apt install steghide
```

### Usage

To embed a secret message into an image

```
$ steghide embed -cf image.jpg -ef secret_message.txt
Enter passphrase : ********
Re-Enter passphrase : ********
embedding "secret_message.txt" in "image.jpg"... done
```

To extract the secret message from the image

```
$ steghide extract -sf image.jpg
Enter passphrase : ********
wrote extracted data to "secret_message.txt".
```

For any help with the commands type

```
$ steghide --help
```

It is important to note that the password may not always be a plain text sentence. Sometimes it may be hashed. Some examples of hashes include MD5, sha1 etc. We all know that there is no specific way to reverse the hashes. But, there are websites which store hashes of certain commonly used strings.

Some of such websites are:  
1. [HashKiller](https://hashkiller.co.uk/md5-decrypter.aspx)  
2. [MD5Decrypt](http://md5decrypt.net/)

here we can extract the password with a wordlist.

```
$ steghide extract -sf austrailian-bulldog-ant.jpg -xf output.txt -p wordlist.txt
```

### References[¶](https://wiki.bi0s.in/steganography/steghide/#references "Permanent link")

For more information about the tool,

```
$ man steghide
```
