#!/usr/bin/python3
"""
1. Compress before sending
"""
from fabric.api import *
from datetime import *


def do_pack():
    try:
        local("mkdir -p versions")
        date = datetime.now().strftime("%Y%m%d%H%M%S")
        name = "versions/web_static_{}.tgz".format(date)
        local("tar -cvzf {} web_static".format(name))
        return name
    except:
        return none
