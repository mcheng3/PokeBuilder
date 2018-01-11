import sqlite3
from os import system
import hashlib

f = "data/app.db"

#creates database
def create_db():
    db = sqlite3.connect(f)#, check_same_thread=False)
    c = db.cursor()
    #creates users table
    c.execute("CREATE TABLE users (user TEXT PRIMARY KEY, pass TEXT, favorites TEXT);")

    #creates teams table
    c.execute("CREATE TABLE teams (teamid INT PRIMARY KEY, user TEXT, name TEXT, desc TEXT, version TEXT, weaknesses TEXT, strengths TEXT, upvotes INT);")

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

    c.execute("SELECT user FROM users WHERE user = \"%s\";" % ( username ))
    found = str(c.fetchone())[3:-3]
    print(found)

    db.commit()
    db.close()

    if found == username:
        return True
    else:
        return False

#finds team
def find_team(teamname):
    db = sqlite3.connect(f)
    c = db.cursor()

    c.execute("SELECT \* FROM teams WHERE name = \"%s\";" % ( teamname ))
    found = str(c.fetchone())
    print(found)

    db.commit()
    db.close()

    if found == teamname:
        return True
    else:
        return False

#get all team by user
def get_teams(username):
    db = sqlite3.connect(f)
    c = db.cursor()

    command = "SELECT name, desc FROM teams WHERE user = \"%s\";" 
    found = list()
    for row in c.execute(command %(username)):
        found.append(row)
               
    db.commit()
    db.close()
    return found

def match_pass(username, password):
    db = sqlite3.connect(f)
    c = db.cursor()

    #looks through table for pass
    c.execute("SELECT pass FROM users WHERE user = \"%s\";" %(username))
    found = str(c.fetchone())[3:-3]

    #returns if password is found
    if found == password:
        return True
    else:
        return False

    db.commit()
    db.close()

#creates a new team
def new_team(username, name, desc, version, weaknesses, strengths, pkmnlist):
    db = sqlite3.connect(f)
    c = db.cursor()
    
    #creating a new teamid
    c.execute("SELECT teamid FROM teams ORDER BY teamid DESC LIMIT 1;")
    teamid = int(c.fetchone())
    teamid += 1

    #adding team to table
    c.execute("INSERT INTO teams VALUES (%d, \"%s\", \"%s\", \"%s\", \"%s\", \"%s\", \"%s\", 0);" %(teamid, username, name, desc, version, weaknesses, strengths))

    db.commit()
    db.close()

#deletes team
def delete_team(username, name):
    db = sqlite3.connect(f)
    c = db.cursor()
    
    #creating a new teamid
    c.execute("DELETE FROM teams WHERE user=\"%s\" and name=\"%s\"" %(username, name))

    db.commit()
    db.close()


#creating a new pokemon
def create_poke(teamid, species, gender, level, ability, moves, item, nature):
    db = sqlite3.connect(f)
    c = db.cursor()

    #creating a new teamid
    c.execute("SELECT teamid FROM teams ORDER BY teamid DESC LIMIT 1;")
    pkmnid = str(c.fetchone()[0])
    pkmnid += 1

    #adding team to table
    c.execute("INSERT INTO pokemon VALUES(%d, %d, \"%s\", \"%s\", %d, \"%s\", \"%s\", \"%s\", \"%s\");" %(pkmnid, teamid, species, gender, level, ability, moves, item, nature))

    db.commit()
    db.close()


#updating pokemon

#def update_poke(

if __name__ == "__main__":
    system("rm data/app.db")
    create_db()
#    new_team("kl", "second", "THis is great", "NONE", "NONE", "NONE", 0)
