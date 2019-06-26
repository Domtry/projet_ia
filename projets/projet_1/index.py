#! /usr/bin/env python2
# -*- coding : utf-8 -*-

#importation des differents module
from flask import *
import psycopg2
import os
from modules import tests as test
from flask_sqlalchemy import SQLAlchemy

root = Flask(__name__)
root.debug = False
root.secret_key = 'projet_IA_v1'

@root.route('/', methods=['GET', 'POST'])
@root.route('/login/', methods=['GET', 'POST'])
def login_page():
    if request.method == 'POST':
        
        user_name = request.form['name']    
        password = request.form['password']
        if test.isName(user_name) and test.isPassword_A(password) :
            return redirect(url_for('profil', name=user_name))    
        else :
            flash('le nom ou mot de passe n\'est pas correct', 'erreur')
            return redirect(url_for('login_page'))  
    else :
        return render_template('login.html')

  
@root.route('/profil/<name>', methods=['GET'])
def profil(name = None):
    if name is not None :
        return render_template('profil.html', titre='Profil', user=name)
    else :
        return redirect(url_for('login_page'))


@root.errorhandler(401)
@root.errorhandler(404)
@root.errorhandler(500)
def error_page(error):
    return render_template('error404.html', titre="Error")

if __name__ == "__main__":
    root.run(debug=True, host='127.0.0.1',  port=5000)