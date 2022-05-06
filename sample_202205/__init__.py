__version__ = '0.1.0'

from operator import add
from functools import reduce

def sum(*args):
    return reduce(add, args)

