#!/usr/bin/python3
"""Compresses the webstatic files into an archive"""
from fabric.api import local
import fabric
from time import strftime


def do_pack():
    """Archive the web_static folder"""
    filename = strftime("%Y%m%d%H%M%S")
    archive_path = "versions/web_static_{}.tgz".format(filename)

    try:
        local("mkdir -p versions")
        local("tar -czvf {} web_static/".format(archive_path))
        return archive_path
    except fabric.exceptions.CommandExecutionError as e:
        print(e)
        return None
