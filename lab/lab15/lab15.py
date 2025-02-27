from time import struct_time
from types import new_class


def convert_link(link):
    """Takes a linked list and returns a Python list with the same elements.

    >>> link = Link(1, Link(2, Link(3, Link(4))))
    >>> convert_link(link)
    [1, 2, 3, 4]
    >>> convert_link(Link.empty)
    []
    """
    new_list = []
    if link is not Link.empty:
        while link is not Link.empty:
            new_list.append(link.first)
            link = link.rest
    return new_list


def store_digits(n):
    """Stores the digits of a positive number n in a linked list.

    >>> s = store_digits(1)
    >>> s
    Link(1)
    >>> store_digits(2345)
    Link(2, Link(3, Link(4, Link(5))))
    >>> store_digits(876)
    Link(8, Link(7, Link(6)))
    """

    def get_list(i):
        if i >= 10:
            num = i
            count = 0
            while num >= 10:
                count += 1
                num //= 10
            diff = i - num * (10 ** count)
            return Link(num, get_list(diff))
        return Link(i)

    return get_list(n)


def every_other(link):
    """Mutates a linked list so that all the odd-indexed elements are removed
    (using 0-based indexing).

    >>> s = Link(1, Link(2, Link(3, Link(4))))
    >>> every_other(s)
    >>> s
    Link(1, Link(3))
    >>> odd_length = Link(5, Link(3, Link(1)))
    >>> every_other(odd_length)
    >>> odd_length
    Link(5, Link(1))
    >>> singleton = Link(4)
    >>> every_other(singleton)
    >>> singleton
    Link(4)
    """

    if link is Link.empty or link.rest is Link.empty:
        return
    link.rest = link.rest.rest
    every_other(link.rest)


def deep_map_mut(fn, link):
    """Mutates a deep link by replacing each item found with the
    result of calling fn on the item.  Does NOT create new Links (so
    no use of Link's constructor)

    Does not return the modified Link object.

    >>> link1 = Link(3, Link(Link(4), Link(5, Link(6))))
    >>> deep_map_mut(lambda x: x * x, link1)
    >>> link1
    Link(9, Link(Link(16), Link(25, Link(36))))
    """

    def iterate(linked):
        if linked is Link.empty:
            return

        if type(linked.first) is int:
            linked.first = fn(linked.first)
            iterate(linked.rest)

        else:
            implicit_link = linked
            while type(implicit_link.first) is not int:
                implicit_link = implicit_link.first
            implicit_link.first = fn(implicit_link.first)
            iterate(implicit_link.rest)
            iterate(linked.rest)

    iterate(link)


class Link:
    empty = ()

    def __init__(self, first, rest=empty):
        assert rest is Link.empty or isinstance(
            rest, Link), "Link does not follow proper structure"
        self.first = first
        self.rest = rest

    def __repr__(self):
        if self.rest is not Link.empty:
            rest_repr = ', ' + repr(self.rest)
        else:
            rest_repr = ''
        return 'Link(' + repr(self.first) + rest_repr + ')'

    def __str__(self):
        string = '<'
        while self.rest is not Link.empty:
            string += str(self.first) + ' '
            self = self.rest
        return string + str(self.first) + '>'


if __name__ == '__main__':
    s = Link(1, Link(2, Link(3, Link(4))))
