from flask import *
from pol2vec import *
import json

app = Flask(__name__)
pol2vec = Pol2Vec('politician_model')

@app.route('/')
def home():
    # main page
    return render_template('home.html')

@app.route('/search')
def search():
    return render_template('search.html')

@app.route('/results', methods=['POST'])
def results():
    app.logger.info(request.form['politicians'])
    query = Pol2Vec.process_query(request.form['politicians'])
    results = pol2vec.most_similar(query['positives'], query['negatives'])
    app.logger.info(results)
    return render_template('result.html', results = results)

@app.route('/contacts')
def contacts():
    return render_template('contact.html')