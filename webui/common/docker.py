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
        self.created = self.raw[3:7]
        self.status = self.raw[8]
        self.port = self.raw[8]
        self.names = self.raw[9]