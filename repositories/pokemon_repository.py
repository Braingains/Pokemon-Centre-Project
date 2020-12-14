from db.run_sql import run_sql

from models.pokemon import Pokemon
from models.trainer import Trainer
from models.nurse import Nurse

def save(pokemon):
    sql = "INSERT INTO pokemons (name, trainer, nurse, species, hatched) VALUES (%s, %s, %s, %s, %s) RETURNING id"
    values = [pokemon.name, pokemon.trainer, pokemon.nurse, pokemon.species, pokemon.hatched]
    results = run_sql( sql, values )
    id = results[0]['id']
    return pokemon

def select_all():
    pokemons = []

    sql = "SELECT * FROM pokemons"
    results = run_sql(sql)
    for row in results:
        pokemon = Pokemon(row['name'], row['trainer'], row['species'], row['hatched'], row['id'])
        pokemons.append(pokemon)
    return pokemons

def select(id):
    pokemon = None
    sql = "SELECT * FROM pokemons WHERE id = %s"
    values = [id]
    result = run_sql(sql, values)[0]

    if result is not None:
        pokemon = Pokemon(result['name'], result['trainer'], result['species'], result['hatched'], result['id'])
    return pokemon 

def update(pokemon):
    sql = "UPDATE pokemons SET (name, trainer, nurse_id, species, hatched) = (%s, %s, %s, %s, %s) WHERE id = %s"
    values = [pokemon.name, pokemon.trainer, pokemon.nurse.id, pokemon.species, pokemon.hatched]
    run_sql(sql, values)

def delete(id):
    sql = "DELETE FROM pokemons WHERE id = %s"
    values = [id]
    run_sql(sql, values)

def delete_all():
    sql = "DELETE FROM pokemons"
    run_sql(sql)


# add pokemon.trainer_id connections later