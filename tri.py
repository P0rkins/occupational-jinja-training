#Big L is the coolest cat in the village

from flask import Flask, render_template
app = Flask(__name__) #create Flask object

@app.route("/") #assign following fxn to run when root route requested
def hello_world():
    return "No hablo queso!"

khal = [0,1,1,2,3,5,8]

@app.route("/my_foist_template")
def test_tmplt():
    return render_template( 'model_tmplt.html', foo="foooood", collection=khal)
    
if __name__ == "__main__":
    #enable debugging, auto-restarting of server when this file is modified
    app.debug = True 
app.run()
