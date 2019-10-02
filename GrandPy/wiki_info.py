import requests
import json

def get_wikidata(parsedlist):
     p = {"action":"query",
          "prop": "extracts",
          "format": "json",
          "explaintext": "",
          "titles": parsedlist, 
          "exsentences": 2,
          }   
     url = "http://fr.wikipedia.org/w/api.php" 
     r = requests.get(url, params = p)
     wikidata = (r.json()['query']['pages'][list(r.json()['query']['pages'])[0]]['extract'])
     return wikidata

#print(get_wikidata(["OpenClassrooms", "GrandPy"]))