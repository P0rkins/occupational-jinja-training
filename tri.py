#Big L is the coolest cat in the village

from flask import Flask, render_template
from utils import occupations

app = Flask(__name__) #create Flask objec


@app.route("/") #assign following fxn to run when root route requested
def hello_world():
    return "Big L is the coolest cat in the village. Be like him."


@app.route("/occupations")
def occupy():
    return render_template('model.html', collection = occupations.store(), job = randomize())
    
if __name__ == "__main__":
    #enable debugging, auto-restarting of server when this file is modified
    app.debug = True 
    app.run()
