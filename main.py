from flask import Flask, flash, render_template, request, session, redirect, url_for
#import sqlite3
#import utils.api as api
#import utils.database as db
#import utils.auth as auth
#import time

app = Flask(__name__)
app.secret_key = "THIS IS NOT SECURE"


#---------------------------------------
# FRONT PAGE
# about information; current top 10 teams
#---------------------------------------
@app.route('/')
def root():
    return render_template("home.html");


#---------------------------------------
# LOGIN PAGE
# authenticate user
#---------------------------------------
@app.route('/login')
def login():
    return render_template("login.html")


#---------------------------------------
# SIGN UP PAGE
# authenticate user
#---------------------------------------
@app.route('/signup')
def login():
    return render_template("signup.html")

#---------------------------------------
# LOGOUT PAGE
#---------------------------------------
@app.route('/logout')
def logout():
    return redirect( url_for("main") )


#---------------------------------------
# PROFILE PAGE
# shows user info, created teams, and upvoted teams
#---------------------------------------
@app.route('/profile')
def profile():
    return render_template("profile.html")


#---------------------------------------
# SEARCH PAGE
# shows teams related to search
#---------------------------------------
@app.route('/search')
def search():
    return render_template("search.html")


#---------------------------------------
# CREATE PAGE
# create a new team
#---------------------------------------
@app.route('/createteam')
def create():
    return render_template("create.html")


#---------------------------------------
# EDIT PAGE
# edit team pokemon members overall
#---------------------------------------
@app.route('/editteam')
def editT():
    return render_template("edit_team.html")


#---------------------------------------
# EDIT POKEMON
# edit specific pokemon traits
#---------------------------------------
@app.route('/editpokemon')
def editP():
    return render_template("edit_pokemon.html")
