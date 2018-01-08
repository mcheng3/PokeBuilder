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
    return render_template("home.html",
                               logged_in = False,
                               top_ten = ["a", "b", "c", "d", "e",
                                              "f", "g", "h", "i", "j"])


#---------------------------------------
# LOGIN PAGE
# authenticate user
#---------------------------------------
@app.route('/login')
def login():
    return render_template("login.html")


#---------------------------------------
# SIGN UP PAGE
# add user to database
#---------------------------------------
@app.route('/signup')
def signup():
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
    return render_template("profile.html",
                               user = "ANON",
                               logged_in = True,
                               fav_teams = ["fTeamA", "fTeamB", "fTeamC"],
                               my_teams = ["mTeamA", "mTeamB", "mTeamC"])


#---------------------------------------
# SEARCH PAGE
# shows teams related to search
#---------------------------------------
@app.route('/search')
def search():
    return render_template("search.html",
                               results = ["sTeamA", "sTeamB", "sTeamC"],
                               logged_in = False)


#---------------------------------------
# CREATE PAGE
# create a new team
#---------------------------------------
@app.route('/createteam')
def create():
    return render_template("create.html",
                               logged_in = True)


#---------------------------------------
# EDIT PAGE
# edit team pokemon members overall
#---------------------------------------
@app.route('/editteam')
def editT():
    return render_template("edit_team.html",
                               logged_in = True,
                               team = "TeamA",
                               pokemon = ["a", "b", "c", "d", "e",
                                              "f", "g", "h", "i", "j"],
                               poke_att1 = ["a1", "b1", "c1", "d1", "e1",
                                                "f1", "g1", "h1", "i1", "j1"],
                               poke_att2 = ["a2", "b2", "c2", "d2", "e2",
                                                "f2", "g2", "h2", "i2", "j2"],
                               poke_att3 = ["a3", "b3", "c3", "d3", "e3",
                                                "f3", "g3", "h3", "i3", "j3"])                                              

#---------------------------------------
# EDIT POKEMON
# edit specific pokemon traits
#---------------------------------------
@app.route('/editpokemon')
def editP():
    return render_template("edit_pokemon.html",
                               logged_in = True,
                               pokemon = "pokemon name",
                               gender_opt = ["m", "f"],
                               level_opt = [1, 2, 3, 4, 5],
                               abilities = ["walk", "eat", "sleep"],
                               moves = "what moves?",
                               item = "what item?",
                               nature = "what nature?")

if __name__ == "__main__":
    app.debug = True
app.run()
