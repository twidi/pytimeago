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


import math

halfstr = u' et demi'
nohalf = u''
pluralstr = u's'
noplural = u''

def french(delta, **kw):
    """French language for pytimeago.  There are no keywords supported.

    First, load utilities for testing:

    >>> from test import *

    The function accepts delta in seconds:

    >>> french(0)
    u'\\xe0 l\'instant'
    >>> french(0.4)
    u'\\xe0 l\'instant'
    >>> french(20)
    u'\\xe0 l\'instant'

    If delta falls in range 1..59 minutes, it is said so:

    >>> french(hours(0, 5))
    u'il y a 5 minutes'
    >>> french(hours(0, 59))
    u'il y a 59 minutes'

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
    u'il y a un jour'

    Less than four weeks, we say so:

    >>> french(weeks(1))
    u'il y a une semaine'
    >>> french(days(8))
    u'il y a une semaine'
    >>> french(days(13))
    u'il y a 2 semaines'
    >>> french(weeks(3))
    u'il y a 3 semaines'
    >>> french(days(17))
    u'il y a 2 semaines et demi'

    Less than a year, say it in months:

    >>> french(weeks(4))
    u'il y a un mois'
    >>> french(days(40))
    u'il y a un mois et demi'
    >>> french(days(29))
    u'il y a un mois'
    >>> french(months(2))
    u'il y a 2 mois'
    >>> french(months(11))
    u'il y a 11 mois'
    >>> french(days(70))
    u'il y a 2 mois et demi'

    We go no further than years:

    >>> french(years(2))
    u'il y a 2 ans'
    >>> french(months(18))
    u'il y a un an et demi'
    >>> french(months(12))
    u'il y a un an'

    """

    # Now
    if delta < 30:
        return u'à l\'instant'

    # < 1 hour
    mins = delta/60.
    if mins < 1.5:
        return u'il y a une minute'
    if mins < 60:
        return u'il y a %d minutes' % math.ceil(mins)

    # < 1 day
    if mins < 75:
        return u'il y a une heure'
    hours, mins = divmod(mins, 60)
    if 15 <= mins <= 45:
        half = halfstr
    else:
        half = nohalf
        if mins > 45:
            hours += 1
    if hours < 24:
    	number = ('%d' % hours) if hours > 1 else 'une'
        plural = hours > 1 and pluralstr or noplural
        return u'il y a %s heure%s%s' % (number, plural, half)

    # < 7 days
    if hours < 30:
        return u'il y a un jour'
    days, hours = divmod(hours, 24)
    if 6 <= hours <= 18:
        half = halfstr
    else:
        half = nohalf
        if hours > 18:
            days += 1
    if days < 7:
    	number = ('%d' % days) if days > 1 else 'un'
        plural = days > 1 and pluralstr or noplural
        return u'il y a %s jour%s%s' % (number, plural, half)

    # < 4 weeks
    if days < 9:
        return u'il y a une semaine'
    weeks, wdays = divmod(days, 7)
    if 2 <= wdays <= 4:
        half = halfstr
    else:
        half = nohalf
        if wdays > 4:
            weeks += 1
    if weeks < 4: # So we don't get 4 weeks
    	number = ('%d' % weeks) if weeks > 1 else 'une'
        plural = weeks > 1 and pluralstr or noplural
        return u'il y a %s semaine%s%s' % (number, plural, half)

    # < year
    if days < 40:
        return u'il y a un mois'
    months, days = divmod(days, 30.4)
    if 10 <= days <= 20:
        half = halfstr
    else:
        half = nohalf
        if days > 20:
            months += 1
    if months < 12:
    	number = ('%d' % months) if months > 1 else 'un'
        return u'il y a %s mois%s' % (number, half)

    # Don't go further
    if months < 16:
        return u'il y a un an'
    years, months = divmod(months, 12)
    if 4 <= months <= 8:
        half = halfstr
    else:
        half = nohalf
        if months > 8:
            years += 1
    number = ('%d' % years) if years > 1 else 'un'
    plural = years > 1 and pluralstr or u''
    return u'il y a %s an%s' % (number, plural)


# Doctest
if __name__ == '__main__':
    import doctest
    doctest.testmod()

