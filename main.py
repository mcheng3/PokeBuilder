from flask import Flask, flash, render_template, request, session, redirect, url_for
import sqlite3
from utils import api, database, auth
import time

app = Flask(__name__)
app.secret_key = "THIS IS NOT SECURE"


#---------------------------------------
# FRONT PAGE
# about information; current top 10 teams
#---------------------------------------
@app.route('/')
def root():
    return render_template("index.html",
                               loggedin = auth.is_logged_in(),
                               top_ten = ["a", "b", "c", "d", "e",
                                              "f", "g", "h", "i", "j"])


#---------------------------------------
# LOGIN PAGE
# authenticate user
#---------------------------------------
@app.route('/login', methods = ['POST', 'GET'])
def login():
    # checks for post method to respond to submit button
    if request.method == 'POST':
        # uses the database method to check the login
        # print "username: " + request.form['usr'] + "\npassword: " + request.form['pwd']
        log_res = auth.login( request.form['usr'], request.form['pwd'] )
        if log_res == 0 :
            return redirect(url_for('root'))
        else:
            return redirect(url_for('login'))
    # just render normally if no post
    else:
        return render_template("login.html")

#---------------------------------------
# SIGN UP PAGE
# add user to database
#---------------------------------------
@app.route('/signup', methods = ['POST', 'GET'])
def signup():
    # CREATE ACCOUNT
    if request.method == 'POST':
        cr_acc_res = auth.sign_up( request.form['usr'], request.form['pwd'] )
        # if successful
        if cr_acc_res == 0:
            flash("Account created!")
            return redirect( url_for('login') )
        # if username already exists
        if cr_acc_res == 1:
            return redirect( url_for('signup') )
    return render_template("signup.html")

#---------------------------------------
# LOGOUT PAGE
#---------------------------------------
@app.route('/logout')
def logout():
    logout();
    return redirect( url_for("root") )


#---------------------------------------
# PROFILE PAGE
# shows user info, created teams, and upvoted teams
#---------------------------------------
@app.route('/profile')
def profile():
    return render_template("profile.html",
                               user = "ANON",
                               loggedin = True,
                               fav_teams = ["fTeamA", "fTeamB", "fTeamC"],
                               my_teams = ["mTeamA", "mTeamB", "mTeamC"])


#---------------------------------------
# SEARCH PAGE
# shows teams related to search
#---------------------------------------
@app.route('/search', methods = ['POST', 'GET'])
def search():
#    api.search_query(request.form['search'])
    return render_template("search.html",
                               results = ["sTeamA", "sTeamB", "sTeamC"],
                               loggedin = False)


#---------------------------------------
# CREATE PAGE
# create a new team
#---------------------------------------
@app.route('/createteam')
def create():
    return render_template("edit_team.html",
                               loggedin = True)


#---------------------------------------
# EDIT PAGE
# edit team pokemon members overall
#---------------------------------------
@app.route('/editteam')
def edit_team():
    pokedict = { 0001 : 'bulbasaur', 0004 : 'squirtle', 0007 : 'charmander' }
    return render_template("edit_team.html",
                               loggedin = True,
                               teamname = "TeamA",
                               pokemon = pokedict,
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
def edit_pokemon():
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
