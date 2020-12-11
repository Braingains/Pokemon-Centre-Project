from flask import Blueprint, Flask, redirect, render_template, request
from models.nurse import Nurse


nurse_blueprint = Blueprint("nurse", __name__)