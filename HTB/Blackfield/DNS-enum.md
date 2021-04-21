# DNS enumeration

We can confirm the domain of the box from CME is correct

```text
root@kali:~/CTF/HTB/Blackfield# nslookup blackfield.local 10.10.10.192
Server:         10.10.10.192
Address:        10.10.10.192#53

Name:   blackfield.local
Address: 10.10.10.192
Name:   blackfield.local
Address: dead:beef::f566:8f53:2a0e:ca16
```

but no way to do a DNS zone transfer

```text
root@kali:~/CTF/HTB/Blackfield# host -t axfr blackfield.local 10.10.10.192
Trying "blackfield.local"
Using domain server:
Name: 10.10.10.192
Address: 10.10.10.192#53
Aliases:

Host blackfield.local not found: 5(REFUSED)
; Transfer failed.
```

