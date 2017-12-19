from flask import *
from pol2vec import *

app = Flask(__name__)
pol2vec = Pol2Vec('politician_model')

@app.route('/')
def hello_world():
    # main page
    return render_template('home.html')

@app.route('/search')
def search():
    return render_template('search.html')

@app.route('/results')
def results():
    return render_template('result.html')

@app.route('/features')
def features():
    return render_template('features.html')

@app.route('/contacts')
def contacts():
    return render_template('contact.html')