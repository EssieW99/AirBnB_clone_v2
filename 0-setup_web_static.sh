#!/usr/bin/env bash
#Installs and configures nginx on a server
#Install nginx
sudo apt update -y
sudo apt install -y nginx

#firewall config
sudo ufw allow 'Nginx HTTP'

#Configure paths
sudo mkdir -P /data/web_static/releases/test/
sudo mkdir -P /data/web_static/shared/

#Update permissions
sudo chown -R "ubuntu":"ubuntu" /data/

#create index.html file
echo "<html>
  <head>
  </head>
  <body>
    Holberton School
  </body>
</html>" > /data/web_static/releases/test/index.html

#create symbolic links
ln -s /data/web_static/releases/test  /data/web_static/current


#Update nginx.config
sudo sed -i '0,/server {/a \
   location \/hbnb_static\/ { \
      alias /data/web_static/current; \
   }' /etc/nginx/sites-available/default

#Restart nginx/data/web_static/releases/test
sudo systemctl restart nginx
