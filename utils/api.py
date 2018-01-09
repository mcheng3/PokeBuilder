import urllib2, json, time, sys, requests

#sys encoding things to prevent Unicode encoding errors
reload(sys)
sys.setdefaultencoding('utf-8')

# CURRENTLY NOT WORKING
def search_poke(query):
    temp = requests.get("http://pokeapi.co/api/v2/pokemon/"+ query, None)
    dic = temp.json()
    print dic
    
if __name__ == '__main__':
    search_poke("pikachu")
