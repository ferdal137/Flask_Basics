from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"

  
#To run the app write in the terminal:
#$ export FLASK_APP="run.py"
#$ flask run
