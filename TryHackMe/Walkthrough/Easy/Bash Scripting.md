![alt text](<images/Pasted image 20240412213827.png>)
What is bash?

Bash is a scripting language that runs within the terminal on most Linux distros, as well as MacOS. 

This room helps to learn topics related to.


    Bash syntax
    Variables
    Using parameters
    Arrays
    conditionals
***

### Task2

Bash scripts always start with below code. So that your shell know that this file needed to run using bash in the terminal.

	"#!/bin/bash"

lets make a simple bash script.

```
#!/bin/bash

echo "Hello World!"
id
pwd
```

so above script outputs ==Hello World== on terminal and in the same time ==id== ,==pwd== , commands will executed. 

1.What piece of code can we insert at the start of a line to comment out our code?

	#

2.What will the following script output to the screen, echo “BishBashBosh”

	BishBashBosh

### Task3

Intro in to variable

Below you can see a simple variable example.

	name="Jammy"

So we have assigned value "Jammy" to variable "name".

You need to know that, there should be no spaces between variable name and "=". It doesn't work if we add space.

To use our variable in other places, we can add "$" in front of the variable name.

```
#!/bin/bash

name="Jammy"
echo $name
```

This will out put "Jammy"

Debugging is a very important task, when it comes to programming. Bash has a few inbuilt features, that will helps us to debug the code.

When running at the command line you can do:


	bash -x ./file.sh

Lets create a script and check how debug mode works.

![alt text](<images/Pasted image 20240413102624.png>)

![alt text](<images/Pasted image 20240413102718.png>)

as above shown set -x and set +x show the range that needed to be debugged.

1 What would this code return?

	Jammy is 21 years old

2 How would you print out the city to the screen?

	echo $city

How would you print out the country to the screen?

	echo country


### Task4

Now lets see how we can use parameters in bash scripting.

below simple script shows how parameters works.

	name=$1
	echo $name

We now run our script with ./example.sh Alex

And sure enough we get returned with “Alex”

To make it little easy, we can use "read" command to get data.

	#!/bin/bash
	echo enter your name
	read name
	echo "Your name is $name"



### Task5 Arrays



Arrays are used to store multiple pieces of information in one variable.

