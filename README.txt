= Human-oriented representation of time deltas, a Python library =

Original description from http://adomas.org/pytimeago/ :

First, I shall define what time delta is. Since Δ generally means “difference”, we take time delta to stand for difference between two events in time. Quite common, however, is to have the current time for the second event. In pytimeago we deal with time deltas from such a perspective.

Quite possibly, you can make use of this library if your application displays some dynamically generated items to the user, and you are looking for a good way to present information on how long ago specific item was created/processed/whatever.

Below is small code snippet demonstrating how simple it is to embed pytimeago:

  from pytimeago.english import english
  from time import time

  message = queue.getNextMessage()
  delta = time() - message.arrived_time
  print "Message arrived %s" % english(delta)

Prints, e.g.

  Message arrived 15mins ago

As you see, pytimeago is package, and has individual modules for every language supported. As of 2006-08-13 the only supported language is English. However, you can take a look at rather trivial implementation of English engine, write one for your language, and send it to to me (email at the bottom of page).

Every language should come with a set of doctests (I prefer them to casual unit tests), just like the English version does. Don't be too verbose, but check essential cases.

pytimeago is licenced under LGPL. I'd be happy to hear if you use this in your software. Note that language module(s) can also be taken standalone to other projects, if desired.
