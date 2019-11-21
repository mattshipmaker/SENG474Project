from flask import Flask
from flask import render_template
from flask import g
from flask import request
from flask import jsonify

import sqlite3
import db

import linreg
import numpy as np

app = Flask(__name__)
dev_host = '127.0.0.1'
dev_port = '8080'
database_name = '../data/db.db'


@app.route('/predict', methods=['POST'])
def predict():
    x = float(request.args.get('x'))
    y = float(request.args.get('y'))
    z = float(request.args.get('z'))

    X = np.array([x, y, z])

    ans = linreg.run(X, 2016)

    return jsonify(ans)

@app.route('/', methods=['GET'])
def index():
    return render_template('index.html')

@app.route('/country', methods=['GET'])
def country_info():

    id = request.args.get('id')

    country = db.get_country(id)
    country_data = db.get_country_data(id)

    return render_template("country.html", country=country[0], country_data=country_data)


if __name__ == '__main__':
    app.run(host=dev_host, port=dev_port)

