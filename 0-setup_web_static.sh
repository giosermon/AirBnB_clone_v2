#!/usr/bin/env bash
# set new release in /data
# Install nginx
apt-get update /dev/null
apt-get install nginx -y

# set nginx config
CONFIG_PATH=/etc/nginx/sites-available/default
OLD="server_name localhost;"
NEW="location /hbnb_static {alias /data/web_static/current/;}"
sed -i "/$OLD/a\\$NEW" $CONFIG_PATH

# create folders
mkdir -p /data/web_static/releases/test/
mkdir -p /data/web_static/shared/
mkdir -p /data/web_static/current
# Load html content
echo "Fake content" >/data/web_static/releases/test/index.html
ln -sfn /data/web_static/releases/test/ /data/web_static/current
chown -R ubuntu /data

service nginx restart
