#!/usr/bin/env bash
#0. Prepare your web servers

sudo mkdir /data/web_static/releases/test/
sudo touch /data/web_static/releases/test/index.html
sudo rm /etc/nginx/sites-enabled/default
echo "Html Empty" >
ln -sf /data/web_static/current /data/web_static/releases/test/
sudo chown Ubuntu /data/
sudo chgrp group /data/

    server {
    listen 80 default_server;
    listen [::]:80 default_server;
    add_header X-Served-By $HOSTNAME;
    root   /var/www/html;
    index  index.html index.htm;
    location /redirect_me {
        return 301 http://cuberule.com/;
    }
    error_page 404 /404.html;
    location /404 {
      root /var/www/html;
      internal;
    }
}" > /etc/nginx/sites-available/default
