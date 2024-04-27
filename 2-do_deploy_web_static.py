#!/usr/bin/python3
"""
distributes an archive to your web servers
"""
from datetime import datetime
from fabric.api import *
from os.path import basename, exists, splitext

env.hosts = ['34.203.29.35', '100.25.3.77']
env.user = 'ubuntu'
env.key = '~/.ssh/school'


def do_pack():
    """ generates a .tgz archive from web_static folder"""

    try:
        date = datetime.now().strftime('%Y%m%d%H%M%S')
        if not exists('versions'):
            local('mkdir versions')
        filename = "versions/web_static_{}.tgz".format(date)
        local("tar -cvzf {} web_static".format(filename))
        return filename
    except Exception:
        return None


def do_deploy(archive_path):
    """ distributes an archive to your web servers"""

    """ check if path exists"""
    path_exists = exists(archive_path)
    if path_exists is False:
        return False

    try:
        """ get last component of the path"""
        filename = basename(archive_path)

        """ split filename into base name and extension"""
        name_no_ext, _ = splitext(filename)

        """ where archive should be uncompressed"""
        folder = f"/data/web_static/releases/{name_no_ext}"

        """ upload archive to /tmp/ directory"""
        put(archive_path, '/tmp/')

        run('mkdir -p {}'.format(folder))

        """ uncompress the archive from where it is to where you want to be"""
        run('tar -xzf /tmp/{} -C {}/'.format(filename, folder))

        run('rm /tmp/{}'.format(filename))

        """
        move all files and directories within web_static directory to the
        root of the deployment folder
        """
        run('mv {}/web_static/* {}'.format(folder, folder))

        """ delete the web_static directory"""
        run('rm -rf {}/web_static'.format(folder))

        """ delete the symbolic link from the servers"""
        run('rm -rf /data/web_static/current')

        """
        create a new symbolic link linked to the new version of the code
        """
        run(f'ln -s {folder}/ /data/web_static/current')

        return True
    except Exception:
        return False
