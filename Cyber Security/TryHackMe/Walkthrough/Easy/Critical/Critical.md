![](Images/Pasted%20image%2020240729082806.png)

# Task1 : Introduction

Incident Scenario

Our user "Hattori" has reported strange behavior on his computer and realized that some PDF files have been encrypted, including a critical document to the company named important_document.pdf. He decided to report it; since it was suspected that some credentials might have been stolen, the DFIR team has been involved and has captured some evidence. Join the team to investigate and learn how to get information from a memory dump in a practical scenario.

Learning Objectives

In this room, we'll cover the following learning objectives.

    Memory Forensics’ basic concepts.
    How to access and set up the environment.
    Gathering information from the compromised target.
    Search for suspicious activity using the information obtained.
    Extracting and analysing data from memory.
    Conclusion & further steps after completing the room.

# Task2: Memory Forensics

memory forensics is a subset of computer forensics that analyze volatile memory.
RAM(Random Access Memory) is the main component accessed, when it comes to memory forensics.
Main different between memory forensics and digital forensics is memory forensics provides additional information such as processors, applications which were running in a particular time and detailed information on the execution flow on a system that may not be present in regular storage units or application logs. 

We can divide Memory forensics in to two part:
- Memory Acquisition.
- Memory Analysis.

During the memory acquisition phase, we'll copy the live memory to a file, commonly referred to as a dump, to perform the analysis without risking losing the data from an inadvertent reboot on the compromised system and have proof of the analysis inc as needed.

- What type of memory is analyzed during a forensic memory task?
	RAM

1. In which phase will you create a memory dump of the target system?
	Memory Acquisition


# Task3: Environment & Setup

Now lets approach the first step of memory forensic task.
Memory Acquisition, and determine the environment and tools we will use to analyze the memory dump.

Imaging Tools

There are several ways to acquire the memory from the target machine if needed; several tools can help us, but which one to use will depend on personal preference and the OS involved in the imaging task. Some of these tools are:

Windows
	FTK imager, WinPmem
Linux
	LIME
macOS
	osxpmem

In our scenario, FTK Imager was used to take the memory dump of the compromised machine, which was copied to the Linux machine to perform the analysis.

After you access the given VM, you will be able to see a memory dump named memdump.mem

![](Images/Pasted%20image%2020240729120548.png)

To analyze the dump, we'll use Volatility 3, a popular choice among analysts to inspect a memory during an incident. In this case, the tool has been installed, and an alias was created for simplicity; entering the command vol will execute Volatiliy3 in the terminal. The -h switch can display the help menu, as shown below.

![](Images/Pasted%20image%2020240729121322.png)

From the above output we see several options are provided according to different OS systems. Since we took the memory dump from windows OS, we can filter out windows related commands using ==**vol windows --help**==

![](Images/Pasted%20image%2020240729122508.png)

Plugins are extremely helpful during the analysis when using Volatility3 since they will quickly parse a memory dump for specific data types and sort the data according to the selected plugin. You can find a summary of some of the most relevant plugins below
Windows.cmdline
	Lists process command line arguments
windows.drivermodule
	Determines if any loaded drivers were hidden by a rootkit
Windows.filescan
	Scans for file objects present in a particular Windows memory image
Windows.getsids
	Print the SIDs owning each process
Windows.handles
	Lists process open handles
Windows.info
	Show OS & kernel details of the memory sample being analyzed
Windows.netscan	Scans for network objects present in a particular Windows memory image
Widnows.netstat	Traverses network tracking structures present in a particular Windows memory image.
Windows.mftscan
	Scans for Alternate Data Stream
Windows.pslist
	Lists the processes present in a particular Windows memory image
Windows.pstree
	List processes in a tree based on their parent process ID

Now that we know how to access our environment and which tools we will use, let's move to the next phase, where we'll start analyzing the data.

- Which plugin can help us to get information about the OS running on the target machine?

	Windows.info

- Which tool referenced above can help us take a memory dump on a Linux OS?

	LIME

- Which command will display the help menu using Volatility on the target machine?

	vol -h

# TASK4 - Gathering Target Information

Obtaining Information

Getting information about the target is crucial to our investigation since it ensures we're analyzing the correct context and environment of the evidence. This step helps us understand specific architecture and operating systems, ensuring our findings' accuracy, relevance, and legitimacy.

We can get information about the target using the -f switch to indicate the file to analyze, in this case, memdump.mem followed by the plugin windows.info  used to get the general information, as in the example shown below.

![](Images/Pasted%20image%2020240729133326.png)

- Is the architecture of the machine x64 (64bit) Y/N?
	Y

- What is the Version of the Windows OS
	10

- What is the base address of the kernel?
	0xf8066161b000

# TASK5 - Searching for Suspicious Activity


Now that we have the information from the target we are working on let's try to identify any suspicious activity in the memory dump. 

**Suspicious Activity**

Suspicious activity refers to technical anomalies that may be present in a system, such as unexpected processes, unusual network connections, or registry modifications. These activities often signal potential security threats like malware attacks or data breaches. 

**Starting the Search**

We can start by observing any potential network activity. We can use the plugin windows.netstat to see if there's an interesting or unusual connection. At this stage, remote access connections or access to suspicious sites are something to look for. 


vol -f memdump.mem windows.netstat

![](Images/Pasted%20image%2020240729140524.png)


From the output above, we can observe a connection established on port 3389 from the IP 192.168.182.139 with timestamp 2024-02-24 22:47:52.00 ; this could indicate an attacker's initial access. 

Now that we have information about the network, let's look at the processes. A volatility plugin we can use is windows.pstree, which will display a tree of the process running on the OS.

![](Images/Pasted%20image%2020240729141200.png)

As we can observe from the above output, the command provides us with information on processes hierarchically running on the system, indicating to us the process and their respective parent process. In this case, Services.exe is the parent process of dllhost.exe

if we further down we can see a process with the truncated name critical_updat, as shown below.

![](Images/Pasted%20image%2020240729141743.png)


This process does not look like it is part of the system, and observing in detail, it's the parent process of updater.exe, which is also not listed as a process part of the Windows OS.

Great. We identify a possible malicious process and should note the information, like timestamp, PID, PPID, and Memory offset.

- Using the plugin "windows.netscan" can you identify the IP address that establish a connection on port 80?

	192.168.182.128

- Using the plugin "windows.netscan," can you identify the program (owner) used to access through port 80?

	msedge.exe

- Analyzing the process present on the dump, what is the PID of the child process of critical_updat?

	1642

- What is the time stamp time for the process with the truncated name critical_updat?

	2024-02-24 22:51:50.000000


# TASK-06 Finding Interesting Data

With the information we have collected, we can investigate the process critical_updat  that we identified in our previous task, which has a child process called updater. Let's investigate the child process more in-depth. Let's start by looking at where on the disk it was saved; for that, we can use the plugin windows.filescan which will allow us to examine the files accessed that are stored in the memory dump. This output is quite big, so to access the data in a better way, we will use the > character in bash to redirect the output to a file, in this case, filescan_out.

**vol -f memdump.mem windows.filescan > filescan_out**

![](Images/Pasted%20image%2020240729153927.png)

 we want to have more detailed information like when the file was accessed or modified, we can use the plugin windows.mftscan.MFTScan, whose output is also quite big, so we will redirect the output to the file mftscan_out as shown below.

**vol -f memdump.mem windows.mftscan.MFTScan > mftscan_out**

and we need to check for important document.pdf
we can search for cat mftscan_out | grep important
then we get the timestamp of that file created.
![](../../../../../Pasted%20image%2020240729155740.png)


Getting the Goods

Let's get information on the process. There are several ways to examine memory, but we will continue using volatility. This time, we will dump the memory region corresponding to updater.exe , and examine it.

 To accomplish the above, we'll use the plugin windows.memmap. This time, we'll specify the output dir with the -o switch. In this case, we will use the same directory denoted by the character " . "and the option --dump followed by the option --pid and the PID of the process, which in the case of updater.exe is.

**vol -f memdump.mem -o . windows.memmap --dump --pid 1612**

When the command above is finished, we will have a file with an extension .dmp in our working directory.

Examining the file is difficult since it contains non-printable characters, so we'll use the strings command to analyze the output better. Since we have the file strings available to us now, we could look for key patterns like HTTP or key or any pattern that can lead us quickly to an artefact. Another way to scroll the terminal is by using the strings command piped to less to navigate through the output as the command output below.



