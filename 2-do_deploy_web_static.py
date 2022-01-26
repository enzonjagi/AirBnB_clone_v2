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
        file_name = archive_path.split("/")[-1].split(".")[0]
        put(archive_path, "/tmp/")

        run("mkdir -p /data/web_static/releases/{}".format(file_name))

        run("tar -xzf /tmp/{}.tgz -C /data/web_static/releases/{}/".
            format(file_name, file_name))

        run('rm -rf /tmp/{}.tgz'.format(file_name))

        run(('mv /data/web_static/releases/{}/web_static/* ' +
             '/data/web_static/releases/{}/').
            format(file_name, file_name))

        run('rm -rf /data/web_static/releases/{}/web_static'.
            format(file_name))

        run('rm -rf /data/web_static/current')

        run(('ln -s /data/web_static/releases/{}/' +
             ' /data/web_static/current').
            format(file_name))

        return(True)
    except Exception:
        return (False)
