from flask import Blueprint, Flask, redirect, render_template, request
from models.nurse import Nurse
import repositories.nurse_repository as nurse_repository

nurse_blueprint = Blueprint("nurse", __name__)

@nurse_blueprint.route("/nurses/index")
def nurse():
    nurses = nurse_repository.select_all()
    return render_template("nurses/index.html", nurses = nurses)