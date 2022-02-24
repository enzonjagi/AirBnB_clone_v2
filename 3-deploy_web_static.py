#!/usr/bin/python3
'''Full deployment
Packs files into a .tgz archive
then deploys the .tgz to web servers
later on extracts these files on the web server and
checks if the paths work
'''

from fabric.api import local, run, sudo, env, put
from datetime import datetime
from fabric.decorators import runs_once
from os.path import exists


# set the environment hosts/servers for fabfile to run on
env.hosts = ['44.200.142.218', '34.138.244.202']
# user for both of the servers
env.user = "ubuntu"


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
    result = local("tar -cvzf {} web_static".
                   format(name), capture=True)
    # returns correctly generated archive on success
    if result.succeeded:
        return (name)
    # else none
    else:
        return(None)


def do_deploy(archive_path):
    '''Does the magic of the script'''
    if not exists(archive_path):
        return(False)
    # upload archive to /tmp/ directory
    file = archive_path.split("/")[-1]
    name = file.split(".")[0]

    if put(archive_path, "/tmp/{}".format(file)).failed is True:
        return False
    if run("rm -rf /data/web_static/releases/{}/".
           format(name)).failed is True:
        return False
    if run("mkdir -p /data/web_static/releases/{}/".
           format(name)).failed is True:
        return False
    if run("tar -xzf /tmp/{} -C /data/web_static/releases/{}/".
           format(file, name)).failed is True:
        return False
    if run("rm /tmp/{}".format(file)).failed is True:
        return False
    if run("mv /data/web_static/releases/{}/web_static/* "
           "/data/web_static/releases/{}/".format(name, name)).failed is True:
        return False
    if run("rm -rf /data/web_static/releases/{}/web_static".
           format(name)).failed is True:
        return False
    if run("rm -rf /data/web_static/current").failed is True:
        return False
    if run("ln -s /data/web_static/releases/{}/ /data/web_static/current".
           format(name)).failed is True:
        return False
    return True


def deploy():
    '''Perform a full deploymeny by calling
    do_pack() and do_deploy()
    '''
    file = do_pack()
    if file is None:
        return False
    return do_deploy(file)
