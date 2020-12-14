from flask import Blueprint, Flask, redirect, render_template, request
from models.pokemon import Pokemon
import repositories.pokemon_repository as pokemon_repository
import repositories.nurse_repository as nurse_repository
import repositories.trainer_repository as trainer_repository

pokemon_blueprint = Blueprint("pokemon", __name__)

@pokemon_blueprint.route("/pokemons/index")
def pokemon():
    pokemons = pokemon_repository.select_all()
    return render_template("pokemons/index.html", pokemons = pokemons)

@pokemon_blueprint.route("/pokemons/new",  methods=['POST'])
def create_pokemon():
    name = request.form["name"]
    trainer = request.form["trainer"]
    species = request.form["species"]
    hatched = request.form["hatched"]
    new_pokemon = Pokemon(name, trainer, species, hatched)
    pokemon_repository.save(new_pokemon)
    return redirect("/pokemons/index")

@pokemon_blueprint.route("/pokemon/<id>/edit")
def edit_pokemon(id):
    pokemons = pokemon_repository.select(id)
    return render_template('pokemons/edit.html', pokemons=pokemons)

# @nurse_blueprint.route("/nurses/<id>/edit", methods=["POST"])
# def update_nurse(id):
#     name = request.form["name"]
#     nurse = Nurse(name, id)
#     nurse_repository.update(nurse)
#     return redirect("/nurses/index")

@pokemon_blueprint.route("/pokemon/<id>/delete", methods=["POST"])
def delete_pokemon(id):
    pokemon_repository.delete(id)
    return redirect("/pokemons/index")