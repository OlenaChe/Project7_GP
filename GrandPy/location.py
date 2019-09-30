import requests
import json

from google_key import *

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
def get_id(query):
    search_payload = {"key":GOOGLE_KEY, "query":query}
    search_url = "https://maps.googleapis.com/maps/api/place/textsearch/json"
    search_req = requests.get(search_url, params=search_payload)
    search_json = search_req.json()
    place_id = search_json["results"][0]["place_id"]
    return place_id
    
#print(get_id(["OpenClassrooms", "Grandpy"]))
"""