![](images/Pasted%20image%2020240805124658.png)

As usual lets perform Nmap scan and Rustscan to get information about open ports and available services.

![](images/Pasted%20image%2020240805125446.png)

so as we can see there are number of ports open in the results.

same time we can that SMB2 error message. we can check SMB details for information.
first what is SMB?
**Server Message Block** (**SMB**) is a [communication protocol](https://en.wikipedia.org/wiki/Communication_protocol "Communication protocol")[[1]](https://en.wikipedia.org/wiki/Server_Message_Block#cite_note-1) used to share files, [printers](https://en.wikipedia.org/wiki/Printer_(computing) "Printer (computing)"), [serial ports](https://en.wikipedia.org/wiki/Serial_port "Serial port"), and miscellaneous communications between [nodes](https://en.wikipedia.org/wiki/Node_(networking) "Node (networking)") on a [network](https://en.wikipedia.org/wiki/Computer_network "Computer network").

okay lets check, what is SMB client?

`smbclient` is a command-line tool used to access and interact with SMB (Server Message Block) shares on a network. It is part of the Samba suite, which provides interoperability between Linux/Unix servers and Windows-based clients. `smbclient` allows users to list files, upload and download files, and perform other file operations on remote SMB servers.

Here are some key features and uses of `smbclient`:

1. **Connecting to SMB Shares**: You can connect to SMB shares on Windows or Samba servers using `smbclient`. This is useful for accessing shared files and directories.
    
2. **File Operations**: Once connected, you can perform various file operations such as listing files and directories, downloading files from the server, and uploading files to the server.
    
3. **Authentication**: `smbclient` supports different authentication mechanisms, allowing users to connect to shares that require a username and password.
    
4. **Scripting and Automation**: Because it is a command-line tool, `smbclient` can be used in scripts to automate file transfer and other tasks.
    
5. **Interactive Shell**: `smbclient` provides an interactive shell where users can execute commands similar to an FTP client.
    

### Basic Usage

Here is a basic example of how to use `smbclient` to connect to an SMB share:

1. **Listing Files on an SMB Share**:
    
    `smbclient //server/share -U username`
    
    After entering the command, you will be prompted to enter the password for the specified user. Once authenticated, you will enter an interactive session where you can execute commands.
    
2. **Downloading a File**:
    
    
    `smbclient //server/share -U username -c "get filename"`
    
    This command connects to the specified share and downloads the file named `filename`.
    
3. **Uploading a File**:
    
    
    `smbclient //server/share -U username -c "put localfile remotefile"`
    
    This command uploads a file from the local system (`localfile`) to the remote share (`remotefile`).
    

### Example Commands

- **Connecting and listing files interactively**:
    
    
    `smbclient //192.168.1.100/shared -U user`
    
- **Listing files in a directory non-interactively**:
    
    
    `smbclient //192.168.1.100/shared -U user%password -c "ls"`
    
- **Downloading a file**:
    
    
    `smbclient //192.168.1.100/shared -U user%password -c "get file.txt"`
    
- **Uploading a file**:
    
    `smbclient //192.168.1.100/shared -U user%password -c "put localfile.txt remotefile.txt"`
    

`smbclient` is a versatile tool for managing and interacting with SMB shares, making it an essential utility for network administrators and users needing to access networked file systems.


![](images/Pasted%20image%2020240805133336.png)

The command `smbclient -L 10.10.16.44` is used to list all the available SMB (Server Message Block) shares on the server with the IP address `10.10.16.44`.

The command successfully enumerated the SMB shares on the target server `10.10.16.44`. The available shares include administrative shares (`ADMIN$`, `C$`), a team-specific share (`datasci-team`), and an IPC share (`IPC$`). Further investigation of these shares may reveal useful information or provide access to files.

![](images/Pasted%20image%2020240805133919.png)

so here we can use this command to connect to datasci-team share on the SMB server. then we ls to list down the files and directories.

![](images/Pasted%20image%2020240805135019.png)


To further explore the contents of the `datasci-team` SMB share on the server `10.10.16.44`, I first connected to the share using `smbclient \\\\10.10.16.44\\datasci-team` and entered my password. Once connected, I turned off the interactive prompt with `prompt off` and enabled recursive directory listing with `recurse on`. I then set the local directory to `/home/kali/Desktop/TryHackMe/Rooms/Weasel/` using `lcd`. Finally, I used the `mget *` command to download all files and directories from the `datasci-team` share to my local machine for further analysis.


![](images/Pasted%20image%2020240805135727.png)

![](images/Pasted%20image%2020240805135833.png)

![](images/Pasted%20image%2020240805135913.png)

![](images/Pasted%20image%2020240805140048.png)

![](images/Pasted%20image%2020240805140720.png)

![](images/Pasted%20image%2020240805141445.png)

![](images/Pasted%20image%2020240805141746.png)

![](images/Pasted%20image%2020240805142050.png)

![](images/Pasted%20image%2020240805142245.png)

![](images/Pasted%20image%2020240805144022.png)


![](images/Pasted%20image%2020240805144414.png)


![](../../../../../Pasted%20image%2020240805144742.png)


![](../../../../../Pasted%20image%2020240805145221.png)


![](../../../../../Pasted%20image%2020240805145242.png)


