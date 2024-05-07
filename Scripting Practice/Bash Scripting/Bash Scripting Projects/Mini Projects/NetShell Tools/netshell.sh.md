```
#! /bin/bash


# Run the ifconfig command and filter the output
ifconfig_output=$(ifconfig)

# Use grep to find the line with the eth0 interface and the inet (IPv4) address
ip_address=$(echo "$ifconfig_output" | grep 'eth0' -A 1 | grep 'inet ' | awk '{print $2}')

# Print the IP address
echo "$ip_address"
```
