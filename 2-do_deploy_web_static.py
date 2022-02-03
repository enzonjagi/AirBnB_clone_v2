#!/usr/bin/python3
'''A fabfile
responsible for uploading an archive to my web servers
'''


from fabric.api import *
from fabric.decorators import runs_once
from os.path import exists


# set the environment hosts/servers for fabfile to run on
env.hosts = ['35.231.58.85', '34.138.244.202']
# user for both of the servers
env.user = "ubuntu"


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


if __name__ == '__main__':
    archive_path = "versions/web_static_20170315015620.tgz"
    do_deploy(archive_path=archive_path)
