""" Setup """
from os.path import join, dirname
from setuptools import setup, find_packages


requirements = [
    'flask>=0.10',
    'requests',
    'pymongo',
]

setup(
    name='itdctools',
    version='0.1.6',
    author='Alexander Telkov',
    author_email='midiblack@yandex-team.ru',
    install_requires=requirements,
    packages=find_packages(exclude=['tests', 'tests.*']),
    include_package_data=True,
    long_description=open(join(dirname(__file__), 'README.md')).read(),
    test_suite='tests',
)
