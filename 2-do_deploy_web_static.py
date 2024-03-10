#!usr/bin/python3
"""Deploys an archive to a remote host"""
from fabric.api import put, sudo, run, env
from fabric import exceptions
from os import path

env.hosts = ["54.237.82.60", "100.27.4.209"]
env.user = "ubuntu"


def do_deploy(archive_path):
    """Deploys an archive to a specified remote(s) host(s)"""
    if not path.exists(archive_path):
        return False

    try:
        archive_name = path.basename(archive_path)
        archive_no_ext, ext = path.splitext(archive_name)
        put("{}".format(archive_path), "/tmp/{}".format(archive_name), mode=755)
        run("mkdir -p /data/web_static/releases/{}".format(archive_no_ext))
        sudo(
            f"tar -xzvf /tmp/{archive_name} -C /data/web_static/releases/{archive_no_ext}/")
        sudo("rm /tmp/{}".format(archive_name))
        sudo("rm /data/web_static/current")
        sudo(
            f"ln -s /data/web_static/releases/{archive_no_ext} /data/web_static/current")
        return True
    except exceptions.CommandTimeout as e:
        return False
