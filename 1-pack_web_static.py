#!/usr/bin/python3
"""generates a .tgz archive from web static folder."""
from fabric.api import *
from time import strftime
from datetime import date


def do_pack():
    """
    script that generates a .tgz archive  of
    the contents of the web_static folder.
    """
    file_name = strftime("%Y%m%d%H%M%S")
    try:
        local("mkdir -p versions")
        local(f"tar -czvf versions/web_static_{file_name}.tgz web_static/")
        return f"versions/web_static_{file_name}.tgz"

    except Exception as e:
        return None
