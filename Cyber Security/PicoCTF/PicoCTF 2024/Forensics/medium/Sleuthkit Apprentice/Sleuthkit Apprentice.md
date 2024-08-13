
Here is a detailed summary of the forensic CTF process you performed:

1. **Listing Initial Files**:
    
    - Command: `ls`
    - Result: Two files listed, `disk.flag(1).img.gz` (compressed image file) and `tmp` (directory).
2. **Decompressing the Image File**:
    
    - Command: `gunzip disk.flag\(1\).img.gz`
    - Outcome: The file `disk.flag(1).img.gz` is decompressed to `disk.flag(1).img`.
3. **Verifying the Decompressed File**:
    
    - Command: `ls`
    - Result: `disk.flag(1).img` and `tmp` are present.
4. **File Type and Partition Analysis**:
    
    - Command: `file disk.flag\(1\).img`
    - Output: Identified as a DOS/MBR boot sector image with three partitions:
        - Partition 1: Linux (0x83)
        - Partition 2: Linux Swap / Solaris x86 (0x82)
        - Partition 3: Linux (0x83)
5. **Detailed Partition Information**:
    
    - Command: `mmls disk.flag\(1\).img`
    - Details:
        - Offset Sector: 0
        - Units: 512-byte sectors
        - Partition Table:
            - Slot 000:000 (Linux, starts at sector 2048)
            - Slot 000:001 (Linux Swap, starts at sector 206848)
            - Slot 000:002 (Linux, starts at sector 360448)

![](../../../../../../Pasted%20image%2020240813125543.png)
- **Mounting the Third Partition**:
    
    - Command: `sudo mount disk.flag\(1\).img /home/kali/Desktop/PicoCTF/Forensics/tmp/test/ -o offset=$((360448*512))`
    - Description: Mounts the third partition to the specified directory using the calculated offset.
- **Navigating and Listing Directories**:
    
    - Commands:
        - `cd /home/kali/Desktop/PicoCTF/Forensics/tmp/test`
        - `ls`
    - Contents of the `test` directory:
        - Standard system directories and files are visible.
![](../../../../../../Pasted%20image%2020240813125618.png)
1. **Switching to Root and Exploring**:
    
    - Command: `sudo su`
    - Directory Navigation:
        - `cd root`
        - `ls`
    - Found `my_folder` in the root directory.
2. **Accessing the Folder and Reading the Flag**:
    
    - Commands:
        - `cd my_folder`
        - `ls`
        - `cat flag.uni.txt`
    - Revealed Flag: `picoCTF{by73_5urf3r_adac6cb4}`

This process involved decompressing a disk image, examining its partitions, mounting a specific partition, and navigating through the file system to find the flag.


![](../../../../../../Pasted%20image%2020240813125635.png)


