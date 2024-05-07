Welcome to my mini project focused on Bash scripting! This project demonstrates the use of Bash scripts to perform common tasks, particularly in network and system administration. The scripts provided in this project showcase how to leverage Bash to automate tasks, extract specific information, and streamline workflows.

## Project Overview

In this project, you'll find a variety of Bash scripts designed to interact with your system and perform useful tasks. One notable script is `show_ip`, which demonstrates how to extract and display the IP address of the `eth0` network interface using a combination of standard Unix utilities such as `ifconfig`, `grep`, and `awk`.

The scripts in this project serve as practical examples of how Bash can be used to simplify and automate tasks. They cover different aspects of system administration, including:

- **Network Information**: Extracting and displaying specific network-related details.
- **Text Processing**: Using tools like `grep` and `awk` to filter and manipulate text.
- **Piping and Chaining Commands**: Combining multiple commands to achieve complex results.

## How to Use the Scripts

To use the scripts provided in this project:

1. Copy the below code.
2. Navigate to the project directory.
3. Review the scripts and modify them as needed for your system.
4. Make the scripts executable using the command `chmod +x script_name.sh`.
5. Execute the scripts using the command `./script_name.sh`.

```
#! /bin/bash


# Run the ifconfig command and filter the output
ifconfig_output=$(ifconfig)

# Use grep to find the line with the eth0 interface and the inet (IPv4) address
ip_address=$(echo "$ifconfig_output" | grep 'eth0' -A 1 | grep 'inet ' | awk '{print $2}')

# Print the IP address
echo "$ip_address"
```

For convenience, you can also define aliases in your shell configuration file to quickly run the scripts. For example, the `show_ip` alias can be defined as follows:

```
alias show_ip='ifconfig | grep "eth0" -A 1 | grep "inet " | awk "{print \$2}"'
```

## Conclusion

This mini project is a great starting point for learning Bash scripting and how it can be used for network and system administration tasks. Feel free to explore the scripts, modify them to suit your needs, and use them as a foundation for your own projects