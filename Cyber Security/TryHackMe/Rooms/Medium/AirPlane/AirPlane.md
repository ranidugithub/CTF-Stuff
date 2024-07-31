
![](Images/Pasted%20image%2020240730094837.png)

Lets perform a simple RustScan to identify openports.
we can type rustscan -a {ip}

![](Images/Pasted%20image%2020240730100546.png)

to get in to more details as a habit, I am performing a nmap scan too.
**sudo nmap -sV -sC -Pn -O -oN nmap_results {ip}**

![](Images/Pasted%20image%2020240730101950.png)

now lets check the anything displays on the web with the given ip address.
![](Images/Pasted%20image%2020240730102738.png)

the page says not found, because we need to add this name to linux Host file. we have to tell our system that given ip address is = airplane.thm.

so we can visit **/etc/hosts** as sudo and add the name and the ip like below.

![](Images/Pasted%20image%2020240730103107.png)

now lets revisit the website.

![](Images/Pasted%20image%2020240730103241.png)
we will be redirected to the above page. we can check for some clue s in inspect this page.

we found nothing suspicious in inspect page.

![](Images/Pasted%20image%2020240730103907.png)
we look close to this link, this is an link of a web security vulnerability known as **Path Traversal** (also called Directory Traversal).

- `http://airplane.thm:8000/` is the base URL for a website.
- `?page=...` is a query parameter indicating that the website is expecting the name of a page to display.

so lets check the passwd location in linux system using this vulnerability.
as expected we got the pass file from the location.

![](Images/Pasted%20image%2020240730104445.png)

Below image shows some usernames that might help.

![](Images/Pasted%20image%2020240730105858.png)

so this will take some time, if we are going to always download and read the file.

we can use burpsuite to continue the process much easier.

open burpsuite and we can intercept the network and refresh link.

so we will get some thing like this. we need to send this to repeater for further investigation.
![](Images/Pasted%20image%2020240730111657.png)

if we click send in repeater, we can see them clearly.
![](Images/Pasted%20image%2020240730111844.png)

now lets check environment information or who is the current user of this session.

for that we can add proc/self/environ at the end.
- If the web server is not properly secured, it may read the `/proc/self/environ` file and display its contents on the webpage.
- Environment variables can include sensitive information such as:
    - Server configuration details.
    - API keys.
    - Database credentials.
    - Other sensitive data.


![](Images/Pasted%20image%2020240730112647.png)

since this home directory shows as Hudson, we can make sure that we are in Hudson session.

since we found nothing much interesting here we can continue with the second port which is 6048



