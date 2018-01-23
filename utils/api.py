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
'''
The final goal is to get a dictionary for the team formated as such:
{
    normal: 1
    fighting: 2
    flying: 0
    poison: -3
    ground: 1
    rock: 0
    bug: 0
    ghost: 0
    steel: 0
    fire: 0
    water: 0
    grass: 0
    electric: 0
    psychic: 0
    ice: 0
    dragon: 0
    dark: 0
}
'''



# Returns a (formated) dictionary with the type effectiveness for the given type
def type_info(type):
    dmg_rel = search_api("type/" + type)["damage_relations"]
    for relation in dmg_rel:
        type_list = []
        for type_entry in dmg_rel[relation]:
            type_list.append( dmg_rel[relation][type_entry]["name"] )
        dmg_rel[relation] = type_tist
    return dmg_rel

# Adds the damage relationships for the individual type to the overall dictionary
# for the team. Must also pass offensive/deffensive
def add_dmg_rel(dmg_rel_dic, type, relationship):
    ind_dmg_rel = type_info(type)
    for relation in ind_dmg_rel:
        if relationship == "offensive":
            f
    return dmg_rel_dic


# given a list of pokemon, returns a dictionary keyed by type with values equal
# to the offense of the team against that type
def get_offensive(team):
    return None

# given a list of pokemon, returns a dictionary keyed by type with values equal
# to the deffense of the team against that type
def get_deffensive(team):
    return None


if __name__ == '__main__':
	print "api"
    # print search_poke("pikachu")
    # print search_api("type/ground")
