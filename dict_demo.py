"""
collections -- Container datatypes
==================================
Source code: Lib/collections/__init__.py

This module implements specialized container datatypes providing alternatives
to Python's general purpose built-in containers: dict, list, set and tuple.

namedtuple()    factory function for creating tuple subclasses with named fields
deque           list-like container with fast appends and pops on either end
ChainMap        dict-like class for creating a single view of multiple mappings
OrderedDict     dict subclass that remembers the order entries were added
defaultdict     dict subclass that calls a factory fnction to supply missing values (instead of throw an exception)
UserDict        wrapper around dictionary objects for easier dict subclassing
UserList        wrapper around list objects for easier list subclassing
UserString      wrapper around string objects for easier string subclassing

OrderDict Methods:
    popitem(last=True): returns and remove a (key, value) pair. 
        The pairs are returned in LIFO order if last is True (default)
        or FIFO order if last is False.

    move_to_end(key, last=True): move an existing key to either end
        of an ordered dictionary. The item is moved to the right if last is True (default)
        or to the beginning if last is False. Raises KeyError if the key does not exist.

Examples
--------

import collections

print('Regular dictionary')
d = {}
d['a'] = 'A'
d['b'] = 'B'
d['c'] = 'C'
d['d'] = 'D'
d['e'] = 'E'

for k, v in d.items():
    print('{}: {}'.format(k,v))

print('\nOrderedDict:')
d = collections.OrderedDict()
d['a'] = 'A'
d['b'] = 'B'
d['c'] = 'C'
d['d'] = 'D'
d['e'] = 'E'

for k, v in d.items():
    print('{}: {}'.format(k,v))

"""
import hashlib



print("Python hash():")
s = 'Python is awesoma?'
print(abs(hash(s)) % (10 ** 4))

print("Python hashlib:")
# **: Exponentiation
# 10 ** 2 = 100
size = 5
print(int(hashlib.sha1(s.encode('utf-8')).hexdigest(), 16) % size)
