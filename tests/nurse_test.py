import unittest

from models.nurse import Nurse

class TestNurse(unittest.TestCase):

    def setUp(self):
        self.nurse_1 = Nurse('Joy')

    def test_nurse_has_name(self):
        self.assertEqual('Joy', self.nurse_1.name)