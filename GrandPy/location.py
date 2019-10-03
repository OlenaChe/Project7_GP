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
        p = {"key":"API_KEY", "query":query}
        url = "https://maps.googleapis.com/maps/api/place/textsearch/json"
        r_data = requests.get(url, params = p).json()
        return r_data

    def get_address(self, query):
        r_data = self.get_data(query)
        address = r_data["results"][0]["formatted_address"]
        return address 
    
    def get_latitude(self, query):
        r_data = self.get_data(query)
        latitude = r_data["results"][0]["geometry"]["location"]["lat"]
        return latitude

    def get_longitude(self, query):
        r_data = self.get_data(query)
        longitude = r_data["results"][0]["geometry"]["location"]["lng"]
        return longitude

#data = Location()
#print(data.get_data(["OpenClassrooms", "Grandpy"]))
#print(data.get_address(["OpenClassrooms", "Grandpy"]))
#print(data.get_latitude(["OpenClassrooms", "Grandpy"]))
#print(data.get_longitude(["OpenClassrooms", "Grandpy"]))



