from flask import Flask
from flask import render_template
from flask import g

import sqlite3
import db

app = Flask(__name__)
dev_host = '127.0.0.1'
dev_port = '8080'
database_name = '../data/db.db'

@app.route('/predict?',methods=['POST'])
def predict(x, y, z):
    return 

@app.route('/', methods=['GET'])
def index():
    return render_template('index.html')

@app.route('/country?id=<id>', methods=['GET'])
def country_info(id):

    country = db.get_country(id)
    country_data = db.get_country_data(id)

    return render_template("country.html",country = country[0], country_data = country_data)


if __name__ == '__main__':
    app.run(host=dev_host, port=dev_port)

