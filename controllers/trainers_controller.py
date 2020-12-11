from flask import Blueprint, Flask, redirect, render_template, request
from models.trainer import Trainer


trainer_blueprint = Blueprint("trainer", __name__)