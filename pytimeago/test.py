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

"""Utilities for unit (or doc-) tests.
"""

def hours(h, m=0):
    return (h*60+m)*60

def days(d):
    return d*hours(24)

def weeks(w):
    return w*7*days(1)

def months(m):
    return m*30*days(1)

def years(y):
    return y*365*days(1)

