# nmap NSE scripts for MS-SQL

First let's run all the ms-sql scripts against the service and see what we get.

```shell
root@Kali:~/HTB/Querier# nmap -Pn -n -sV -p1433 --script=*ms-sql* 10.10.10.125 -e tun0
Starting Nmap 7.80 ( https://nmap.org ) at 2020-11-08 01:16 +08
Nmap scan report for 10.10.10.125
Host is up (0.0053s latency).

PORT     STATE SERVICE  VERSION
1433/tcp open  ms-sql-s Microsoft SQL Server 2017 14.00.1000.00; RTM
| ms-sql-brute: 
|   [10.10.10.125:1433]
|_    No credentials found
| ms-sql-config: 
|   [10.10.10.125:1433]
|_    ERROR: No login credentials
| ms-sql-dump-hashes: 
| [10.10.10.125:1433]
|_  ERROR: No login credentials
| ms-sql-hasdbaccess: 
|   [10.10.10.125:1433]
|_    ERROR: No login credentials.
| ms-sql-ntlm-info: 
|   Target_Name: HTB
|   NetBIOS_Domain_Name: HTB
|   NetBIOS_Computer_Name: QUERIER
|   DNS_Domain_Name: HTB.LOCAL
|   DNS_Computer_Name: QUERIER.HTB.LOCAL
|   DNS_Tree_Name: HTB.LOCAL
|_  Product_Version: 10.0.17763
| ms-sql-query: 
|   (Use --script-args=ms-sql-query.query='<QUERY>' to change query.)
|   [10.10.10.125:1433]
|_    ERROR: No login credentials
| ms-sql-tables: 
|   [10.10.10.125:1433]
|_    ERROR: No login credentials.
| ms-sql-xp-cmdshell: 
|   (Use --script-args=ms-sql-xp-cmdshell.cmd='<CMD>' to change command.)
|   [10.10.10.125:1433]
|_    ERROR: No login credentials.

Host script results:
| ms-sql-info: 
|   10.10.10.125:1433: 
|     Version: 
|       name: Microsoft SQL Server 2017 RTM
|       number: 14.00.1000.00
|       Product: Microsoft SQL Server 2017
|       Service pack level: RTM
|       Post-SP patches applied: false
|_    TCP port: 1433

Service detection performed. Please report any incorrect results at https://nmap.org/submit/ .
Nmap done: 1 IP address (1 host up) scanned in 593.10 seconds
```

That returned nothing we didn't already know. How about running [ms-sql-config](https://nmap.org/nsedoc/scripts/ms-sql-config.html) with creds found in the xlsm file?

```shell
root@Kali:~/HTB/Querier# nmap -Pn -n -p1433 --script ms-sql-config --script-args mssql.username=reporting,mssql.password=PcwTWTHRwryjc$c6 10.10.10.125
Starting Nmap 7.80 ( https://nmap.org ) at 2020-11-08 02:20 +08
Nmap scan report for 10.10.10.125
Host is up (0.013s latency).

PORT     STATE SERVICE
1433/tcp open  ms-sql-s
| ms-sql-config: 
|   [10.10.10.125:1433]
|_    ERROR: Bad username or password

Nmap done: 1 IP address (1 host up) scanned in 0.30 seconds
root@Kali:~/HTB/Querier# nmap -Pn -n -p1433 --script ms-sql-config --script-args mssql.username=luis,mssql.password=PcwTWTHRwryjc$c6 10.10.10.125
Starting Nmap 7.80 ( https://nmap.org ) at 2020-11-08 02:20 +08
Nmap scan report for 10.10.10.125
Host is up (0.0082s latency).

PORT     STATE SERVICE
1433/tcp open  ms-sql-s
| ms-sql-config: 
|   [10.10.10.125:1433]
|_    ERROR: Bad username or password

Nmap done: 1 IP address (1 host up) scanned in 0.28 seconds
```

Wasn't able to authenticate with it, not even when I included/omitted the domain, used **reporting** instead of **luis**, quoted the username, password etc.

```shell
root@Kali:~/HTB/Querier# nmap -Pn -n -sV -p1433 --script ms-sql-config --script-args mssql.username="querier\reporting",mssql.password="PcwTWTHRwryjc$c6" 10.10.10.125
Starting Nmap 7.80 ( https://nmap.org ) at 2020-11-13 14:40 +08
Nmap scan report for 10.10.10.125
Host is up (0.19s latency).

PORT     STATE SERVICE  VERSION
1433/tcp open  ms-sql-s Microsoft SQL Server 2017 14.00.1000.00; RTM
| ms-sql-config: 
|   [10.10.10.125:1433]
|_    ERROR: Bad username or password

Service detection performed. Please report any incorrect results at https://nmap.org/submit/ .
Nmap done: 1 IP address (1 host up) scanned in 7.84 seconds

root@Kali:~/HTB/Querier# nmap -Pn -n -sV -p1433 --script ms-sql-hasdbaccess --script-args mssql.username="querier\\reporting",mssql.password='PcwTWTHRwryjc$c6' 10.10.10.125
Starting Nmap 7.80 ( https://nmap.org ) at 2020-11-13 14:42 +08
Nmap scan report for 10.10.10.125
Host is up (0.12s latency).

PORT     STATE SERVICE  VERSION
1433/tcp open  ms-sql-s Microsoft SQL Server 2017 14.00.1000.00; RTM
| ms-sql-hasdbaccess: 
|_  [10.10.10.125:1433]

Service detection performed. Please report any incorrect results at https://nmap.org/submit/ .
Nmap done: 1 IP address (1 host up) scanned in 7.77 seconds
```

Tried another script unsuccessfully

```shell
root@Kali:~/HTB/Querier# nmap -Pn -n -p1433 --script ms-sql-query --script-args mssql.username=luis,mssql.password=PcwTWTHRwryjc$c6,ms-sql-query.query="SELECT * @@version" 10.10.10.125
Starting Nmap 7.80 ( https://nmap.org ) at 2020-11-08 02:25 +08
Nmap scan report for 10.10.10.125
Host is up (0.0080s latency).

PORT     STATE SERVICE
1433/tcp open  ms-sql-s
| ms-sql-query: 
|   [10.10.10.125:1433]
|_    ERROR: Bad username or password

Nmap done: 1 IP address (1 host up) scanned in 0.27 seconds
root@Kali:~/HTB/Querier# nmap -Pn -n -p1433 --script ms-sql-query --script-args mssql.username=querier/luis,mssql.password=PcwTWTHRwryjc$c6,ms-sql-query.query="SELECT * @@version" 10.10.10.125
Starting Nmap 7.80 ( https://nmap.org ) at 2020-11-08 02:25 +08
Nmap scan report for 10.10.10.125
Host is up (0.0048s latency).

PORT     STATE SERVICE
1433/tcp open  ms-sql-s
| ms-sql-query: 
|   [10.10.10.125:1433]
|_    ERROR: Bad username or password

Nmap done: 1 IP address (1 host up) scanned in 0.29 seconds
root@Kali:~/HTB/Querier# nmap -Pn -n -p1433 --script ms-sql-query --script-args mssql.username=querier\luis,mssql.password=PcwTWTHRwryjc$c6,ms-sql-query.query="SELECT * @@version" 10.10.10.125
Starting Nmap 7.80 ( https://nmap.org ) at 2020-11-08 02:25 +08
Nmap scan report for 10.10.10.125
Host is up (0.0046s latency).

PORT     STATE SERVICE
1433/tcp open  ms-sql-s
| ms-sql-query: 
|   [10.10.10.125:1433]
|_    ERROR: Bad username or password

Nmap done: 1 IP address (1 host up) scanned in 0.29 seconds
```



