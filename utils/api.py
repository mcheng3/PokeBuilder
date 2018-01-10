import urllib2, json, time, sys
from flask import request

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

if __name__ == '__main__':
    print search_poke("pikachu")
