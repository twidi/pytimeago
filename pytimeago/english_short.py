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

$Id: english_short.py 12 2006-09-14 09:07:02Z admp $
"""

halfstr = u'\u00BD'

def english_short(delta, **kw):
    """English language for pytimeago.  There are no keywords supported.

    First, load utilities for testing:

    >>> from test import *
    
    The function accepts delta in seconds:

    >>> english_short(0)
    u'now'

    If delta falls in range 0..59 minutes, it is said so:

    >>> english_short(hours(0, 5))
    u'5 mn'
    >>> english_short(hours(0, 59))
    u'59 mn'

    If delta is less than 24 hours, it is reported in hours with half-
    periods:

    >>> english_short(hours(3))
    u'3h'
    >>> english_short(hours(12, 25))
    u'12\\xbdh'

    Next, if delta is less than 7 days, it reported just so.

    >>> english_short(days(6))
    u'6 d'

    And also use half-periods:

    >>> english_short(days(4) + hours(11))
    u'4\\xbd d'

    Special case for 1 day:

    >>> english_short(days(1))
    u'1 d'

    Less than four weeks, we say so:

    >>> english_short(weeks(1))
    u'1 w'
    >>> english_short(days(8))
    u'1 w'
    >>> english_short(days(13))
    u'2 w'
    >>> english_short(weeks(3))
    u'3 w'
    >>> english_short(days(17))
    u'2\\xbd w'

    Less than a year, say it in months:

    >>> english_short(weeks(4))
    u'1 mo'
    >>> english_short(days(40))
    u'1\\xbd mo'
    >>> english_short(days(29))
    u'1 mo'
    >>> english_short(months(2))
    u'2 mo'
    >>> english_short(months(11))
    u'11 mo'
    >>> english_short(days(70))
    u'2\\xbd mo'

    We go no further than years:

    >>> english_short(years(2))
    u'2 y'
    >>> english_short(months(12))
    u'1 y'

    """

    # Now
    if delta == 0:
        return u'now'

    # < 1 hour
    mins = delta/60
    if mins < 60:
        return u'%d mn' % mins

    # < 1 day
    hours, mins = divmod(mins, 60)
    if hours < 24:
        # "half" is for 30 minutes in the middle of an hour
        half = 15 <= mins <= 45 and halfstr or u''
        return u'%d%sh' % (hours, half)

    # < 7 days
    hours += round(mins/60.)
    days, hours = divmod(hours, 24)
    if days == 1:
        return u'1 d'
    if days < 7:
        half = 6 <= hours <= 18 and halfstr or u''
        return u'%d%s d' % (days, half)

    # < 4 weeks
    days += round(hours/24.)
    if days < 9:
        return u'1 w'
    weeks, wdays = divmod(days, 7)
    if 2 <= wdays <= 4:
        half = halfstr
    else:
        half = u''
        if wdays > 4:
            weeks += 1
    if weeks < 4: # So we don't get 4 weeks
        return u'%d%s w' % (weeks, half)

    # < year
    if days < 35:
        return u'1 mo'
    months, days = divmod(days, 30)
    if 10 <= days <= 20:
        half = halfstr
    else:
        half = u''
        if days > 20:
            months += 1
    if months < 12:
        return u'%d%s mo' % (months, half)

    # Don't go further
    years = round(months/12.)
    if years == 1:
        return u'1 y'
    else:
        return u'%d y' % years


# Doctest
if __name__ == '__main__':
    import doctest
    doctest.testmod()

