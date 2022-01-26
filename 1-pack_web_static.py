#!/usr/bin/python3
'''Places items from the web_static
folder into a tgz archive
'''
from fabric.api import local
from datetime import datetime
from fabric.decorators import runs_once


@runs_once
def do_pack():
    '''packs web_static into a .tgz file'''
    # add files from web_static to tgz archive
    # all archives are stored in /versions in the archive
    local("mkdir -p versions")
    # name of archive to follow format
    # web_static_<year><month><day><hour><minute><secon\d>.tgz
    timestamp = datetime.strftime(datetime.now(), "%Y%m%d%H%M%S")
    name = ("versions/web_static_{}.tgz".
            format(timestamp))
    result = local("tar -cvzf {} /web_static".
                   format(name), capture=True)
    # returns correctly generated archive on success
    if result.succeeded:
        return (name)
    # else none
    else:
        return(None)
