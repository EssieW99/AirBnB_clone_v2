#!/usr/bin/env bash
#Installs and configures nginx on a server
#Install nginx
sudo apt-get update -y
sudo apt-get install -y nginx

# #firewall config
sudo ufw allow 'Nginx HTTP'

#Configure paths
sudo mkdir -p /data/web_static/releases/test/
sudo mkdir -p /data/web_static/shared/

#Update permissions
sudo chown -R "ubuntu":"ubuntu" /data/

#create index.html file
sudo echo "<html>
  <head>
  </head>
  <body>
    Holberton School
  </body>
</html>" | sudo tee /data/web_static/releases/test/index.html

#create symbolic links
sudo ln -s /data/web_static/releases/test  /data/web_static/current

#Remove old config
sudo rm /etc/nginx/sites-enabled/default


#Update nginx.config
sudo echo "
server {
        listen 80 default_server;
        listen [::]:80 default_server;

        # SSL configuration
        #
        # listen 443 ssl default_server;
        # listen [::]:443 ssl default_server;
        root /var/www/html;

        index index.html index.htm index.nginx-debian.html;

        server_name _;
        rewrite ^/redirect_me https://www.youtube.com/ permanent;
        error_page 404 /custom_404.html;
        location = /custom_404.html {
            root /usr/share/nginx/html;
            internal;
        }


        location / {
                # First attempt to serve request as file, then
                # as directory, then fall back to displaying a 404.
                try_files $uri $uri/ =404;
                add_header X-Served-By "473257-web-01";
        }

        location = /hbnb_static/ {
                alias /data/web_static/current/;
                add_header X-Served-By "473257-web-01";
        }
}" | sudo tee /etc/nginx/sites-available/default

#create new symbolic link
sudo ln -s /etc/nginx/sites-available/default /etc/nginx/sites-enabled/default

#Restart nginx/data/web_static/releases/test
sudo systemctl restart nginx
