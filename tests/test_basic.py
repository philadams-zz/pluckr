# -*- coding: utf-8 -*-

from .context import pluckr

import unittest


class BasicTestSuite(unittest.TestCase):
    """Basic test cases."""

    def test_reads_csv(self):
        assert False


if __name__ == '__main__':
    unittest.main()
