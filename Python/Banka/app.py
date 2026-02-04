from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return '<a href="/formular">Formular</a>'

@app.route('/formular')
def hello():
    return 'Hello, World'