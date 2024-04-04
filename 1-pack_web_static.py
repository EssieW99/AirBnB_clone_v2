#!/usr/bin/python3
"""
generates a .tgz archive from the contents of the web_static folder
of your AirBnB Clone repo, using the function do_pack
"""
from datetime import datetime
from fabric.api import local
import os


def do_pack():
    """ generates a .tgz archive from web_static folder"""

    try:
        date = datetime.now().strftime('%Y%m%d%H%M%S')
        if not os.path.exists('versions'):
            local('mkdir versions')
        filename = "versions/web_static_{}.tgz".format(date)
        local("tar -cvzf {} web_static".format(filename))
        return filename
    except:
        return None
