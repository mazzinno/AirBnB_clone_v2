#!/usr/bin/python3
"""
Deploy web files to server
"""
from fabric.api import *
from datetime import datetime
from time import strftime
from os import path

env.hosts = ['100.26.237.194', '34.239.255.112']
env.user = 'ubuntu'
env.key_filename = '/home/id_rsa'


def do_pack():
    """
    script that generates a .tgz archive from the
    contents of the web_static folder
    """
    file_name = strftime("%Y%m%d%H%M%S")
    try:
        local("mkdir -p versions")
        local(f"tar -czvf versions/web_static_{file_name}.tgz web_static/")
        return f"versions/web_static_{file_name}.tgz"

    except Exception as e:
        return None


def do_deploy(archive_path):
    """
    Deploy web files to server
    """
    try:
        if not (path.exists(archive_path)):
            return False

        # upload archive to server
        put(archive_path, '/tmp/')

        # create target dir
        timestamp = archive_path[-18:-4]
        run(f'sudo mkdir -p /data/web_static/\
releases/web_static_{timestamp}/')

        # uncompress archive and delete .tgz
        run(f'sudo tar -xzf /tmp/web_static_{timestamp}.tgz -C \
/data/web_static/releases/web_static_{timestamp}/')

        # remove archive
        run(f'sudo rm /tmp/web_static_{timestamp}.tgz')

        # move contents into host web_static
        run(f'sudo mv /data/web_static/releases/web_static_{timestamp}\
/web_static/* /data/web_static/releases/web_static_{timestamp}/')

        # remove extraneous web_static dir
        run(f'sudo rm -rf /data/web_static/releases/\
web_static_{timestamp}/web_static')

        # delete pre-existing sym link
        run('sudo rm -rf /data/web_static/current')

        # re-establish symbolic link
        run(f'sudo ln -s /data/web_static/releases/\
web_static_{timestamp}/ /data/web_static/current')
    except Exception:
        return False

    # return True
    return True


def deploy():
    """
    Create and distribute an archive to a web server.
    """
    file = do_pack()
    if file is None:
        return False
    return do_deploy(file)
