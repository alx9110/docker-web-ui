""" Setup """
from os.path import join, dirname
from setuptools import setup, find_packages


requirements = [
    'flask>=0.10',
    'requests',
    'docker',
    'redis',
    'rq',
    'python-telegram-bot',
    ]

setup(
    name='docker-web-ui',
    version='0.0.2',
    author='Alexander Telkov & Paul Farunda',
    author_email='alx9110@yandex.ru',
    install_requires=requirements,
    packages=find_packages(exclude=['tests', 'tests.*']),
    include_package_data=True,
    long_description=open(join(dirname(__file__), 'README.md')).read(),
    test_suite='tests',
)
