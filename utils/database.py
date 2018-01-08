import sqlite3
from os import system
import hashlib

#creates database
def create_db():
    db = sqlite3.connect(f)
    c = db.cursor()
    
    #creates users table
    c.execute("CREATE TABLE users (user TEXT PRIMARY KEY, pass TEXT, favorites TEXT);")
    
    #creates teams table
    c.execute("CREATE TABLE teams (teamid TEXT PRIMARY KEY, user TEXT, name TEXT, version TEXT, weaknesses TEXT, strengths TEXT, upvotes INT);")
    
    #creates pokemon table
    c.execute("CREATE TABLE pokemon (pkmnid TEXT PRIMARY KEY, teamid TEXT, species TEXT, gender TEXT, level INT, ability TEXT, moves TEXT, item TEXT, nature TEXT);")

    db.commit()
    db.close()

    
#adds new user
def new_user(username, password):
    db = sqlite3.connect(f)
    c = db.cursor()

    #adds user to table
    c.execute("INSERT INTO users VALUES(\"%s\", \"%s\", \"\");" %(username, password))

    db.commit()
    db.close()

    
#adds a team to the favorites list
def add_favorite(username, teamid);
    db = sqlite3.connect(f)
    c = db.cursor()

    #retreive favorites list from table
    c.execute("SELECT favorites FROM users WHERE user = \"%s\";" %(username))
    fav_t = c.fetchone()

    #appending string in favorites column
    fav_s = fav_t[0]
    fav_s = fav_s + "," + teamid

    #updating database
    c.execute("UPDATE users SET favorites = \"%s\" WHERE user = \"%s\";;" %(fav_s, username))

    db.commit()
    db.close()

#creates a new team
def new_team(username, name, version, weaknesses, strengths, pkmnlist)
    db = sqlite3.connect(f)
    c = db.cursor()

    #not done
    
    db.commit()
    db.close()
