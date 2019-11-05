from flask import Flask
from flask import render_template
from flask import g

import sqlite3

app = Flask(__name__)
dev_host = '127.0.0.1'
dev_port = '8080'
db = '../data/db.db'

@app.route('/')
def index():
    return render_template('index.html')


if __name__ == '__main__':
    app.run(host=dev_host, port=dev_port)

