from __future__ import division, print_function

import os
import hashlib
from unittest import TestCase, main
import doctest

from tomcrypt.hash import *
from tomcrypt import hash

from . import get_doctests


def load_tests(loader, tests, ignore):
    tests.addTests(get_doctests(hash))
    return tests


class TestHashed(TestCase):

    def test_against_hashlib(self):
        for name in hash.names:
            print(repr(name))
            if name == 'chc':
                continue
            try:
                y = hashlib.new(name)
            except ValueError:
                continue
            yield self.check_hashlib, name


    def check_hashlib(self):        
        x = Hash(name)
        y = hashlib.new(name)
        for i in xrange(100):
            s = os.urandom(i)
            x.update(s)
            y.update(s)
            assert x.digest() == y.digest()
        x2 = x.copy()
        x2.update('something else')
        assert x.digest() == y.digest()
        assert x2.digest() != y.digest()


    def test_api(self):
        assert 'sha256' in hash.names
        msg = b'hello, world'
        assert hash.sha256(msg).hexdigest() == '09ca7e4eaa6e8ae9c7d261167129184883644d07dfba7cbfbc4c8a2e08360d5b'


if __name__ == '__main__':
    main()
