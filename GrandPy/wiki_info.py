import requests
import json

def get_wiki_info(parsedlist):
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
    return r.json()

def get_wiki_extract(parsedlist):
    wiki_extract = "Dis-moi, quel endroit tu cherches ?"
    data = get_wiki_info(parsedlist)
    try:
        wiki_data = data['query']['pages'][list(data['query']['pages'])[0]]['extract']
        wiki_extract = "D'ailleurs, est-ce que tu sais que " + wiki_data
    except KeyError:
        wiki_extract = "Je ne sais rien par rapport à ce sujet. C'est bizarre!"
    finally:
        return wiki_extract
    
def get_wiki_url(parsedlist):
    wiki_url = "https://fr.wikipedia.org/wiki/Wikip%C3%A9dia:Accueil_principal"
    data = get_wiki_info(parsedlist)
    try:
        wiki_url = (data['query']['pages'][list(data['query']['pages'])[0]]['fullurl'])
    except KeyError:
        wiki_url = "https://fr.wikipedia.org/wiki/Wikip%C3%A9dia:Accueil_principal"
    finally:
        return wiki_url
    

#print(get_wiki_info([""]))
print(get_wiki_extract([""]))
#print(get_wiki_url([""]))