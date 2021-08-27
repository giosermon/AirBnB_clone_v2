#!/usr/bin/python3
"""
 Fabric script (based on the file 1-pack_web_static.py)
 that distributes an archive to your web servers,
 using the function do_deploy:
"""


from datetime import datetime
import os
from fabric.api import run, put, env

env.hosts = ['ubuntu@34.139.216.89', 'ubuntu@54.159.25.183']



def do_deploy(archive_path):
    """
    Distributes an archive to the web servers
    """
    # Validate if the archive path does not exist
    if not os.path.exists(archive_path):
        return False
    try:

        split_name = archive_path.split('/')
        file_name = split_name[1]


        put(archive_path, "/tmp/")


        file_path = file_name.split('.')
        file_path = '/data/web_static/releases/' + file_path[0]
        run("mkdir -p {}".format(file_path))
        run("tar -xzf /tmp/{} -C {}".format(file_name, file_path))


        run("rm /tmp/{}".format(file_name))


        file_path_move = file_path + '/web_static'
        run("mv {}/* {}".format(file_path_move, file_path))


        run("rm -rf {}".format(file_path_move))


        run("rm -rf /data/web_static/current")


        run("ln -s {} /data/web_static/current".format(file_path))
        return True
    except:
        return False
