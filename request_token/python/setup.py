import os
from setuptools import setup, find_packages

version = 1
build = 0
README = os.path.join(os.path.dirname(__file__), 'README.md')
long_description = open(README).read()
version = "%s.%s" % (version, build)

setup(name='pygenjwt',
      version=version,
      description=("Telesign JWT Generator"),
      long_description=long_description,
      classifiers=[
          "Programming Language :: Python",
          ("Topic :: Telesign :: Libraries :: Shared"),
      ],
      keywords = 'telesign',
      author = 'TeleSign',
      install_requires=['bottle',
                        'pyjwt',
                        'PyLRU'],
      packages=find_packages(),
     )
