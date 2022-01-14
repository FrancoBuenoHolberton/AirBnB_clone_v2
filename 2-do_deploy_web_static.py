#!/usr/bin/python3
"""
1. Compress before sending
"""
from fabric.api import *
from os.path import *
env.hosts = ['34.138.247.205', '34.74.60.97']

def do_deploy(archive_path):
    if exists(archive_path) is False:
        return False
    else:
        try:
            filename = archive_path.split("/")[-1]
            extension = archive_path.split(".")[0]
            path = "/data/web_static/releases/"
            put(archive_path, '/tmp/')
            run('mkdir -p {}{}/'.format(filename, extension))
            run('tar -xzf /tmp/{} -C {}{}/',format(filename, path, extension))
            run('rm /tmp/{}'.format(filename))
            run('mv {0}{1}/web_static/* {0}{1}/'.format(filename, extension))
            run('rm -rf {}{}/web_static'.format(path, extension))
            run('rm -rf /data/web_static/current')
            run('ln -s {}{}/ /data/web_static/current'.format(path, extension))
            return True
        except:
            return False

