# Enumerating in /opt

Poking around in /opt I found this.

```shell
web@doctor /opt/clean $ ls -lah
total 52K
drwxrwxr-x 2 root root 4,0K Sep  7 15:36 .
drwxr-xr-x 4 root root 4,0K Sep  6 17:56 ..
-rwxr-xr-x 1 root root  211 Sep  6 16:14 cleandb.py
-rwxr-xr-x 1 root root  129 Jul 26 19:35 clean.py
-rw-r--r-- 1 root root  36K Sep  6 16:12 site.db
web@doctor /opt/clean $ cat clean.py
#!/usr/bin/env python3
import os

os.system('rm /var/www/html/*')
os.system('cp /opt/clean/index.html /var/www/html/index.html')
web@doctor /opt/clean $ cat cleandb.py
#!/usr/bin/env python3
import os

os.system('rm /home/web/blog/flaskblog/site.db')
os.system('cp /opt/clean/site.db /home/web/blog/flaskblog/site.db')
os.system('chown web:web /home/web/blog/flaskblog/site.db')
```

This looks like a cron job which replaces site.db (containing the Web app notes and users). A quick check tells us the DB are the same (or will eventually be the same)

```shell
web@doctor /opt/clean $ diff /home/web/blog/flaskblog/site.db site.db
```

We can also read the DB with `sqlite3` on Kali too.

```shell
root@Kali:~/HTB/Doctor/DBs# sqlite3 clean_site.db
SQLite version 3.27.2 2019-02-25 16:06:06
Enter ".help" for usage hints.
sqlite> .databases
main: /root/HTB/Doctor/DBs/clean_site.db
sqlite> .tables
post  user
sqlite> select * from user;
1|admin|admin@doctor.htb|default.gif|$2b$12$Tg2b8u/elwAyfQOvqvxJgOTcsbnkFANIDdv6jVXmxiWsg4IznjI0S
sqlite> select * from post;
1|Doctor blog|2020-09-18 20:48:37.55555|A free blog to share medical knowledge. Be kind!|1
```

