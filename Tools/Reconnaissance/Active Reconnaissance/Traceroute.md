As the name suggests, the traceroute command _traces the route_ taken by the packets from your system to another host. The purpose of a traceroute is to find the IP addresses of the routers or hops that a packet traverses as it goes from your system to a target host. This command also reveals the number of routers between the two systems. It is helpful as it indicates the number of hops (routers) between your system and the target host. However, note that the route taken by the packets might change as many routers use dynamic routing protocols that adapt to network changes.

On Linux and macOS, the command to use is `traceroute 10.10.143.17`, and on MS Windows, it is `tracert 10.10.143.17`. `traceroute` tries to discover the routers across the path from your system to the target system.

There is no direct way to discover the path from your system to a target system. We rely on ICMP to “trick” the routers into revealing their IP addresses. We can accomplish this by using a small Time To Live (TTL) in the IP header field. Although the T in TTL stands for time, TTL indicates the maximum number of routers/hops that a packet can pass through before being dropped; TTL is not a maximum number of time units. When a router receives a packet, it decrements the TTL by one before passing it to the next router. The following figure shows that each time the IP packet passes through a router, its TTL value is decremented by 1. Initially, it leaves the system with a TTL value of 64; it reaches the target system with a TTL value of 60 after passing through 4 routers.

![[e82c42dcfae78ac592a8d7843465d2d6.png]]
```shell-session
traceroute tryhackme.com
```

