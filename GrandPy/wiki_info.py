import requests
import json

def get_wiki_url(parsedlist):
     p = {"action":"query",
          "prop": "info|extracts",
          "inprop": "url",
          "format": "json",
          "explaintext": "",
          "titles": parsedlist, 
          "exsentences": 2,
          }   
     url = "http://fr.wikipedia.org/w/api.php" 
     r = requests.get(url, params = p)
     wiki_url = (r.json()['query']['pages'][list(r.json()['query']['pages'])[0]]['fullurl'])
     return wiki_url

#print(get_wiki_url(["OpenClassrooms"]))

def get_wiki_extract(parsedlist):
     p = {"action":"query",
          "prop": "extracts",
          "format": "json",
          "explaintext": "",
          "titles": parsedlist, 
          "exsentences": 2,
          }   
     url = "http://fr.wikipedia.org/w/api.php" 
     r = requests.get(url, params = p)
     wiki_extract = (r.json()['query']['pages'][list(r.json()['query']['pages'])[0]]['extract'])
     return wiki_extract

#print(get_wiki_extract(["OpenClassrooms"]))
