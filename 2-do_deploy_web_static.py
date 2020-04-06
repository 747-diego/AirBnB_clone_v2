#!/usr/bin/python3
"""Fabric script that distributes an archive to the web servers"""

import os
env.hosts = ['35.243.212.54', '3.88.185.245']


def do_deploy(archive_path):
    """Distributes an archive to the web servers"""
    if os.path.exists(archive_path) is False:
        return False

    try:
        put(archive_path, "/tmp/")
        if archive_path[-4:] == ".tgz":
            split_path = archive_path[:-4]
        new_dirctory = "/data/web_static/releases/" + split_path
        run("sudo mkdir -p " + new_dirctory)
        run("sudo tar -xzf /tmp/" + archive_path + " -C " + new_dirctory)
        run("sudo rm /tmp/" + archive_path)
        run("sudo mv " + new_dirctory + "/web_static/*" + new_dirctory)
        run("sudo rm -rf " + new_dirctory + "/web_static")
        run("sudo rm -rf /data/web_static/current")
        run("sudo ln -s " + new_dirctory + " /data/web_static/current")
        return True
    except:
        return False