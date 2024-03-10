It is a tool that is used mainly to read metadata in files.

##### Installation

```
$ sudo apt install exiftool
```

#### Usage

```
$ exiftool <file-name>
```

```
$ exiftool -a -u <file-name>
```




Exiftool gives the metadata of a file as its output. This data can be used for further analysis regarding the file type and its data. On a CTF point-of-view, we might get clues and hints or information that might turn out to be crucial for finding the flag.

> Tip
> 
> _strings_ is a bash command that shows all the ASCII strings in the file that is passed into the command. In CTFs it is often seen that sometimes some clues or even the flag can be found as an ASCII string inside the given challenge file. Way to use:

```
$ strings  <file-name>
```

### References

For more information about the tool,

```
$ man exiftool
```


