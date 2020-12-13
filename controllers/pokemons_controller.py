from flask import Blueprint, Flask, redirect, render_template, request
from models.pokemon import Pokemon
import repositories.pokemon_repository as pokemon_repository

pokemon_blueprint = Blueprint("pokemon", __name__)

@pokemon_blueprint.route("/pokemons/index")
def pokemon():
    pokemons = pokemon_repository.select_all()
    return render_template("pokemons/index.html", pokemons = pokemons)

@pokemon_blueprint.route("/pokemons/new")
def new_pokemon():
    return render_template("pokemons/new.html")