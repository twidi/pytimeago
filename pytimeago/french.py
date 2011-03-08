# -*- coding: utf-8 -*-
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

"""French language for pytimeago.

$Id$
"""

halfstr = u' et demi'
pluralstr = u's'

def french(delta, **kw):
    """French language for pytimeago.  There are no keywords supported.

    First, load utilities for testing:

    >>> from test import *

    The function accepts delta in seconds:

    >>> french(0)
    u'\\xe0 l\'instant'

    >>> french(20)
    u'\\xe0 l\'instant'

    If delta falls in range 1..58 minutes, it is said so:

    >>> french(hours(0, 1))
    u'il y a 1 minute'
    >>> french(hours(0, 5))
    u'il y a 5 minutes'
    >>> french(hours(0, 58))
    u'il y a 58 minutes'
    >>> french(hours(0, 59))
    u'il y a 1 heure'

    If delta is less than 24 hours, it is reported in hours with half-
    periods:

    >>> french(hours(3))
    u'il y a 3 heures'
    >>> french(hours(12, 25))
    u'il y a 12 heures et demi'

    Next, if delta is less than 7 days, it reported just so.

    >>> french(days(6))
    u'il y a 6 jours'

    And also use half-periods:

    >>> french(days(4) + hours(11))
    u'il y a 4 jours et demi'

    Special case for 1 day:

    >>> french(days(1))
    u'hier'

    Less than four weeks, we say so:

    >>> french(weeks(1))
    u'il y a 1 semaine'
    >>> french(days(8))
    u'il y a 1 semaine'
    >>> french(days(13))
    u'il y a 2 semaines'
    >>> french(weeks(3))
    u'il y a 3 semaines'
    >>> french(days(17))
    u'il y a 2 semaines et demi'

    Less than a year, say it in months:

    >>> french(weeks(4))
    u'il y a 1 mois'
    >>> french(days(40))
    u'il y a 1 mois et demi'
    >>> french(days(29))
    u'il y a 1 mois'
    >>> french(months(2))
    u'il y a 2 mois'
    >>> french(months(11))
    u'il y a 11 mois'
    >>> french(days(70))
    u'il y a 2 mois et demi'

    We go no further than years:

    >>> french(years(2))
    u'il y a 2 ans'
    >>> french(months(12))
    u'il y a 1 an'

    """

    # Now
    if delta < 30:
        return u'à l\'instant'

    # < 1 hour
    mins = delta/60
    if mins < 1: mins=1
    if mins < 59:
        plural = mins > 1 and pluralstr or u''
        return u'il y a %d minute%s' % (mins, plural)

    # < 1 day
    hours, mins = divmod(mins, 60)
    if hours < 1: hours = 1
    if hours < 23:
        # "half" is for 30 minutes in the middle of an hour
        if 15 <= mins <= 45:
            half = halfstr
        else:
            half = u''
            if mins > 45:
                hours += 1
        plural = hours > 1 and pluralstr or u''
        return u'il y a %d heure%s%s' % (hours, plural, half)

    # < 7 days
    hours += round(mins/60.)
    days, hours = divmod(hours, 24)
    if days == 1:
        return u'hier'
    if days < 7:
        half = 6 <= hours <= 18 and halfstr or u''
        if 6 <= hours <= 18:
            half = halfstr
        else:
            half = u''
            if hours > 18:
                days += 1
        plural = days > 1 and pluralstr or u''
        return u'il y a %d jour%s%s' % (days, plural, half)

    # < 4 weeks
    days += round(hours/24.)
    weeks, wdays = divmod(days, 7)
    if 2 <= wdays <= 4:
        half = halfstr
    else:
        half = u''
        if wdays > 4:
            weeks += 1
    if weeks < 4: # So we don't get 4 weeks
        plural = weeks > 1 and pluralstr or u''
        return u'il y a %d semaine%s%s' % (weeks, plural, half)

    # < year
    months, days = divmod(days, 30)
    if 10 <= days <= 20:
        half = halfstr
    else:
        half = u''
        if days > 20:
            months += 1
    if months < 12:
        return u'il y a %d mois%s' % (months, half)

    # Don't go further
    years = round(months/12.)
    plural = years > 1 and pluralstr or u''
    return u'il y a %d an%s' % (years, plural)


# Doctest
if __name__ == '__main__':
    import doctest
    doctest.testmod()

