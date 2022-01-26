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


@runs_once
def do_deploy(archive_path):
    '''Does the magic of the script'''
    if not exists(archive_path):
        return(False)
    # upload archive to /tmp/ directory
    try:
        files = archive_path.split("/")[-1].split(".")[0]
        put("archive_path", "/tmp/", use_sudo=True)
        # uncompress the archive to /data/web_static/releases/ directory
        sudo("mkdir -p /data/web_static/releases/{}".format(files))
        sudo("tar -xzf /tmp/{}.tgz /data/web_static/releasese/{}"
             .format(files, files)
             )
        # Delete archive from web server
        sudo("rm -rf /tmp/{}.tgz".format(files))

        # move the extracted contents to /releases/*
        sudo(('mv /data/web_static/releases/{}/web_static/* ' +
              '/data/web_static/releases/{}/').format(files, files))
        # delete the folder
        sudo(('rm -rf /data/web_static/releases/{}/web_static/*'.
              format(files)))
        # delete the symbolic link
        sudo("rm -rf /data/web_static/current")

        # create a new sym link to the new code version
        sudo('ln -s /data/web_static/releases/{}/' +
             ' /data/web_static/current {}'.format(files))

        return(True)
    except Exception:
        return (False)
