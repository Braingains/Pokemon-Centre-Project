from flask import Blueprint, Flask, redirect, render_template, request
from models.pokemon import Pokemon
import repositories.pokemon_repository as pokemon_repository

pokemon_blueprint = Blueprint("pokemon", __name__)