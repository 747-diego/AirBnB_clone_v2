#!/usr/bin/python3
"""Write a Fabric script that generates a .tgz archive."""
import os
from fabric.api import *
from datetime import datetime


def do_pack():
    """Compress before sending."""
    try:
        PathOfFile = datetime.now().strftime("%Y%m%d%H%M%S") + '.tgz'
        os.mkdir('versions/')

        local("tar -fvcz versions/web_static_{} web_static".format(PathOfFile))
    except:
        return None
