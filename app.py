from flask import Flask, render_template

from controllers.pokemons_controller import pokemons_blueprint
from controllers.trainers_controller import trainers_blueprint
from controllers.nurses_controller import nurses_blueprint

app = Flask(__name__)

app.register_blueprint(pokemons_blueprint)
app.register_blueprint(trainers_blueprint)
app.register_blueprint(nurses_blueprint)

@app.route("/")
def main():
    return render_template('index.html')

if __name__ == '__main__':
    app.run()