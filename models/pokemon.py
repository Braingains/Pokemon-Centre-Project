class Pokemon:
    def __init__(self, name, trainer, species, hatched, nurse, notes, id = None):
        self.name = name
        self.trainer = trainer
        self.species = species
        self.hatched = hatched
        self.nurse = nurse
        self.notes = notes
        self.id = id
        #add elemental type

    def assign_nurse(self, nurse):
        self.nurse = nurse


#add notes to Pokemon with its injury, it can be edited by nurses to track treatment