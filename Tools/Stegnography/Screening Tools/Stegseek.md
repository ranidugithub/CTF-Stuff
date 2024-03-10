
Stegseek is a lightning fast steghide cracker that can be used to extract hidden data from files. It is built as a fork of the original steghide project and, as a result, it is _thousands of times_ faster than other crackers and can run through the entirety of **`rockyou.txt`* in under 2 seconds.**

Stegseek can also be used to extract steghide metadata without a password, which can be used to test whether a file contains steghide data.

* `rockyou.txt` is a well-known password list with over 14 million passwords.

##### Installation

```
$ sudo apt install stegseek
```

#### Usage

The most important feature of stegseek is wordlist cracking:

```
$ steggeek sus.jpg /usr/share/wordlists/rockyou.txt
```
