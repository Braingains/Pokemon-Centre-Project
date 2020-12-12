class Pokemon:
    def __init__(self, name, trainer, species, hatched, id = None):
        self.name = name
        self.trainer = trainer
        self.species = species
        self.hatched = hatched
        self.id = id
        self.nurse = None

    def assign_nurse(self, nurse):
        self.nurse = nurse