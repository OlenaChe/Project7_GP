"""Methods which get the data from the Google Maps API"""

import requests

from .key import GOOGLE_KEY
#print(GOOGLE_KEY)

# import os
# API_KEY = str(os.getenv('API_KEY'))

def get_data(query):
    """Method which gets the data concerned with the 'query' from the Google
    Maps API """
    par = {"key":str(GOOGLE_KEY), "query":query}
    url = "https://maps.googleapis.com/maps/api/place/textsearch/json"
    req = requests.get(url, params=par)
    return req.json()

def get_address(query):
    """Method which gets an address of the place concerned with the 'query'
    from from the Google Maps API"""
    address = "Dis-moi, quel endroit tu cherches ?"
    data = get_data(query)
    try:
        address_data = data["results"][0]["formatted_address"]
        address = "Si je ne me trompe pas, l'adresse que tu cherche, c'est ... "\
        + address_data + ". Sinon, dis-moi le nom de lieu exact"
    except IndexError:
        address = "Désolé, je n'ai pas compris quel endroit tu cherches ?"
    finally:
        return address

def get_latitude(query):
    """Method which gets a latitude of the place concerned with the 'query'
    from from the Google Maps API"""
    data = get_data(query)
    latitude = 48.856614
    try:
        latitude = data["results"][0]["geometry"]["location"]["lat"]
    except IndexError:
        latitude = 48.856614
    finally:
        return latitude

def get_longitude(query):
    """Method which gets a longitude of the place concerned with the 'query'
    from from the Google Maps API"""
    data = get_data(query)
    longitude = 2.3504873
    try:
        longitude = (
            data.get_data(query)["results"][0]["geometry"]["location"]["lng"])
    except IndexError:
        longitude = 2.3504873
    finally:
        return longitude

#print(get_data("OpenClassrooms"))
#print(get_address("OpenClassrooms"))
#print(get_latitude("OpenClassrooms"))
#print(get_longitude("OpenClassrooms"))
