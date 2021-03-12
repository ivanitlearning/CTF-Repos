# nginx vhost config files

/etc/nginx/sites-available/sneakycorp.htb

```text
server {
        listen 0.0.0.0:80 default_server;
        listen [::]:80 default_server;
        return 301 http://sneakycorp.htb;
        server_name _;
}


server {
        listen 0.0.0.0:80;
        listen [::]:80;

        server_name sneakycorp.htb;

        root /var/www/sneakycorp.htb;
        index index.php;
        location / {
                try_files $uri $uri/ =404;
        }
        location ~ \.php$ {
                include snippets/fastcgi-php.conf;
                fastcgi_pass unix:/run/php/php7.3-fpm.sock;
        }
}

server {
        listen 0.0.0.0:80;
        listen [::]:80;

        server_name dev.sneakycorp.htb;

        root /var/www/dev.sneakycorp.htb/dev;
        index index.php;
        location / {
                try_files $uri $uri/ =404;
        }
        location ~ \.php$ {
                include snippets/fastcgi-php.conf;
                fastcgi_pass unix:/run/php/php7.3-fpm.sock;
        }
}
```

/etc/nginx/sites-available/pypi.sneakycorp.htb

```text
server {
        listen 0.0.0.0:8080 default_server;
        listen [::]:8080 default_server;
        server_name _;
}


server {
        listen 0.0.0.0:8080;
        listen [::]:8080;

        server_name pypi.sneakycorp.htb;

        location / {
                proxy_pass http://127.0.0.1:5000;
                proxy_set_header Host $host;
                proxy_set_header X-Real-IP $remote_addr;
        }
}
```

