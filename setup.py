

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

config = {
    'description': 'e-mail facility',
    'author': 'Adisakshya Chauhan',
    'url': 'URL to get it at.',
    'download_url': 'Where to download it.',
    'author_email': 'adisakshya chauhan',
    'version': '1.0',
    'install_requires': [],
    'packages': [],
    'scripts': ['bin/pymail.py'],
    'name': 'pymail'
    }

setup(**config)
