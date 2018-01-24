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
    c.execute("CREATE TABLE teams (teamid INT PRIMARY KEY, user TEXT, name TEXT, desc TEXT, version TEXT, weaknesses TEXT, strengths TEXT, upvotes INT, pkmnid TEXT);")
    #creates pokemon table
    c.execute("CREATE TABLE pokemon (pkmnid INT PRIMARY KEY, species TEXT, gender TEXT, level INT, ability TEXT, moves TEXT, item TEXT, nature TEXT, img TEXT);")

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

    #retrieve favorites list from table
    c.execute("SELECT favorites FROM users WHERE user = \"%s\";" %(username))
    fav_t = c.fetchone()

    #appending string in favorites column
    fav_s = fav_t[0]
    if fav_s == "":
        fav_s = "" + str(teamid)
    else:
        fav_s = fav_s + "," + str(teamid)

    #updating database
    c.execute("UPDATE users SET favorites = \"%s\" WHERE user = \"%s\";" %(fav_s, username))

    #updating team upvotes
    c.execute("SELECT upvotes FROM teams WHERE teamid = %d;" %(teamid))
    votes = c.fetchone()[0]
    votes += 1
    c.execute("UPDATE teams SET upvotes = %d WHERE teamid = %d;" %(votes, teamid))

    db.commit()
    db.close()

#unfavorites a team 
def remove_favorite(username, remove_team):
    db = sqlite3.connect(f)
    c = db.cursor()
    
    #deleting from users datatable
    c.execute("SELECT favorites FROM users WHERE user = \"%s\";" %(username))
    old_string = c.fetchone()[0]
    if old_string.endswith(str(remove_team)):
        new_string = old_string.replace(str(remove_team), '')
    else:
        new_string = old_string.replace(str(remove_team) + ",", '')

    c.execute("UPDATE users SET favorites=\"%s\" WHERE user = \"%s\";" %(new_string, username))
    db.commit()
        
    #updating team upvotes
    c.execute("SELECT upvotes FROM teams WHERE teamid = %d;" %(remove_team))
    votes = c.fetchone()[0]
    votes -= 1
    c.execute("UPDATE teams SET upvotes = %d WHERE teamid = %d;" %(votes, remove_team))
    
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

#searches for team names / usernames with a given string, and returns a list
def search_name(search):
    db = sqlite3.connect(f)
    c = db.cursor()
    result = []
    c.execute("SELECT name,teamid,user FROM teams WHERE name LIKE '%s';" %(search))
    for row in c:
        result.append(row)

    c.execute("SELECT name,teamid,user FROM teams WHERE user LIKE '%s';" %(search))
    for row in c:
        result.append(row)

    print result
    return result

    db.commit()
    db.close()

#finds team
def find_team(teamid):
    db = sqlite3.connect(f)
    c = db.cursor()

    c.execute("SELECT * FROM teams WHERE teamid = %d;" % ( teamid ))
    team = None
    for row in c:
        team = row

    db.commit()
    db.close()
    if row[0] == teamid:
       return team
    else:
      return None

#get all team by user
def get_teams(username):
    db = sqlite3.connect(f)
    c = db.cursor()

    command = "SELECT teamid, name, desc FROM teams WHERE user = \"%s\";"
    found = list()
    for row in c.execute(command %(username)):
        found.append(row)

    db.commit()
    db.close()

    return found

#returns user's favorites
def return_favorites(user):
    db = sqlite3.connect(f)
    c = db.cursor()

    command = "SELECT favorites FROM users WHERE user = \"%s\";"
    favorite = list()
    for row in c.execute(command %(user)):
        favorite.append(row)

    db.commit()
    db.close()

    return favorite


#returns pokemon info by searching the pkmnid
def return_pkmn(pkmnid):
    db = sqlite3.connect(f)
    c = db.cursor()

    command = "SELECT * FROM pokemon WHERE pkmnid = %d;"
    pkmn_info = list()
    for row in c.execute(command %(pkmnid)):
        print row
        pkmn_info.append(row)

    db.commit()
    db.close()
    print pkmn_info
    return pkmn_info

#returns type (nature) of the pokemon
def return_type(pkmnid):
    db = sqlite3.connect(f)
    c = db.cursor()

    c.execute("SELECT nature FROM pokemon WHERE pkmnid = %d;" %(pkmnid))
    nature_s = c.fetchone()[0]
    nature_l = nature_s.split(",")

    return nature_l

    db.commit()
    db.close()

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

'''
#creates a new team
def new_team(teamid, username, name, desc, version, weaknesses, strengths, pkmnlist):
    db = sqlite3.connect(f)
    c = db.cursor()

    #creating a new teamid
    command ="SELECT teamid FROM teams ORDER BY teamid DESC LIMIT 1;"
    teamid = 0
    for row in c.execute(command):
        teamid = row[0]

    #adding team to table
    c.execute("INSERT INTO teams VALUES (%d, \"%s\", \"%s\", \"%s\", \"%s\", \"%s\", \"%s\", 0, \"%s\");" %(teamid+1, username, name, desc, version, weaknesses, strengths, pkmnlist))

    db.commit()
    db.close() '''

# helper function for getting the next teamid
def next_teamid(user):
    db = sqlite3.connect(f)
    c = db.cursor()

    command ="SELECT teamid FROM teams ORDER BY teamid DESC LIMIT 1;"
    teamid = 0
    for row in c.execute(command):
        teamid = row[0]

     #adding team to table
    c.execute("INSERT INTO teams VALUES (%d, \"%s\", \"%s\", \"%s\", \"%s\", \"%s\", \"%s\", 0, \"%s\");" %(teamid+1, user, "", "", "", "", "", ""))

    db.commit()
    db.close()

    return teamid+1



#deletes team
def delete_team(teamid):
    db = sqlite3.connect(f)
    c = db.cursor()

    #creating a new teamid
    c.execute("DELETE FROM teams WHERE teamid = %d" %(teamid))

    db.commit()
    db.close()

#creating a new pokemon
def create_poke(species, gender, level, ability, moves, item, nature, teamid, img):
    db = sqlite3.connect(f)
    c = db.cursor()

    #creating a new pkmnid
    c.execute("SELECT pkmnid FROM pokemon ORDER BY pkmnid DESC LIMIT 1;")
    pkmnid = 0
    for row in c: 
        pkmnid = row[0]

    #adding pokemon to table
    c.execute("INSERT INTO pokemon VALUES(%d, \"%s\", \"%s\", %d, \"%s\", \"%s\", \"%s\", \"%s\", \"%s\");" %(pkmnid+1, species, gender, level, ability, moves, item, nature, img))

    #adding pkmnid to teams table
    c.execute("SELECT pkmnid FROM teams WHERE teamid = %d;" %(teamid))
    pkmnlist = c.fetchone()[0]
    if pkmnlist == "": 
        pkmnlist = "%d" %(pkmnid+1)
    else:
        pkmnlist += ", %d" %(pkmnid+1)
    c.execute("UPDATE teams SET pkmnid = \"%s\" WHERE teamid = %d;" %(pkmnlist, teamid))

    db.commit()
    db.close()

#updating pokemon
def update_poke(pkmnid, species, gender, level, ability, moves, item, nature, img):
    db = sqlite3.connect(f)
    c = db.cursor()

    #update info
    c.execute("UPDATE pokemon SET species = \"%s\", gender = \"%s\", level = %d, ability = \"%s\", moves = \"%s\", item = \"%s\", nature = \"%s\", img = \"%s\" WHERE pkmnid = \"%s\";" %(species, gender, level, ability, moves, item, nature, img, pkmnid))

    db.commit()
    db.close()

#updating team info
def update_team(teamid, name, desc, version, weaknesses, strengths):
    db = sqlite3.connect(f)
    c = db.cursor()

    #update info
    print teamid
    print int(teamid)
    c.execute("UPDATE teams SET name = \"%s\", desc = \"%s\", version = \"%s\", weaknesses = \"%s\", strengths = \"%s\" WHERE teamid = %d;" %(name, desc, version, weaknesses, strengths, int(teamid)))

    db.commit()
    db.close()

#deleting pokemon
def delete_poke(teamid, delete_pkmn):
    db = sqlite3.connect(f)
    c = db.cursor()

    #deleting from team datatable
    c.execute("SELECT pkmnid FROM teams WHERE teamid = %d;" %(teamid))
    old_string = c.fetchone()[0]
    if old_string.endswith(str(delete_pkmn)):
        new_string = old_string.replace(str(delete_pkmn), '')
    else:
        new_string = old_string.replace(str(delete_pkmn) + ", " , '')
    c.execute("UPDATE teams SET pkmnid = \"%s\" WHERE teamid = %d;" %(new_string, teamid))
    db.commit()

    #deleting from pokemon datatable
    c.execute("DELETE FROM pokemon WHERE pkmnid = %d;" %(delete_pkmn))

    db.commit()
    db.close()

#gets top ten most upvoted teams and returns as a tuple made out of tuples
def get_ten():
    db = sqlite3.connect(f)
    c = db.cursor()

    c.execute("DELETE FROM teams WHERE name = \"\"")
    db.commit()
    
    #getting the top ten most upvoted teams
    c.execute("SELECT * FROM teams ORDER BY upvotes DESC LIMIT 10;" %())
    top_ten = c.fetchall()

    return top_ten

    db.commit()
    db.close()

def get_recent():
    db = sqlite3.connect(f)
    c = db.cursor()

    #getting the top ten most upvoted teams
    c.execute("SELECT * FROM teams ORDER BY teamid DESC LIMIT 15;" %())
    top_ten = c.fetchall()

    print "LATEST"
    print top_ten
    return top_ten

    db.commit()
    db.close()


if __name__ == "__main__":
    system("rm data/app.db")
    create_db()
#    new_team("kl", "second", "THis is great", "NONE", "NONE", "NONE", 0)
