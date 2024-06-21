![](Images/Pasted%20image%2020240507123436.png)

 CHALLENGE DESCRIPTION

As a part of our SDLC process, we've got our firmware ready for security testing. Can you help us by performing a security assessment?

what is SDLC process?

  
SDLC stands for Software Development Life Cycle. It is a systematic process for planning, creating, testing, and deploying an information system.

  
Inside the `Needle.zip` file, there's a `firmware.bin` file. I connected to the provided IP address and port using Netcat, which prompted me for a login and password. I tried common usernames like `admin` with the password `admin`, but the login attempt failed.

![](Images/Pasted%20image%2020240507125453.png)

now we need identify, things that embedded in this firmware.bin file.

By using `binwalk`, you can efficiently inspect and understand the contents of `firmware.bin`, which can provide valuable insights into its structure and functionality.

![](Images/Pasted%20image%2020240507130124.png)

After using `binwalk` on `firmware.bin`, a new folder called `firmware.bin.extracted` is created. Inside this folder, you can see various subfolders and files.

![](Images/Pasted%20image%2020240507130630.png)

 To locate the login username and password, we can search the extracted files for references to "login" using the command `grep -rn "./" -e "login"`. This command searches recursively through the extracted directory for instances of the word "login." The search results include various relevant pieces of information, such as the line `/usr/sbin/login -u Device_admin:$sign`, which provides details about the login process and potential credentials.

 ![](Images/Pasted%20image%2020240507131418.png)

  
Next, we know that the password for `Device_admin` is stored in a variable called `$sign`. To find the password, we search for files named "sign" using the command `find ./ -name sign`. After locating the file, we can view its contents with the command `cat`, revealing the password for the login.
![](Images/Pasted%20image%2020240507132501.png)

Now, let's use Netcat to connect to the server and log in with the username and password we found. Once logged in successfully, we can list the contents of the directory using `ls` and see the file `flag.txt` as shown below.

![](Images/Pasted%20image%2020240507133355.png)