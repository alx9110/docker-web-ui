""" Docker lib """
import subprocess
import json


class Network(object):
    """ Base """
    def __init__(self, raw):
        self.raw = raw.split()
        self.id = self.raw[0]
        self.name = self.raw[1]
        self.driver = self.raw[2]
        self.scope = self.raw[3]

    @property
    def inspect(self):
        res = subprocess.check_output('docker network inspect {0}'.format(self.name),
                                      shell=True).decode()
        return json.loads(res)

class Container(object):
    """ Container """
    def __init__(self, raw):
        self.raw = raw.split()
        self.id = self.raw[0]
        self.image = self.raw[1]
        self.command = self.raw[2]
        self.created = ' '.join(self.raw[3:6])
        self.status = ' '.join(self.raw[6:11])
        self.port = ' '
        self.names = self.raw[-1]
