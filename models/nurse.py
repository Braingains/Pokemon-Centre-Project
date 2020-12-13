class Nurse:
    def __init__(self, name, id = None):
        self.name = name
        self.id = id
        self.pokemon = None

    def assign_pokemon(self, pokemon):
        self.pokemon = pokemon