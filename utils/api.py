import urllib2, json, time, sys

#sys encoding things to prevent Unicode encoding errors
reload(sys)
sys.setdefaultencoding('utf-8')

# CURRENTLY NOT WORKING
def search_poke(query):
    temp = urllib2.Request("http://pokeapi.co/api/v2/pokemon/" + query)
    print temp
    u = urllib2.urlopen(temp)
    s = u.read()
    dic = json.loads(s)
    print dic
    
if __name__ == '__main__':
    search_poke("pikachu")
