import requests
import json

def get_data(parsedlist):
     p = {"action":"query",
          "prop": "extracts",
          "format": "json",
          "explaintext": "",
          "titles": parsedlist, 
          "exsentences": 2,
          }   
     url = "http://fr.wikipedia.org/w/api.php" 
     r = requests.get(url, params = p)
     wiki_response = (r.json()['query']['pages'][list(r.json()['query']['pages'])[0]]['extract'])
     return wiki_response
     #return r.json()

#print(get_data(["OpenClassrooms", "GrandPy"]))