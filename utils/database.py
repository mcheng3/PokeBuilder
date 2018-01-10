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
    c.execute("CREATE TABLE teams (teamid INT PRIMARY KEY, user TEXT, name TEXT, version TEXT, weaknesses TEXT, strengths TEXT, upvotes INT);")
    
    #creates pokemon table
    c.execute("CREATE TABLE pokemon (pkmnid INT PRIMARY KEY, teamid INT, species TEXT, gender TEXT, level INT, ability TEXT, moves TEXT, item TEXT, nature TEXT);")

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
def add_favorite(username, teamid):
    db = sqlite3.connect(f)
    c = db.cursor()

    #retreive favorites list from table
    c.execute("SELECT favorites FROM users WHERE user = \"%s\";" %(username))
    fav_t = c.fetchone()

    #appending string in favorites column
    fav_s = fav_t[0]
    fav_s = fav_s + "," + teamid

    #updating database
    c.execute("UPDATE users SET favorites = \"%s\" WHERE user = \"%s\";" %(fav_s, username))

    db.commit()
    db.close()

#finds username
def find_user(username):
    db = sqlite3.connect(f)
    c = db.cursor()

    #looks through users table
    c.execute("SELECT user FROM users WHERE user = \"%s\";" %(username))
    found = c.fetchone()[0]

    db.commit()
    db.close()

    #returns true if username is found
    if found == username:
        return True
    else:
        return False


#find password
def match_pass(username, password):
    db = sqlite3.connect(f)
    c = db.cursor()
    
    #looks through table for pass
    c.execute("SELECT pass FROM users WHERE user = \"%s\";" %(username))
    found = c.fetchone()[0]

    #returns if password is found
    if found == password:
        return True
    else:
        return False
    
    db.commit()
    db.close()
    
#creates a new team
def new_team(username, name, version, weaknesses, strengths, pkmnlist):
    db = sqlite3.connect(f)
    c = db.cursor()

    #creating a new teamid
    c.execute("SELECT teamid FROM teams ORDER BY teamid DESC LIMIT 1;")
    teamid = c.fetchone()[0]
    teamid += 1

    #adding team to table
    c.execute("INSERT INTO teams VALUES(%d, \"%s\", \"%s\", \"%s\", \"%s\", \"%s\", 0);" %(teamid, username, name, version, weaknesses, strengths))
    
    db.commit()
    db.close()


#creating a new pokemon
def create_poke(teamid, species, gender, level, ability, moves, item, nature):
    db = sqlite3.connect(f)
    c = db.cursor()

    #creating a new teamid
    c.execute("SELECT teamid FROM teams ORDER BY teamid DESC LIMIT 1;")
    pkmnid = c.fetchone()
    pkmnid += 1

    #adding team to table
    c.execute("INSERT INTO pokemon VALUES(%d, %d, \"%s\", \"%s\", %d, \"%s\", \"%s\", \"%s\", \"%s\");" %(pkmnid, teamid, species, gender, level, ability, moves, item, nature))
    
    db.commit()
    db.close()

    
#updating pokemon
#def update_poke(

