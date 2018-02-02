""" RQ Tasks """
from subprocess import Popen, PIPE


def build_from_git(url):
    """ Task for auto-build from GIT repo """
    tmp_name = url.replace('.git', '').split('/')[-1]
    cmd = """git clone {0} /tmp/user@{1}&&cd /tmp/user@{1}&&docker build -t user_{1} .&&cd ..&&sudo rm -R user@{1}"""
    # Stage1: git clone
    clone = Popen(cmd.format(url, tmp_name),
                shell=True, stdout=PIPE, universal_newlines=True
               )
    return clone.stdout.read()
