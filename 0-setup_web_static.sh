#!/usr/bin/env bash
# Setup configurations for a customised nginx setup
# sudo apt-get update
# sudo apt-get install -y nginx
# mkdir /data/
sudo mkdir -p /data/web_static/shared/ /data/web_static/releases/test/

# change ownership of data folder to ubuntu ser and group
sudo chown ubuntu:ubuntu /data/*
# simple html file for configuration purposes
echo "<h1>nginx set!!</h2>" >> /data/web_static/releases/test/index.html
# check if symbolink link exists and delete it then install
SYMLINK=/data/web_static/current
if [ -f "$SYMLINK" ]; then
    sudo rm -rf /data/web_static/current;
fi;
sudo ln -s /data/web_static/releases/test/ /data/web_static/current
# change ownership of data folde\r to ubuntu ser and group
sudo chown -hR ubuntu:ubuntu /data/
# Update nginx config to set the above into motion
sudo sed -i '38i\\tlocation /hbnb_static/ {\n\t\talias /data/web_static/current/;\n\t}\n' /etc/nginx/sites-available/default
sudo ln -sf '/etc/nginx/sites-available/default' '/etc/nginx/sites-enabled/default'
# sudo service nginx restart
