#!/usr/bin/env bash
# Setup configurations for a customised nginx setup
DIR=/data
DIR2=/data/web_static
DIR3=/data/web_static/releases/test
DIR4=/data/web_static/shared
# check if folders exist and set them up
if [ ! -d "$DIR" ] && [ ! -d "$DIR2" ] && [ ! -d "$DIR3" ] && [ ! -d "$DIR4" ];
then
    sudo mkdir /data/
    sudo mkdir /data/web_static/
    sudo mkdir /data/web_static/releases/
    sudo mkdir /data/web_static/shared/
    sudo mkdir /data/web_static/releases/test/
fi
# change ownership of data folder to ubuntu ser and group
sudo chown ubuntu:ubuntu /data/*
# simple html file for configuration purposes
echo "nginx set!!" >> /data/web_static/releases/test/index.html
# check if symbolink link exists and delete it then install
SYMLINK=/data/web_static/current
if [ -f "$SYMLINK" ]; then
    sudo unlink /data/web_static/current
fi
sudo ln -s /data/web_static/releases/test/ /data/web_static/current

# Update nginx config to set the above into motion
sudo sed -i "/listen 80 default_server/a \\\tlocation /hbnb_static { alias /
data/web_static/current; }"  /etc/nginx/sites-available/default
