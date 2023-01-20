from flask import Flask, request, render_template, redirect, session, abort
import psycopg2
import os
from flask_sqlalchemy import SQLAlchemy
psycopg2.extensions.register_type(psycopg2.extensions.UNICODE)
psycopg2.extensions.register_type(psycopg2.extensions.UNICODEARRAY)
#from models import db
#app = flask.Flask(name)



app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://vanick:123456@localhost/base'
app.secret_key = 'V\xa9\x00\x8d\xef\x1bL\xc8ToNJ'
db = SQLAlchemy(app)

@app.route('/', methods=['GET', 'POST'])
def login():
    error = None
    if request.method == 'POST':
        if (
            request.form['username'] == 'admin'
            and request.form['password'] == 'admin'
        ):
            return redirect('home')
        error = 'Invalid Credentials. Please try again.'
        session['logout'] = True
    return render_template('pages/login.html', error=error)

@app.route('/home', methods=['GET', 'POST'])
def home():
    return render_template('pages/home.html')

@app.route('/licence/algorithmique', methods=['GET', 'POST'])
def algorithmique():
	connec = psycopg2.connect(database="base", user = "vanick", password = "12345", host = "127.0.0.1", port = "5432")
	cux = connec.cursor()
	cux.execute("SELECT * FROM emg")
	cns = cux.fetchall()
	connec.close()
	if request.method == 'POST':
		return redirect('/licence/algorithmique/emargement')
	return render_template('pages/licence/algorithmique.html', ligne = cns)

@app.route('/licence/robotique', methods=['GET', 'POST'])
def robotique():
	connec = psycopg2.connect(database="base", user = "vanick", password = "12345", host = "127.0.0.1", port = "5432")
	cux = connec.cursor()
	cux.execute("SELECT * FROM emg")
	cns = cux.fetchall()
	connec.close()
	if request.method == 'POST':
		return redirect('/licence/robotique/emargement')
	return render_template('pages/licence/robotique.html', ligne = cns)	

@app.route('/licence/programmation', methods=['GET', 'POST'])
def programmation():
	connec = psycopg2.connect(database="base", user = "vanick", password = "123456", host = "127.0.0.1", port = "5432")
	cux = connec.cursor()
	cux.execute("SELECT * FROM emg")
	cns = cux.fetchall()
	connec.close()
	if request.method == 'POST':
		return redirect('/licence/programmation/emargement')
	return render_template('pages/licence/programmation.html', ligne = cns)	

@app.route('/licence/algorithmique/emargement', methods=['GET', 'POST'])
def emargement_al():
    if request.method == 'POST':
        dates = request.form['dates']
        lecon = request.form['lecons']
        absent = request.form['absents']
        connex = psycopg2.connect(database="base", user = "vanick", password = "123456", host = "127.0.0.1", port = "5432")
        cux = connex.cursor()
        cux.execute('''CREATE TABLE IF NOT EXISTS emg (id INT PRIMARY KEY NOT NULL,  date VARCHAR(15) NOT NULL, lecons VARCHAR(50) NOT NULL, absents VARCHAR(50) NOT NULL)''')
        cux.execute("INSERT INTO emg (date, lecons, absents) VALUES (%s,%s,%s)", (dates,lecon,absent))
        connex.commit()
        return redirect('pages/licence/algorithmique')
    return render_template('pages/licence/emargement.html')


@app.route('/licence/robotique/emargement', methods=['GET', 'POST'])
def emargement_ro():
    if request.method == 'POST':
        dates = request.form['dates']
        lecon = request.form['lecons']
        absent = request.form['absents']
        connex = psycopg2.connect(database="base", user = "vanick", password = "123456", host = "127.0.0.1", port = "5432")
        cux = connex.cursor()
        cux.execute('''CREATE TABLE IF NOT EXISTS emg (id INT PRIMARY KEY NOT NULL,  date VARCHAR(15) NOT NULL, lecons VARCHAR(50) NOT NULL, absents VARCHAR(50) NOT NULL)''')
        cux.execute("INSERT INTO emg (date, lecons, absents) VALUES (%s,%s,%s)", (dates,lecon,absent))
        connex.commit()
        return redirect('pages/licence/robotique')
    return render_template('pages/licence/emargement.html')

@app.route('/licence/programmation/emargement', methods=['GET', 'POST'])
def emargement_pro():
    if request.method == 'POST':
        dates = request.form['dates']
        lecon = request.form['lecons']
        absent = request.form['absents']
        connex = psycopg2.connect(database="base", user = "vanick", password = "123456", host = "127.0.0.1", port = "5432")
        cux = connex.cursor()
        cux.execute('''CREATE TABLE IF NOT EXISTS emg (id INT PRIMARY KEY NOT NULL,  date VARCHAR(15) NOT NULL, lecons VARCHAR(50) NOT NULL, absents VARCHAR(50) NOT NULL)''')
        cux.execute("INSERT INTO emg (date, lecons, absents) VALUES (%s,%s,%s)", (dates,lecon,absent))
        connex.commit()
        return redirect('pages/licence/programmation')
    return render_template('pages/licence/emargement.html')

if __name__ == '__main__':
	app.secret_key = os.urandom(12)
	app.run(debug=True,host='0.0.0.0', port=3000)
	db.init_app(app)