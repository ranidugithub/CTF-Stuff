
Find the IP address of a domain name using `nslookup`, which stands for Name Server Look Up. You need to issue the command `nslookup DOMAIN_NAME`, for example, `nslookup tryhackme.com`. Or, more generally, you can use `nslookup OPTIONS DOMAIN_NAME SERVER`. These three main parameters are:

- OPTIONS contains the query type as shown in the table below. For instance, you can use `A` for IPv4 addresses and `AAAA` for IPv6 addresses.
- DOMAIN_NAME is the domain name you are looking up.
- SERVER is the DNS server that you want to query. You can choose any local or public DNS server to query. Cloudflare offers `1.1.1.1` and `1.0.0.1`, Google offers `8.8.8.8` and `8.8.4.4`, and Quad9 offers `9.9.9.9` and `149.112.112.112`. There are many [more public DNS servers](https://duckduckgo.com/?q=public+dns) that you can choose from if you want alternatives to your ISP’s DNS servers.

					|Query type |Result|

					|A          |IPv4 Addresses|
					|AAAA       |IPv6 Addresses|
					|CNAME      |Canonical Name|
					|MX         |Mail Servers|
					|SOA        |Start of Authority|
					|TXT        |TXT Records|

For instance, `nslookup -type=A tryhackme.com 1.1.1.1` (or `nslookup -type=a tryhackme.com 1.1.1.1` as it is case-insensitive) can be used to return all the IPv4 addresses used by tryhackme.com.

```shell-session
user@TryHackMe$ nslookup -type=A tryhackme.com 1.1.1.1
Server:		1.1.1.1
Address:	1.1.1.1#53

Non-authoritative answer:
Name:	tryhackme.com
Address: 172.67.69.208
Name:	tryhackme.com
Address: 104.26.11.229
Name:	tryhackme.com
Address: 104.26.10.229
```

## DIG

For more advanced DNS queries and additional functionality, you can use `dig`, the acronym for “Domain Information Groper,” if you are curious. Let’s use `dig` to look up the MX records and compare them to `nslookup`. We can use `dig DOMAIN_NAME`, but to specify the record type, we would use `dig DOMAIN_NAME TYPE`. Optionally, we can select the server we want to query using `dig @SERVER DOMAIN_NAME TYPE`.

- SERVER is the DNS server that you want to query.
- DOMAIN_NAME is the domain name you are looking up.
- TYPE contains the DNS record type, as shown in the table provided earlier.

```
dig @1.1.1.1 tryhackme.com MX
```
![[Pasted image 20231003073211.png]]


