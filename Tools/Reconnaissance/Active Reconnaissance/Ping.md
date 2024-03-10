Ping should remind you of the game ping-pong (table tennis). You throw the ball and expect to get it back. The primary purpose of ping is to check whether you can reach the remote system and that the remote system can reach you back. In other words, initially, this was used to check network connectivity; however, we are more interested in its different uses: checking whether the remote system is online.

In simple terms, the ping command sends a packet to a remote system, and the remote system replies. This way, you can conclude that the remote system is online and that the network is working between the two systems.

If you prefer a pickier definition, the ping is a command that sends an ICMP Echo packet to a remote system. If the remote system is online, and the ping packet was correctly routed and not blocked by any firewall, the remote system should send back an ICMP Echo Reply. Similarly, the ping reply should reach the first system if appropriately routed and not blocked by any firewall.

The objective of such a command is to ensure that the target system is online before we spend time carrying out more detailed scans to discover the running operating system and services.

On your AttackBox terminal, you can start to use ping as `ping 10.10.143.17` or `ping HOSTNAME`. In the latter, the system needs to resolve HOSTNAME to an IP address before sending the ping packet. If you don’t specify the count on a Linux system, you will need to hit `CTRL+c` to force it to stop. Hence, you might consider `ping -c 10 10.10.143.17` if you just want to send ten packets. This is equivalent to `ping -n 10 10.10.143.17` on a MS Windows system.

Technically speaking, ping falls under the protocol ICMP (Internet Control Message Protocol). ICMP supports many types of queries, but, in particular, we are interested in ping (ICMP echo/type 8) and ping reply (ICMP echo reply/type 0). Getting into ICMP details is not required to use ping.

In the following example, we have specified the total count of packets to 5. From the AttackBox’s terminal, we started pinging `10.10.143.17`. We learned that `10.10.143.17` is up and is not blocking ICMP echo requests. Moreover, any firewalls and routers on the packet route are not blocking ICMP echo requests either.

![[Pasted image 20231003195243.png]]
