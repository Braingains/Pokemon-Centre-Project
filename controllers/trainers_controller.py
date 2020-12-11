from flask import Blueprint, Flask, redirect, render_template, request
from models.trainer import Trainer
import repositories.trainer_repository as trainer_repository

trainer_blueprint = Blueprint("trainer", __name__)