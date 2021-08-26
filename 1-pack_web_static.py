#!/usr/bin/python3
""" compress folder with fabric module """
from os import path
from fabric.api import local
from datetime import datetime

VERSION_PATH = "./versions"
MKDIR_FOLDER = "mkdir {}"
DATE_FORMAT = "%Y%m%d%H%M%S"


def do_pack():
    """ Compress web_static folder"""
    # validate folder
    if not path.exists(VERSION_PATH):
        local(MKDIR_FOLDER.format(VERSION_PATH))
    # get now and get format to filename
    current_time = datetime.now()
    date_format = current_time.strftime(DATE_FORMAT)
    filename = "web_static_{}.tgz".format(date_format)
    # compress
    try:
        local("tar -cvzf {}/{} /data/web_static/".format(VERSION_PATH, filename))
        return filename
    except:
        return None
