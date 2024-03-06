#!/usr/bin/python3
"""Compresses the webstatic files into an archive"""
from fabric.api import *
from datetime import datetime


@task
def do_pack(ctx):
    """Use run the compress command tar"""
    archive_name = f"web_static_{datetime.now()}.tgz"
    res = local(f"tar -c /versions/{archive_name} web_static/ ")

    if res.failed:
        print(f"Packing web_static to versions/{archive_name}")
    else:
        return None
