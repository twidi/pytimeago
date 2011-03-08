# pytimeago -- library for rendering time deltas
# Copyright (C) 2006 Adomas Paltanavicius
# 
# This library is free software; you can redistribute it and/or
# modify it under the terms of the GNU Lesser General Public
# License as published by the Free Software Foundation; either
# version 2.1 of the License, or (at your option) any later version.
# 
# This library is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU
# Lesser General Public License for more details.
# 
# You should have received a copy of the GNU Lesser General Public
# License along with this library; if not, write to the Free Software
# Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston, MA  02110-1301  USA

"""Convert time deltas into phrases like "5min ago",
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

"""

import pytimeago.english

