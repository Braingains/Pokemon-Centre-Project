from flask import Blueprint, Flask, redirect, render_template, request
from models.pokemon import Pokemon
import repositories.pokemon_repository as pokemon_repository
import repositories.nurse_repository as nurse_repository
import repositories.trainer_repository as trainer_repository
import pdb

pokemon_blueprint = Blueprint("pokemon", __name__)

@pokemon_blueprint.route("/pokemons/index")
def pokemon():
    pokemons = pokemon_repository.select_all()
    return render_template("pokemons/index.html", pokemons = pokemons)

@pokemon_blueprint.route("/pokemons/new")
def new_pokemon():
    nurses = nurse_repository.select_all()
    return render_template("/pokemons/new.html", pokemon = pokemon, nurses=nurses)

@pokemon_blueprint.route('/pokemons/new', methods=['POST'])
def create_pokemon():
    name = request.form["name"]
    trainer = request.form["trainer"]
    species = request.form["species"]
    hatched = request.form["hatched"]
    nurse_id = request.form["nurse_id"]
    nurse = nurse_repository.select(nurse_id)
    notes = request.form["notes"]
    new_pokemon = Pokemon(name, trainer, species, hatched, nurse, notes)
    pokemon_repository.save(new_pokemon)
    return redirect('/pokemons/index')

@pokemon_blueprint.route("/pokemons/<id>/edit")
def edit_pokemon(id):
    pokemon = pokemon_repository.select(id)
    nurses = nurse_repository.select_all()
    return render_template('pokemons/edit.html', pokemon=pokemon, nurses = nurses)

@pokemon_blueprint.route("/pokemons/<id>/edit", methods=["POST"])
def update_pokemon(id):
    pokemon = pokemon_repository.select(id)
    name = request.form["name"]
    trainer = request.form['trainer']
    species = request.form['species']
    hatched = request.form['hatched']
    nurse_id = request.form['nurse_id']
    nurse = nurse_repository.select(nurse_id)
    notes = request.form['notes']
    pokemon = Pokemon(name, trainer, species, hatched, nurse, notes)
    pokemon.id = id
    pokemon_repository.update(pokemon)
    return redirect("/pokemons/index")

@pokemon_blueprint.route("/pokemons/<id>/delete", methods=["POST"])
def delete_pokemon(id):
    pokemon_repository.delete(id)
    return redirect("/pokemons/index")