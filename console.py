from models.pokemon import Pokemon
from models.trainer import Trainer
from models.nurse import Nurse

import repositories.pokemon_repository as pokemon_repository
import repositories.trainer_repository as trainer_repository
import repositories.nurse_repository as nurse_repository

pokemon_repository.delete_all()
nurse_repository.delete_all()
trainer_repository.delete_all()

trainer_1 = Trainer('Ash', '2 Pallet Town', 32356)
trainer_2 = Trainer('Misty', 'Cerulean Gym', 78232)
nurse_1 = Nurse('Joy')
nurse_2 = Nurse('Joye')
pokemon_1 = Pokemon('Sparky', trainer_1, 'Pikachu', '15/6/2017')
pokemon_2 = Pokemon('Frankie', trainer_2, 'Psyduck', '12/1/2016')
pokemon_3 = Pokemon('Sally', trainer_2, 'Seel', '15/8/2015')

#assign nurse to pokemon before running console.py
pokemon_1.assign_nurse(nurse_1)
pokemon_2.assign_nurse(nurse_2)
pokemon_3.assign_nurse(nurse_2)

trainer_repository.save(trainer_1)
trainer_repository.save(trainer_2)

nurse_repository.save(nurse_1)
nurse_repository.save(nurse_2)

pokemon_repository.save(pokemon_1)
pokemon_repository.save(pokemon_2)
pokemon_repository.save(pokemon_3)








