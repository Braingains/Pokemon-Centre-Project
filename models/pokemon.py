class Pokemon:
    def __init__(self, name, trainer, species, hatched, nurse, id = None):
        self.name = name
        self.trainer = trainer
        self.species = species
        self.hatched = hatched
        self.nurse = nurse
        self.id = id
        #add elemental type

    def assign_nurse(self, nurse):
        self.nurse = nurse