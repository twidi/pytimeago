#!/usr/bin/env python

from distutils.core import setup

VERSION = '2.0'
DESCRIPTION = "Human-oriented representation of time deltas, a Python library"
LONG_DESCRIPTION = """
Convert time deltas into phrases like "5 minutes ago",
"3 hours ago", "2 days ago" etc.

This package has a number of modules in it, each for separate
language.  It is standard that module pytimeago.X has function
X, which accepts at least on argument -- number of seconds
between two events.  It may also accept extra keywords, which
should be documented in the docstring of the function.
Returned is always unicode string.

Usage pattern:

    from pytimeago.english import english
    from time import time, sleep

    a = time()
    # ...do something here...
    delta = int(time() - a)  # could use sometimedetal.total_seconds()
    print "job started %s" % english(delta)

Prints, e.g.

    job started 15 minutes ago

Available languages are:

    from pytimeago.english import english
    from pytimeago.english import english_short
    from pytimeago.french import french

Licenced under GNU Lesser General Public License,
you can get a copy at: http://www.gnu.org/licenses/lgpl.html

Written by Adomas Paltanavicius (adomas.paltanavicius@gmail.com).
Packaged, french added, and computation enhanced by Stephane "Twidi" Angel (s.angel@twidi.com)
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

