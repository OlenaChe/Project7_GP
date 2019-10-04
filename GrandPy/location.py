import requests
import json

#from .google_key import *

"""
def get_latitude(query):
    p = {"key":GOOGLE_KEY, "query":query}
    url = "https://maps.googleapis.com/maps/api/place/textsearch/json"
    r = requests.get(url, params = p)
    r_json = r.json()
    lat = r_json["results"][0]["geometry"]["location"]["lat"]
    return lat

#print(get_latitude(["OpenClassrooms", "Grandpy"]))

def get_longitude(query):
    p = {"key":GOOGLE_KEY, "query":query}
    url = "https://maps.googleapis.com/maps/api/place/textsearch/json"
    r = requests.get(url, params = p)
    r_json = r.json()
    lng = r_json["results"][0]["geometry"]["location"]["lng"]
    return lng

#print(get_longitude(["OpenClassrooms", "Grandpy"]))

def get_address(query):
    p = {"key":GOOGLE_KEY, "query":query}
    url = "https://maps.googleapis.com/maps/api/place/textsearch/json"
    r = requests.get(url, params = p)
    r_json = r.json()
    address = r_json["results"][0]["formatted_address"]
    return address

#print(get_address(["OpenClassrooms", "Grandpy"]))
"""

class Location:

    def get_data(self, query):
        p = {"key":"AIzaSyD1YKYO73lEKwBEShSb7Fty-37CC2pAJKs", "query":query}
        url = "https://maps.googleapis.com/maps/api/place/textsearch/json"
        r = requests.get(url, params = p)
        return r
        

    def get_address(self, query):
        r = self.get_data(query)
        address = "Dis-moi, quel endroit tu cherches ?"
        if r.status_code == 200:
            try:
                address_data = r.json()["results"][0]["formatted_address"]
                address = "Si je ne me trompe pas, l'adresse que tu cherche, c'est ... " + address_data + " Sinon, dis-moi le nom de lieu exact"
            except IndexError:
                address = "Désolé, je n'ai pas compris. Quel endroit tu cherches ?"
            finally:
                return address   
    
    def get_latitude(self, query):
        r = self.get_data(query)
        latitude = 48.8748465
        if r.status_code == 200:
            try:
                latitude = self.get_data(query)["results"][0]["geometry"]["location"]["lat"]
            except IndexError:
                latitude = 48.8748465
            finally:
                return latitude 
    
    def get_longitude(self, query):
        r = self.get_data(query)
        longitude = 2.3504873
        if r.status_code == 200:
            try:
                longitude = self.get_data(query)["results"][0]["geometry"]["location"]["lng"]
            except IndexError:
                longitude = 2.3504873
            finally:
                return longitude

#data = Location()
#print(data.get_data(["GrandPy", "OpenClassrooms"]))
#print(data.get_address(["GrandPy", "OpenClassrooms"]))
#print(data.get_latitude(["Grandpy"]))
#print(data.get_longitude(["Grandpy"]))



