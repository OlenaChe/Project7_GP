import requests
import json

class Wiki_info:

    def get_wiki_info(self, parsedlist):
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
        return r
    
    def response200(self, parsedlist):
        r = self.get_wiki_info(parsedlist)
        if r.status_code == 200:
            print(r.json())
        else:
            print("C'est triste")
    
    def get_wiki_extract(self, parsedlist):
        r = self.get_wiki_info(parsedlist)
        if r.status_code == 200:
            try:
                wiki_data = (r.json()['query']['pages'][list(r.json()['query']['pages'])[0]]['extract'])
                wiki_extract = "D'ailleurs, est-ce que tu sais que " + wiki_data
            except KeyError:
                wiki_extract = "Je ne sais rien par rapport à ce sujet. C'est bizarre!"
            finally:
                return wiki_extract
        else:
            wiki_extract = "Dis-moi, quel endroit tu cherches ?"
            return wiki_extract

    def get_wiki_url(self, parsedlist):
        r = self.get_wiki_info(parsedlist)
        if r.status_code == 200:
            try:
                wiki_url = (r.json()['query']['pages'][list(r.json()['query']['pages'])[0]]['fullurl'])
            except KeyError:
                wiki_url = None
            finally:
                return wiki_url
        else:
            wiki_url = None
            return wiki_url

#wiki_info = Wiki_info()
#wiki_info.response200(["Openclassrooms"])
#print(wiki_info.get.wiki_info(["%%^"]))
#print(wiki_info.get_wiki_extract([""]))
#print(wiki_info.get_wiki_url(["Openclassrooms"]))
