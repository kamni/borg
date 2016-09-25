"""
J Leadbetter <jleadbet@gmail.com>
MIT License

An exploration of Python Borg pattern. Except these Borg are Highlanders.
"""

from __future__ import print_function


class ThereCanBeOnlyOne(object):
    """Implementation of the traditional Python Borg pattern"""

    __shared__ = {}

    def __init__(self, name, beheaded=None):
        self.__dict__ = ThereCanBeOnlyOne.__shared__

        self.name = name
        self.beheaded = beheaded

    def has_beheaded(self):
        return '{} has beheaded {}.'.format(self.name, self.beheaded)

    def __str__(self):
        return '{} is an immortal.'.format(self.name)


if __name__ == '__main__':
    highlander1 = ThereCanBeOnlyOne('Victor Kurgan', 'Osta Vasilek')

    print(highlander1)
    print(highlander1.has_beheaded())
    print("But if we create another highlander...")

    highlander2 = ThereCanBeOnlyOne('Connor MacLeod', 'The Kurgan')

    print("We see that there can only be one.")
    print(highlander1)
    print(highlander1.has_beheaded())
