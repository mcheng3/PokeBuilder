import urllib2, json, time, sys
#from flask import requests
import requests

#sys encoding things to prevent Unicode encoding errors
reload(sys)
sys.setdefaultencoding('utf-8')

def search_api(query):
    temp = requests.get("http://pokeapi.co/api/v2/"+ query, None)
    dic = temp.json()
    return dic

# Returns a dictionary of the pokemon's moves, items, abilities, etc.
def search_poke(pokemon):
    dic = search_api("pokemon/" + pokemon)
    return dic



# ============ STRENGTHS/WEAKNESSES ===============

# Returns a (formated) dictionary with the type effectiveness for the given type
def type_info(type):
    dmg_rel = search_api("type/" + type)["damage_relations"]
    for relation in dmg_rel:
        type_list = []
        for type_entry in dmg_rel[relation]:
            type_list.append( dmg_rel[relation][type_entry]["name"] )
        dmg_rel[relation] = type_tist
    return dmg_rel



# given a list of pokemon, returns a dictionary keyed by type with values equal
# to the strength of the team against that type
def get_strengths(team):
    return None

# given a list of pokemon, returns a dictionary keyed by type with values equal
# to the weakness of the team against that type
def get_weaknesses(team):
    return None

# given a list of pokemon, returns a dictionary keyed by type with values equal
# to the resistance of the team against that type
def get_resistance(team):
    return None

if __name__ == '__main__':
	print "api"
    # print search_poke("pikachu")
    # print search_api("type/ground")
