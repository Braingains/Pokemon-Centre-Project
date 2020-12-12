from db.run_sql import run_sql

from models.pokemon import Pokemon
from models.trainer import Trainer

def save(pokemon):
    sql = "INSERT INTO pokemons (name, trainer_id, species, hatched) VALUES (%s, %s, %s, %s) RETURNING id"
    values = [pokemon.name, pokemon.trainer.id, pokemon.species, pokemon.hatched]
    results = run_sql( sql, values )
    pokemon.id = results[0]['id']
    return pokemon