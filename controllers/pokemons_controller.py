from flask import Blueprint, Flask, redirect, render_template, request
from models.pokemon import Pokemon


pokemon_blueprint = Blueprint("pokemon", __name__)