

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

config = {
    'description': 'e-mail facility',
    'author': 'Adisakshya Chauhan',
    'url': 'https://github.com/adisakshya/pymail',
    'download_url': 'https://github.com/adisakshya/pymail',
    'author_email': 'adisakshya chauhan',
    'version': '1.0',
    'install_requires': [],
    'packages': ['pymail'],
    'scripts': ['bin/pymail.py'],
    'name': 'pymail'
    }

setup(**config)
