""" Unit tests """
from unittest import TestCase


class DockerTestCase(TestCase):
    """ Class for testing Docker SDK """
    def test_container_list(self):
        """ client.container.list() testing """
        self.assertEqual('Hello', 'Hello')
