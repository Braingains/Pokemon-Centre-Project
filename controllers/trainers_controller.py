# from flask import Blueprint, Flask, redirect, render_template, request
# from models.trainer import Trainer
# import repositories.trainer_repository as trainer_repository

# trainer_blueprint = Blueprint("trainer", __name__)

# @trainer_blueprint.route("/trainers/index")
# def trainer():
#     trainers = trainer_repository.select_all()
#     return render_template("trainers/index.html", trainers = trainers)

# @trainer_blueprint.route("/trainers/new")
# def new_trainer():
#     return render_template("trainers/new.html")

# @trainer_blueprint.route("/trainers/<id>/delete", methods=["POST"])
# def delete_trainer(id):
#     trainer_repository.delete(id)
#     return redirect("/trainers/index")