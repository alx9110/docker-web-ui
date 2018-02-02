""" RQ Tasks """
from subprocess import Popen, PIPE


def build_from_git(url):
    """ Task for auto-build from GIT repo """
    tmp_name = url.replace('.git', '').split('/')[-1]
    # Stage1: git clone
    clone = Popen('/usr/bin/git clone {0} /tmp/{1}'.format(url, tmp_name),
                shell=True, stdout=PIPE, universal_newlines=True
               )
    # Stage2: docker build
    build = Popen('docker build -t {0} /tmp/{0}'.format(tmp_name),
                shell=True, stdout=PIPE, universal_newlines=True
               )
    # Stage3: clean workdir
    clean = Popen('rm -R /tmp/{0}'.format(tmp_name),
                shell=True, stdout=PIPE, universal_newlines=True
               )
    return clone.stdout.read() + build.stdout.read() + clean.stdout.read()
