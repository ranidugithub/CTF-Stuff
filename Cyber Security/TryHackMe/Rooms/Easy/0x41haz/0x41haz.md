First we can download the binary file and check the information about the file by typing **file** {file_name}.
![](images/Pasted%20image%2020240806094152.png)

so the file type mentioned here is unknown. so search this on internet and found a good article related fixing or brining back to default state.

https://pentester.blog/?p=247

![](../../../../../Pasted%20image%2020240806094415.png)
as it says 6th byte should be LSB(1) MSB(1) . But our binary file says 2. lets change it back to 1.
we can use **hexeditor** to change the values.

![](../../../../../Pasted%20image%2020240806095429.png)

now it shows information without nay error.
![](../../../../../Pasted%20image%2020240806095515.png)

The disassembly is performed using a tool like `radare2` (r2), which is a popular open-source reverse engineering framework.
The program is a simple password checker. It prompts the user for a password, reads the input, checks if the input is exactly 13 characters long, and then compares each character of the input with a predefined string. If the input matches the predefined string, it prints a success message; otherwise, it prints a failure message and exits.

![](../../../../../Pasted%20image%2020240806102042.png)

final answer is the combination of below three strings

![](../../../../../Pasted%20image%2020240806102259.png)

![](../../../../../Pasted%20image%2020240806102320.png)

