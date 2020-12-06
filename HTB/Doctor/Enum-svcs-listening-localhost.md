# Enumerating services listening on localhost

linpeas tells us there's something listening on localhost:5000

```shell
tcp        0      0 127.0.0.1:5000          0.0.0.0:*               LISTEN      -                   
```

But if you read the [vhost config file](https://github.com/ivanitlearning/CTF-Repos/blob/master/HTB/Doctor/vhost_config.md) this is the webserver to which all Web requests to http://doctors.htb is directed.

```shell
web@doctor /etc/apache2/sites-available $ curl http://127.0.0.1:5000
<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 3.2 Final//EN">
<title>Redirecting...</title>
<h1>Redirecting...</h1>
<p>You should be redirected automatically to target URL: <a href="/login?next=%2F">/login?next=%2F</a>.  If not click the link.
```

