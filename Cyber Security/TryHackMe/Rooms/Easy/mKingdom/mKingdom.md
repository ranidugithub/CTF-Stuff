![](images/Pasted%20image%2020240731102244.png)

Task 1 - What is user.txt?

Lets perform Nmap and RustScan to compare and Confirm the open ports.

![](images/Pasted%20image%2020240731102913.png)
From the nmap results, we can see that port 85 is open. lets confirm it with Rust scan.

![](images/Pasted%20image%2020240731103103.png)

lets check, what is available is port 85.

![](images/Pasted%20image%2020240731103402.png)

Okayyy................ soooo.... nothing interesting here, except being pathetic.

so lets perform gobuster scan to find other directories.
![](images/Pasted%20image%2020240731104131.png)
results shows **/app** directory. 

so goes to a page showing jump.
![](images/Pasted%20image%2020240731104326.png)

after we click this button, we are being directed to a different webpage.

![](images/Pasted%20image%2020240731104457.png)

this webpage is in directory called **castle**

So i did couple of gobuster scans on 
gobuster dir -u http://10.10.99.173:85/app/castle/ -w /usr/share/wordlists/dirb/common.txt

![](images/Pasted%20image%2020240731122107.png)

gobuster dir -u http://10.10.99.173:85/app/castle/index.php/ -w /usr/share/wordlists/dirb/common.txt 

![](images/Pasted%20image%2020240731122154.png)
Then i found a login page.

![](images/Pasted%20image%2020240731122259.png)

and same time check **Wrappalyzer** to analyze the stack used to make this website.

and it shows Concrete **CMS 8.5.2** has been used to make the website.

then I searched for Concrete CMS  8.5.2 exploits in google and found a good article.

https://vulners.com/hackerone/H1:768322

according to the article to do anything, we have to login as admin. so i just tried CTF 101 rule book. first tried admin password and boom we are in. sometimes we have to see these challenges in CTF eyes.

After login we need to go setting and select allowed files types. there number of allowed files extensions are shows in text box. we can remove all of them and add php extension. And hit save.
![](images/Pasted%20image%2020240731131907.png)

then we can search for file manager, where we can upload image files.
![](images/Pasted%20image%2020240731132419.png)
since we approve php files. we can add reverse shell to get access to the target machine.

so we can visit pentest monkey and create a new reverse shell and upload it here. after upload start a netcat listener.

![](images/Pasted%20image%2020240731140615.png)

after upload the file, we will able to see the link for that and if netcat listener is started, you can successfully spawn rev shell.
and we can use python3 to make the shell stable and import xterm
![](images/Pasted%20image%2020240731141601.png)

we can check **ss -tpln** 

The `ss -tpln` command in Linux is used to display detailed information about the network sockets on your system. Here's a simple breakdown:

- `ss`: The command used to display socket statistics.
- `-t`: Shows TCP (Transmission Control Protocol) sockets.
- `-p`: Displays the process using the socket.
- `-l`: Lists listening sockets.
- `-n`: Shows numerical addresses instead of resolving hostnames.

So, when you run `ss -tpln`, it shows a list of TCP sockets that are currently listening, along with the processes using them and their numerical addresses and ports.
![](images/Pasted%20image%2020240731142835.png)


since 3306 available means, mysql database is available. so as CTF 101 rule book. we can try blindly login without a password with root user name. and again we are successfully login the mysql database.

![](images/Pasted%20image%2020240731143301.png)

so we can use mKingdom database, and select all from users table. Like below. And here we can get information related to admin user.

![](images/Pasted%20image%2020240731144111.png)

Still we didint got users we needed, when it comes to get access in server users. so lets use mysql DB and check for users.
and here we got the password of SQL hash file for toad user.


![](images/Pasted%20image%2020240731144744.png)

so we can copy this hash and paste it in text file and crack the hash using hash cat. after cracking we cat get password as below.
![](images/Pasted%20image%2020240731150006.png)
 then we can switch user to toad using toad password.

but we cannot find any flags in this user, so which means we have to get access to mario user.
even if we run 
**find / -perm /4000 2>/dev/null**
![](images/Pasted%20image%2020240731151040.png)
most of here permissions created with admin user. so that is useless right now.

now lets find a way to get into mario user.

now if we type env.
The `env` command in Linux is used to display and manipulate the environment variables of the current user session. Environment variables are dynamic values that affect the way processes and applications run on a computer.

we can see a base64 encoded password token. lets decode it.

![](images/Pasted%20image%2020240731151534.png)

i am hoping that is the password for Mario and tried to login with that credentials. and we succeed.
but the other problem is we cannot view the user.txt file because it is created by admin. so we need admin access to view both flags.

so lets sudo -l to check the allowed command to the user. 
The `sudo -l` command in Linux is used to display the allowed (and forbidden) commands for the current user or another user. This command is useful for understanding what administrative privileges a user has without actually executing any commands. Here’s a simple explanation of how it works:

![](images/Pasted%20image%2020240731153156.png)

![](images/Pasted%20image%2020240731155018.png)



![](../../../../../Pasted%20image%2020240731160205.png)


![](../../../../../Pasted%20image%2020240731160145.png)

![](../../../../../Pasted%20image%2020240731160713.png)


