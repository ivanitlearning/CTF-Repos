# Subdomain enumeration

We have some subdomain lists in

```text
root@Kali:~/HTB/Mango# grep staging-order /usr/share/seclists/Discovery/DNS/*
/usr/share/seclists/Discovery/DNS/dns-Jhaddix.txt:staging-order
/usr/share/seclists/Discovery/DNS/dns-Jhaddix.txt:www.staging-order
```

Note the subdomain can't be found with dirbuster wordlists

```text
root@Kali:~/HTB/Mango# grep staging-order /usr/share/dirbuster/wordlists/*
```

While gobuster has the vhost option for subdomain enumeration...

```plaintext
root@Kali:~/HTB/Mango# gobuster vhost -u mango.htb -w /usr/share/seclists/Discovery/DNS/dns-Jhaddix.txt
===============================================================
Gobuster v3.0.1
by OJ Reeves (@TheColonial) & Christian Mehlmauer (@_FireFart_)
===============================================================
[+] Url:          http://mango.htb
[+] Threads:      10
[+] Wordlist:     /usr/share/seclists/Discovery/DNS/dns-Jhaddix.txt
[+] User Agent:   gobuster/3.0.1
[+] Timeout:      10s
===============================================================
2020/10/31 20:23:53 Starting gobuster
===============================================================
Found: *.0.mango.htb (Status: 400) [Size: 442]
Found: *.*.mango.htb (Status: 400) [Size: 442]
Found: 00.mango.htb (Status: 403) [Size: 277]
Found: .........mango.htb (Status: 400) [Size: 442]
Found: ...mango.htb (Status: 400) [Size: 442]
```

There was no option to exclude/include status codes:

```text
root@Kali:~/HTB/Mango# gobuster vhost -h
Uses VHOST bruteforcing mode

Usage:
  gobuster vhost [flags]

Flags:
  -c, --cookies string        Cookies to use for the requests
  -r, --followredirect        Follow redirects
  -H, --headers stringArray   Specify HTTP headers, -H 'Header1: val1' -H 'Header2: val2'
  -h, --help                  help for vhost
  -k, --insecuressl           Skip SSL certificate verification
  -P, --password string       Password for Basic Auth
  -p, --proxy string          Proxy to use for requests [http(s)://host:port]
      --timeout duration      HTTP Timeout (default 10s)
  -u, --url string            The target URL
  -a, --useragent string      Set the User-Agent string (default "gobuster/3.0.1")
  -U, --username string       Username for Basic Auth

Global Flags:
  -z, --noprogress        Don't display progress
  -o, --output string     Output file to write results to (defaults to stdout)
  -q, --quiet             Don't print the banner and other noise
  -t, --threads int       Number of concurrent threads (default 10)
  -v, --verbose           Verbose output (errors)
  -w, --wordlist string   Path to the wordlist
```

## wfuzz subdomain enum

Alternatively we could use `wfuzz`. Install/upgrade with `apt install wfuzz`. If you find you need a newer version of **pyparsing**, upgrade the Python package with `pip3 install pyparsing -U`. Unfortunately, I was unable to discover the subdomain even though it was on the wordlist

```text
root@Kali:~/HTB/Mango# wfuzz -w /usr/share/seclists/Discovery/DNS/dns-Jhaddix.txt -H "Host: FUZZ.mango.htb" --hc 403,400 -t 150 10.10.10.162
 /usr/lib/python3/dist-packages/wfuzz/__init__.py:34: UserWarning:Pycurl is not compiled against Openssl. Wfuzz might not work correctly when fuzzing SSL sites. Check Wfuzz's documentation for more information.
********************************************************
* Wfuzz 3.0.1 - The Web Fuzzer                         *
********************************************************

Target: http://10.10.10.162/
Total requests: 2178751

===================================================================
ID           Response   Lines    Word     Chars       Payload                                                                              
===================================================================

Killed
```

Running it with fewer threads also killed

```text
root@Kali:~/HTB/Mango# wfuzz -w /usr/share/seclists/Discovery/DNS/dns-Jhaddix.txt -H "Host: FUZZ.mango.htb" --hc 403,400 -t 80 10.10.10.162
 /usr/lib/python3/dist-packages/wfuzz/__init__.py:34: UserWarning:Pycurl is not compiled against Openssl. Wfuzz might not work correctly when fuzzing SSL sites. Check Wfuzz's documentation for more information.
********************************************************
* Wfuzz 3.0.1 - The Web Fuzzer                         *
********************************************************

Target: http://10.10.10.162/
Total requests: 2178751

===================================================================
ID           Response   Lines    Word     Chars       Payload                                                                              
===================================================================

Killed
```

But if you run on a much shorter list (I cherry picked 5 words including the answer) it works

```
root@Kali:~/HTB/Mango# wfuzz -w list -H "Host: FUZZ.mango.htb" --hc 403,400 -t 80 10.10.10.162
 /usr/lib/python3/dist-packages/wfuzz/__init__.py:34: UserWarning:Pycurl is not compiled against Openssl. Wfuzz might not work correctly when fuzzing SSL sites. Check Wfuzz's documentation for more information.
********************************************************
* Wfuzz 3.0.1 - The Web Fuzzer                         *
********************************************************

Target: http://10.10.10.162/
Total requests: 5

===================================================================
ID           Response   Lines    Word     Chars       Payload                                                                              
===================================================================

000000003:   200        209 L    403 W    4022 Ch     "staging-order"                                                                      

Total time: 0
Processed Requests: 5
Filtered Requests: 4
Requests/sec.: 0
```

Why? No idea.