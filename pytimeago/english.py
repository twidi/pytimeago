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

"""English language for pytimeago.

$Id: english.py 12 2006-09-14 09:07:02Z admp $
"""

import math

halfstr = u'\u00BD'
nohalf = u''

def english(delta, **kw):
    """English language for pytimeago.  There are no keywords supported.

    First, load utilities for testing:

    >>> from test import *

    The function accepts delta in seconds:

    >>> english(0)
    u'just now'
    >>> english(0.4)
    u'just now'
    >>> english(20)
    u'just now'

    If delta falls in range 1..59 minutes, it is said so:

    >>> english(hours(0, 5))
    u'5 minutes ago'
    >>> english(hours(0, 59))
    u'59 minutes ago'

    If delta is less than 24 hours, it is reported in hours with half-
    periods:

    >>> english(hours(3))
    u'3 hours ago'
    >>> english(hours(12, 25))
    u'12\\xbd hours ago'

    Next, if delta is less than 7 days, it reported just so.

    >>> english(days(6))
    u'6 days ago'

    And also use half-periods:

    >>> english(days(4) + hours(11))
    u'4\\xbd days ago'

    Special case for 1 day:

    >>> english(days(1))
    u'a day ago'

    Less than four weeks, we say so:

    >>> english(weeks(1))
    u'a week ago'
    >>> english(days(8))
    u'a week ago'
    >>> english(days(13))
    u'2 weeks ago'
    >>> english(weeks(3))
    u'3 weeks ago'
    >>> english(days(17))
    u'2\\xbd weeks ago'

    Less than a year, say it in months:

    >>> english(weeks(4))
    u'a month ago'
    >>> english(days(40))
    u'1\\xbd months ago'
    >>> english(days(29))
    u'a month ago'
    >>> english(months(2))
    u'2 months ago'
    >>> english(months(11))
    u'11 months ago'
    >>> english(days(70))
    u'2\\xbd months ago'

    We go no further than years:

    >>> english(years(2))
    u'2 years ago'
    >>> english(months(18))
    u'1\\xbd years ago'
    >>> english(months(12))
    u'a year ago'

    """

    # Now
    if delta < 0.5:
        return u'just now'

    # < 1 hour
    mins = delta/60.
    if mins < 1.5:
        return u'a minute ago'
    if mins < 60:
        return u'%d minutes ago' % math.ceil(mins)

    # < 1 day
    if mins < 75:
        return u'an hour ago'
    hours, mins = divmod(mins, 60)
    if 15 <= mins <= 45:
        half = halfstr
    else:
        half = nohalf
        if mins > 45:
            hours += 1
    if hours < 24:
        return u'%d%s hours ago' % (hours, half)

    # < 7 days
    if hours < 30:
        return u'a day ago'
    days, hours = divmod(hours, 24)
    if 6 <= hours <= 18:
        half = halfstr
    else:
        half = nohalf
        if hours > 18:
            days += 1
    if days < 7:
        return u'%d%s days ago' % (days, half)

    # < 4 weeks
    if days < 9:
        return u'a week ago'
    weeks, wdays = divmod(days, 7)
    if 2 <= wdays <= 4:
        half = halfstr
    else:
        half = nohalf
        if wdays > 4:
            weeks += 1
    if weeks < 4: # So we don't get 4 weeks
        return u'%d%s weeks ago' % (weeks, half)

    # < year
    if days < 40:
        return u'a month ago'
    months, days = divmod(days, 30.4)
    if 10 <= days <= 20:
        half = halfstr
    else:
        half = nohalf
        if days > 20:
            months += 1
    if months < 12:
        return u'%d%s months ago' % (months, half)

    # Don't go further
    if months < 16:
        return u'a year ago'
    years, months = divmod(months, 12)
    if 4 <= months <= 8:
        half = halfstr
    else:
        half = nohalf
        if months > 8:
            years += 1
    return u'%d%s years ago' % (years, half)


# Doctest
if __name__ == '__main__':
    import doctest
    doctest.testmod()

