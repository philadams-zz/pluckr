# -*- coding: utf-8 -*-

from .context import pluckr

import unittest


class AdvancedTestSuite(unittest.TestCase):
    """Advanced test cases."""

    def test_thoughts(self):
        pluckr.hello_world()


if __name__ == '__main__':
    unittest.main()
