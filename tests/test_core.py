import unittest

class LgtmTest(unittest.TestCase):
    def test_lgtm(self):
        from lgtm.core import lgtm
        sefl.assertIsNone(lgtm("./python.jpeg","LGTM"))
        