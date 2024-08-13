
The "Publisher" CTF machine is a simulated environment hosting some services. Through a series of enumeration techniques, including directory fuzzing and version identification, a vulnerability is discovered, allowing for Remote Code Execution (RCE). Attempts to escalate privileges using a custom binary are hindered by restricted access to critical system files and directories, necessitating a deeper exploration into the system's security profile to ultimately exploit a loophole that enables the execution of an unconfined bash shell and achieve privilege escalation.

first lets perform a simple Nmap scan.

![](images/Pasted%20image%2020240810122839.png)
this shows port 80 and port 20 is open.

lets check port 80, and show a website. And there is something called SPIP
_SPIP_ is a free software content management system designed for web site publishing, oriented towards online collaborative editing.

![](images/Pasted%20image%2020240810123403.png)

then I checked for some SPIP vulnerability and found a good git repository explaining a attack on SPIP.


in a part is shows the possibility in injection of serialized PHP string,
![](images/Pasted%20image%2020240810125122.png)

if we go forward with SPIP, we redirecting to another page.
![](images/Pasted%20image%2020240810125345.png)

and if we click the first link, we ll be sent to another page.
![](images/Pasted%20image%2020240810125438.png)

then as per the instruction, if we put page=spip_pass, we ll be redirected to the below page
![](images/Pasted%20image%2020240810125726.png)

we can use open burpsuite, listen and enter a random email in the box.
![](images/Pasted%20image%2020240810130205.png)

![](images/Pasted%20image%2020240810130516.png)


now we have to add remaining parts as explained in the website.
![](images/Pasted%20image%2020240810132056.png)


then we can forward the traffic and we got another page which has information related to php.

lets search for a php injection method using metasploit
![](../../../../../Pasted%20image%2020240810135914.png)

we found one remote code execution method.
we can use 1 and set all the required information
![](../../../../../Pasted%20image%2020240810140240.png)

and we successfully able to spawn a shell.
![](../../../../../Pasted%20image%2020240810140808.png)


since we can read the id_rsa file, we can copy create id_rsa file in our kali machine.

![](../../../../../Pasted%20image%2020240810141045.png)



so using this id_rsa we can easily login to think user
![](../../../../../Pasted%20image%2020240810141415.png)

i tried to add linpeas to the tmp directory. got an user permission error.
![](../../../../../Pasted%20image%2020240810142331.png)

then searching hints given in root flag. found a location where we can send linpeas.(/dev/shm)
![](../../../../../Pasted%20image%2020240810142651.png)
i get to know i was not in bash, so i changed to bash and checked the  opt folder.
![](../../../../../Pasted%20image%2020240810144116.png)

and found a docker container
![](../../../../../Pasted%20image%2020240810145003.png)

![](../../../../../Pasted%20image%2020240810145809.png)

![](../../../../../Pasted%20image%2020240810150050.png)


![](../../../../../Pasted%20image%2020240810150029.png)







