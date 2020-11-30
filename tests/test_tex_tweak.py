import unittest
from tex_tweak import __version__


class TestHelpers(unittest.TestCase):
    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_version(self):
        assert __version__ == "0.1.0"

    def test_zero_pad(self):
        self.assertEqual(str(3).zfill(5), "00003")
        self.assertEqual(str(15331).zfill(3), "15331")
