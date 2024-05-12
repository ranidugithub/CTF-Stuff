In bash scripting, variables are placeholders used to store data that can be referenced and manipulated throughout the script. They provide a way to make scripts more dynamic and adaptable by allowing values to be assigned and changed as needed.

we dont even need a script to implement a variable. we can just open terminal and just add a variable as below.

`myname="Hyphen"`

![](Images/Pasted%20image%2020240512160013.png)

Bash requires a dollar sign (`$`) before a variable name to reference it because it needs a way to distinguish between regular text and variable names. The dollar sign signals to Bash that what follows is a variable name that needs to be replaced with its value. This convention helps Bash parse the script correctly and avoid confusion between literal text and variable references.


how could actually variables helps us?

imagine if there requirement is automating task in production, variables are very useful. variables have many use cases. One of the major thing, they do is avoid retyping.

now in below example we have use a single variable in multiple places. so we dont have the word awesome manually in each line.

![](Images/Pasted%20image%2020240512164813.png)

when we run the bash script, output will be displayed as below.
![](Images/Pasted%20image%2020240512165024.png)

Exercise 1 - now lets make variable that equal to the output of a command.

so below is the example- so in here we haven't use any kind of double quotations but parenthesis. **$(ls)** - this is called a **subshell**.

this allows to execute a command in background. it sends the ls to background and equal it to the given variable.
![](Images/Pasted%20image%2020240512165623.png)

now look in the below example :
![](Images/Pasted%20image%2020240512171903.png)

here is the output:
![](Images/Pasted%20image%2020240512171936.png)
we didn't even declare any kind variable for "USER", but output shows the current user name.

In the system there are default variables, already declared. And $USER is one of those. This will always shows he user currently you login as.

There is environment inside the shell. And this environment contains bunch of variables that already and always there. A variable with upper case is a system variable/environment variable that something built in. Even we can create upper case variables. lower case and upper case variables has important distinctions. So we shouldn't create our own variables with uppercase. if some see your script, that person is going to identify difference of system and custom variables by lowercase or uppercase. Still you can create your own variable, but not recommended.


You can see the current environment variables by typing **env**.
check out..... see yaa...

