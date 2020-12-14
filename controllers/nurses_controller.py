from flask import Blueprint, Flask, redirect, render_template, request
from models.nurse import Nurse
from models.pokemon import Pokemon

import pdb
import repositories.nurse_repository as nurse_repository
import repositories.pokemon_repository as pokemon_repository

nurse_blueprint = Blueprint("nurse", __name__)

@nurse_blueprint.route("/nurses/index")
def nurse():
    nurses = nurse_repository.select_all()
    return render_template("nurses/index.html", nurses = nurses)

@nurse_blueprint.route("/nurses/index", methods=["POST"])
def create_nurse():
    name = request.form["name"]
    new_nurse = Nurse(name)
    nurse_repository.save(new_nurse)
    return redirect("/nurses/index")

@nurse_blueprint.route("/nurses/new", methods=['GET'])
def new_nurse():
    nurses = nurse_repository.select_all()
    pokemons = pokemon_repository.select_all()
    return render_template("nurses/new.html", nurses = nurses, pokemons = pokemons)

@nurse_blueprint.route("/nurses/new",  methods=['POST'])
def assign_nurse():
    nurse_id = request.form['nurse_id']
    pokemon_id = request.form['pokemon_id']
    nurse = nurse_repository.select(nurse_id)
    pokemon = pokemon_repository.select(pokemon_id)
    nurse.assign_pokemon(pokemon)
    # pdb.set_trace()
    pokemon_repository.update(pokemon)
    return redirect('/nurses/index')

@nurse_blueprint.route("/nurses/<id>/edit")
def edit_nurse(id):
    nurse = nurse_repository.select(id)
    return render_template('nurses/edit.html', nurse=nurse)

@nurse_blueprint.route("/nurses/<id>/edit", methods=["POST"])
def update_nurse(id):
    name = request.form["name"]
    nurse = Nurse(name, id)
    nurse_repository.update(nurse)
    return redirect("/nurses/index")

@nurse_blueprint.route("/nurses/<id>/delete", methods=["POST"])
def delete_nurse(id):
    nurse_repository.delete(id)
    return redirect("/nurses/index")