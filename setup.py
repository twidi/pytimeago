#!/usr/bin/env python

from distutils.core import setup

VERSION = '1.0'
DESCRIPTION = "Human-oriented representation of time deltas, a Python library"
LONG_DESCRIPTION = """
First, I shall define what time delta is. Since delta generally means "difference", we take time delta to stand for difference between two events in time. Quite common, however, is to have the current time for the second event. In pytimeago we deal with time deltas from such a perspective.

Quite possibly, you can make use of this library if your application displays some dynamically generated items to the user, and you are looking for a good way to present information on how long ago specific item was created/processed/whatever.
"""

CLASSIFIERS = filter(None, map(str.strip,
"""                 
Intended Audience :: Developers
License :: OSI Approved :: MIT License
Programming Language :: Python
Topic :: Database :: Front-Ends
Topic :: Software Development :: Libraries :: Python Modules
""".splitlines()))


setup(
    name="pytimeago",
    version=VERSION,
    description=DESCRIPTION,
    long_description=LONG_DESCRIPTION,
    classifiers=CLASSIFIERS,
    author="Adomas Paltanavicius",
    author_email="adomas@adomas.com",
    url="http://adomas.org/pytimeago/",
    license="LGPL",
    packages=['pytimeago'],
    platforms=['any'],
)

