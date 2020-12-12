from models.pokemon import Pokemon
from models.trainer import Trainer
from models.nurse import Nurse

import repositories.pokemon_repository as pokemon_repository
import repositories.trainer_repository as trainer_repository
import repositories.nurse_repository as nurse_repository


trainer_1 = Trainer('Ritchie', '12 Pallet Town', 32356)
nurse_1 = Nurse('Joy')
pokemon_1 = Pokemon('Sparky', trainer_1, 'Pikachu', '15/6/2017')

#assign nurse to pokemon before running console.py
pokemon_1.assign_nurse(nurse_1)

trainer_repository.save(trainer_1)

nurse_repository.save(nurse_1)

pokemon_repository.save(pokemon_1)

