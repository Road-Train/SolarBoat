import sys, os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../../')))

from flask import Flask, render_template
from src.Game.game import run

app = Flask(__name__, template_folder='Dashboard') 

@app.route('/')
def dashboard():
    return render_template('idea.html')

@app.route('/game')
def game():
    result = game.run()  
    return f"Game result: {result}"

if __name__ == '__main__':
    app.run(debug=True)
