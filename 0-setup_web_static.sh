#!/usr/bin/env bash

# A Bash script that sets up my web servers for the deployment of web_static

# Install Nginx if not already installed
if ! command -v nginx &> /dev/null
then
    sudo apt-get update
    sudo apt-get -y install nginx
fi

# Create necessary folders if they don't exist
sudo mkdir -p /data/web_static/releases/test /data/web_static/shared

# Create fake HTML file for testing
echo "<html>
  <head>
  </head>
  <body>
    <p>Hello, this is a test index.html file!</p>
  </body>
</html>" | sudo tee /data/web_static/releases/test/index.html > /dev/null

# Create symbolic link
sudo ln -sf /data/web_static/releases/test /data/web_static/current

# Set ownership recursively to ubuntu user and group
sudo chown -R ubuntu:ubuntu /data/

# Update Nginx configuration
sudo sed -i '/^\tlocation \/ {/a \
\t\tlocation /hbnb_static/ {\
\t\t\talias /data/web_static/current/;\
\t\t}' /etc/nginx/sites-available/default

# Restart Nginx
sudo service nginx restart
