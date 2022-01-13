#!/usr/bin/env bash
#0. Prepare your web servers

sudo apt update
sudo apt -y install nginx

sudo mkdir -p /data/web_static/releases/test/
sudo touch /data/web_static/releases/test/index.html
sudo rm /etc/nginx/sites-enabled/default

html5="
<html>
  <head>
  </head>
  <body>
    Holberton School
  </body>
</html>
"

sudo echo "$html5" | sudo tee /data/web_static/releases/test/index.html
ln -sf /data/web_static/releases/test/ /data/web_static/current
sudo chown ubuntu /data/
sudo chgrp ubuntu /data/
sudo sed -i '/listen 80 default_server;
	     a location /hbnb_static/ {
	     alias /data/web_static/current/;}' /etc/nginx/sites-available/default
sudo service nginx restart
