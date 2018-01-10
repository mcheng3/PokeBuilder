import csv
import api

d = api.search_api("pokemon/?limit=1000")
f = open("pokemon", "w")
for key in d["results"]:
    f.write('"' + key["name"] +'", ')