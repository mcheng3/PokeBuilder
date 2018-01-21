from flask import Flask, flash, render_template, request, session, redirect, url_for
import sqlite3
from utils import api, database, auth
import time, json

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
        return render_template("login.html", loggedin=auth.is_logged_in())

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
    return render_template("signup.html", loggedin=auth.is_logged_in())

#---------------------------------------
# LOGOUT PAGE
#---------------------------------------
@app.route('/logout')
def logout():
    auth.logout();
    return redirect( url_for("root") )


#---------------------------------------
# PROFILE PAGE
# shows user info, created teams, and upvoted teams
#---------------------------------------
@app.route('/profile')
def profile():
    fav_list = database.return_favorites(session["user"])[0][0].split(",")
    fav_teams = list()
    for team in fav_list:
        if team != '':
            fav_teams.append(database.find_team(int(team)))
    return render_template("profile.html",
                               user = session['user'],
                               loggedin = auth.is_logged_in(),
                               fav_teams = fav_teams,
                               my_teams = database.get_teams(session['user']))


#---------------------------------------
# SEARCH PAGE
# shows teams related to search
#---------------------------------------
@app.route('/search', methods = ['POST', 'GET'])
def search():
    print(request.args['search'])
    results = database.search_name(request.args['search'])
    return render_template("search.html",
                           results = results,
                           loggedin = auth.is_logged_in())


#---------------------------------------
# CREATE PAGE
# create a new team
#---------------------------------------
@app.route('/createteam', methods = ['POST', 'GET'])
def create():
    #ajax should maybe check if all form items are filled before submitting to database
    if request.method == 'POST':
        #database.delete_team(session['user'], request.form['teamname'])
        database.new_team(session['user'], request.form['teamname'], request.form['teamdesc'], "NONE", "NONE", "NONE", 0)
        return redirect(url_for("root"))
    else:
        return render_template("edit_team.html",
                                   loggedin = auth.is_logged_in())

#---------------------------------------
# VIEW TEAM
# view team details
#---------------------------------------
@app.route('/viewteam', methods = ['POST', 'GET'])
def view_team():
    if request.method == 'POST':
        if 'edit' in request.form:
            return redirect(url_for("edit_team", id = request.args['id']))
        elif 'favorite' in request.form:
            if 'user' in session:
                id = request.args["id"]
                database.add_favorite(session["user"], id)
                return redirect(url_for("view_team", id = id))
            else:
                return redirect(url_for('login'))
        else:
            id = request.args["id"]
            #remove favorite
            return redirect(url_for("view_team", id = id))
    else:
        id = int(request.args["id"])
        team = database.find_team(id)
        mine = 'user' in session and session["user"] == team[1]
        faves = list()
        if 'user' in session: 
            faves = database.return_favorites(session["user"])[0][0].split(",")
        return render_template("view_team.html",
                               loggedin = auth.is_logged_in(),
                               team = team,
                               favorited = str(id) in faves,
                               mine = mine,
                               poke_teams = ["yea", "yeas", "sdfa"])

#---------------------------------------
# EDIT PAGE
# edit team pokemon members overall
#---------------------------------------
@app.route('/editteam', methods = ['POST', 'GET'])
def edit_team():
    if request.method == 'POST':
        database.update_team()
    else:
        pokedict = { 0001 : 'bulbasaur', 0004 : 'squirtle', 0007 : 'charmander' }
        id = int(request.args["id"])
        team = database.find_team(id)
        return render_template("edit_team.html",
                                   loggedin = auth.is_logged_in(),
                                   teamname = "TeamA",
                                   pokemon = pokedict,
                                   poke_att1 = ["a1", "b1", "c1", "d1", "e1",
                                                "f1", "g1", "h1", "i1", "j1"],
                                   poke_att2 = ["a2", "b2", "c2", "d2", "e2",
                                                "f2", "g2", "h2", "i2", "j2"],
                                   poke_att3 = ["a3", "b3", "c3", "d3", "e3",
                                                "f3", "g3", "h3", "i3", "j3"])


#---------------------------------------
# CREATE POKEMON
# add new pokemon to team
#---------------------------------------
@app.route('/createpokemon', methods = ['POST', 'GET'])
def create_pokemon():
    if request.method == 'POST':
        database.create_poke(things)
    return render_template("edit_pokemon.html",
                               loggedin = auth.is_logged_in(),
                               pokemon = "",
                               gender_opt = ["m", "f"],
                               level_opt = [1, 2, 3, 4, 5],
                               abilities = ["walk", "eat", "sleep"],
                               moves = "what moves?",
                               item = "what item?",
                               nature = "what nature?")
    
#---------------------------------------
# EDIT POKEMON
# edit specific pokemon traits
#---------------------------------------
@app.route('/editpokemon', methods = ['POST', 'GET'])
def edit_pokemon():
    if request.method == 'POST':
        update_poke(stuff)
    return render_template("edit_pokemon.html",
                               loggedin = auth.is_logged_in(),
                               pokemon = "pokemon name",
                               gender_opt = ["m", "f"],
                               level_opt = [1, 2, 3, 4, 5],
                               abilities = ["walk", "eat", "sleep"],
                               moves = "what moves?",
                               item = "what item?",
                               nature = "what nature?")

@app.route("/pokedata")
def pokedata():
    data = request.args.get("name")
    results = api.search_poke(data)
    print results
    moves = []
    print results["moves"]
    for each in results["moves"]:
        moves.append(each["move"]["name"])
    print moves
    abilities = []
    for each in results["abilities"]:
        abilities.append(each["ability"]["name"])
    response = {'img': results["sprites"]["front_default"], 'moves': moves, "type": results["types"], 'abilities': abilities}
    return json.dumps(response)

if __name__ == "__main__":
    app.debug = True
    app.run()
