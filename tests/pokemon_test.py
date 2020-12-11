import unittest

from models.pokemon import Pokemon

class TestPokemon(unittest.TestCase):

    def setUp(self):
        self.pokemon_1 = Pokemon('Sparky', 'Ritchie', 'Pikachu', '15/6/2017')

    def test_pokemon_has_name(self):
        self.assertEqual('Sparky', self.pokemon_1.name)

    def test_pokemon_has_trainer(self):
        self.assertEqual('Ritchie', self.pokemon_1.trainer)

    def test_pokemon_has_species(self):
        self.assertEqual('Pikachu', self.pokemon_1.species)

    def test_pokemon_has_hatched(self):
        self.assertEqual('15/6/2017', self.pokemon_1.hatched)