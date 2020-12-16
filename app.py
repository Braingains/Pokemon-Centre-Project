from flask import Flask, render_template

from controllers.pokemons_controller import pokemon_blueprint
# from controllers.trainers_controller import trainer_blueprint
from controllers.nurses_controller import nurse_blueprint

app = Flask(__name__)

app.register_blueprint(pokemon_blueprint)
# app.register_blueprint(trainer_blueprint)
app.register_blueprint(nurse_blueprint)

@app.route("/")
def main():
    return render_template('index.html')

if __name__ == '__main__':
    app.run() 