from flask import Flask
from flask_mysqldb import MySQL
import os

app = Flask(__name__)
app.config.from_pyfile('config.py')

db = MySQL(app)
from views import *

if __name__ == '__main__': #Faz com que só execute esse if se esse arquivo for execcutado diretamente
    app.run(host='0.0.0.0', port=8080, debug=True)