#!/usr/bin/python3
'''Places items from the web_static
folder into a tgz archive
'''
from fabric.api import *


env.hosts = ['localhost']


def do_pack():
    # add files from web_static to tgz archive
    # all archives are stored in /versions in the archive
    run("mkdir versions/")
    # name of archive to follow format
    # web_static_<year><month><day><hour><minute><secon\d>.tgz
    timestamp = dt.now().strftime("%Y_%m_%d_%H_%M_%S")
    name = "web_static_" + timestamp + ".tgz"
    result = run("tar -czvf /versions/name.tgz /web_static")
    # returns correctly generated archive on success
    if result.succeeded:
        return (result)
    # else none
    else:
        return(None)
