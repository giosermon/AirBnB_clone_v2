#!/usr/bin/env bash
# set new release in /data
# Install nginx
apt-get update
apt-get install nginx -y

# set nginx config
CONFIG_PATH=/etc/nginx/sites-available/default
NEW="location /hbnb_static {alias /data/web_static/current/;}"
sed -i "29i $NEW" $CONFIG_PATH

# create folders
mkdir -p /data/web_static/releases/
mkdir -p /data/web_static/shared/
mkdir -p /data/web_static/releases/test/
# Load html content
echo "Fake content" >/data/web_static/releases/test/index.html
ln -sfn /data/web_static/releases/test/ /data/web_static/current
chown -R ubuntu:ubuntu /data
service nginx restart
