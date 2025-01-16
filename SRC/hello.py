from flask import Flask, render_template
from datetime import datetime

app = Flask(__name__)


@app.route("/")
def home():
    return render_template('test.html')



# java script qui demande au serveur regulièremebnt si de nouvelles données sont ajoutées