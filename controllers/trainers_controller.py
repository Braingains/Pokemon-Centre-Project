from flask import Blueprint, Flask, redirect, render_template, request
from models.trainer import Trainer
import repositories.trainer_repository as trainer_repository

trainer_blueprint = Blueprint("trainer", __name__)

@trainer_blueprint.route("/trainers/index")
def trainer():
    trainers = trainer_repository.select_all()
    return render_template("trainers/index.html", trainers = trainers)