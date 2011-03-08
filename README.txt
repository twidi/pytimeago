Convert time deltas into phrases like "5min ago",
"3h ago", "2 days ago" etc.

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
