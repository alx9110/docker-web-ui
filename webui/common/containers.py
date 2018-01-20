import json


class Container(object):
    """ Extended Container Class """
    def __init__(self, instance):
        self.instance = instance
        self.stats = json.loads(next(instance.stats()), encoding='utf-8')
        self.cpu_stats = self.stats['cpu_stats']
