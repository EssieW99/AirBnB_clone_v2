#!/usr/bin/python3
"""Creates an archive and uploads it to the server"""
from fabric import exceptions
from fabric.api import env, runs_once, local
from time import strftime

upload = __import__('2-do_deploy_web_static').do_deploy

env.hosts = ["54.237.82.60", "100.27.4.209"]
env.user = "ubuntu"


@runs_once
def do_pack():
    """Archive the web_static folder"""
    filename = strftime("%Y%m%d%H%M%S")
    archive_path = "versions/web_static_{}.tgz".format(filename)

    try:
        local("mkdir -p versions")
        local("tar -czvf {} web_static/".format(archive_path))
        return archive_path
    except exceptions.CommandExecutionError as e:
        print(e)
        return None


def deploy():
    """Creates an archive and uploads to servers"""
    archive = do_pack()
    if archive is None:
        return False
    deployment = upload(archive)
    return deployment
