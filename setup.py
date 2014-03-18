#!/usr/bin/env python

from distutils.core import setup

VERSION = '1.0.2'
DESCRIPTION = "Human-oriented representation of time deltas, a Python library"
LONG_DESCRIPTION = """
Convert time deltas into phrases like "5min ago",
"3h ago", "2 days ago" etc.

Base work from Adomas Paltanavicius, but with two added versions: french and "short english"

This package has a number of modules in it, each for separate
language.  It is standard that module pytimeago.X has function
X, which accepts at least on argument -- number of seconds
between two events.  It may also accept extra keywords, which
should be documented in the docstring of the function.
Returned is always unicode string.

Usage pattern:

    from pytimeago.english import english # or other...
    from time import time, sleep

    a = time()
    # ...do something here...
    delta = int(time() - a)
    print "job started %s" % english(delta)

Prints, e.g.

    job started 15mins ago

Licenced under GNU Lesser General Public License,
you can get a copy at: http://www.gnu.org/licenses/lgpl.html

Written by Adomas Paltanavicius (adomas.paltanavicius@gmail.com).
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
    author_email="adomas.paltanavicius@gmail.com",
    url="https://github.com/twidi/pytimeago",
    license="LGPL",
    packages=['pytimeago'],
    platforms=['any'],
)

