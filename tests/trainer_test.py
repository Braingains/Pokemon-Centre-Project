import unittest

from models.trainer import Trainer

class TestTrainer(unittest.TestCase):

    def setUp(self):
        self.trainer_1 = Trainer('Ash', '1 Pallet Town', 12345)

    def test_trainer_has_name(self):
        self.assertEqual('Ash', self.trainer_1.name)

    def test_trainer_has_address(self):
        self.assertEqual('1 Pallet Town', self.trainer_1.address)

    def test_trainer_has_pokenav_number(self):
        self.assertEqual(12345, self.trainer_1.pokenav)