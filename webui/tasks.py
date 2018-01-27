from subprocess import Popen, PIPE


def build_from_git(url):
    res = Popen('/usr/bin/git clone {0} /tmp/test-build'.format(url), shell=True, stdout=PIPE, universal_newlines=True)
    return res.stdout.read()
