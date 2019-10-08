import requests
import json

#import os
#GOOGLE_KEY = str(os.getenv('API_KEY'))

def get_data(query):
    p = {"key":"", "query":query}
    url = "https://maps.googleapis.com/maps/api/place/textsearch/json"
    r = requests.get(url, params = p)
    return r.json()
        
def get_address(query):
    address = "Dis-moi, quel endroit tu cherches ?"
    data = get_data(query)
    try:
        address_data = data["results"][0]["formatted_address"]
        address = "Si je ne me trompe pas, l'adresse que tu cherche, c'est ... " + address_data + ". Sinon, dis-moi le nom de lieu exact"
    except IndexError:
        address = "Désolé, je n'ai pas compris. Quel endroit tu cherches ?"
    finally:
        return address  

def get_latitude(query):
    data = get_data(query)
    latitude = 48.856614
    try:
        latitude = data["results"][0]["geometry"]["location"]["lat"]
    except IndexError:
        latitude = 48.856614
    finally:
        return latitude 
    
def get_longitude(query):
    data = get_data(query)
    longitude = 2.3504873
    try:
        longitude = data.get_data(query)["results"][0]["geometry"]["location"]["lng"]
    except IndexError:
        longitude = 2.3504873
    finally:
        return longitude

print(get_data("Openclassrooms"))
print(get_address("Openclassrooms"))
#print(get_latitude("Paris"))
#print(get_longitude("Paris"))
#print(get_longitude("OpenClassrooms"))

