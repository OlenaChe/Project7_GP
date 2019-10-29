"""Testing the methods get_address, get_latitude, get_longitude"""
import requests

from Projet7_GrandPy.GrandPy import location


class RequestResponse:
    """Class defines the request response of the Google Maps API (200 OK)"""
    def json(self):
        """Method which returns the data in json format"""
        req = {
            'html_attributions': [
            ],
            'results': [
                {
                    'formatted_address': '7 Cité Paradis, 75010 Paris, France',
                    'geometry': {
                        'location': {
                            'lat': 48.8748465,
                            'lng': 2.3504873
                        },
                        'viewport': {
                            'northeast': {
                                'lat': 48.87622362989272,
                                'lng': 2.351843679892722
                            },
                            'southwest': {
                                'lat': 48.87352397010727,
                                'lng': 2.349144020107278
                            }
                        }
                    },
                    'icon': 'https://maps.gstatic.com/mapfiles/place_api/ico\
                        ns/generic_business-71.png',
                    'id': 'dd80dc7de1802674cba35cce4e303e6862a4f3ed',
                    'name': 'Openclassrooms',
                    'opening_hours': {
                        'open_now': False
                    },
                    'photos': [
                        {
                            'height': 385,
                            'html_attributions': [
                                '<a href="https://maps.google.com/maps/contri\
                                    b/110718279865691618892/photos">Openclass\
                                        rooms</a>'
                            ],
                            'photo_reference':'CmRaAAAA9cvg0yNhM_kNcdZGgDc3SsD\
                                Um-RX27BB4huye0bknEQIP95O4aGaGdvqyfQkatdESXTS1\
                                    X0lz0mxK7xc9lOh7DaazwoJdd6tJ_IclywwuNOlHgy\
                                        jpiQmqWo08H8rUaClEhBmN4GagHkXvy5xYB8IY\
                                            e7YGhTzVtQ2lRQztSqjB4GdfLpGJi0f9w',
                            'width': 385
                        }
                    ],
                    'place_id': 'ChIJIZX8lhRu5kcRGwYk8Ce3Vc8',
                    'plus_code': {
                        'compound_code': 'V9F2+W5 Paris',
                        'global_code': '8FW4V9F2+W5'
                    },
                    'rating': 3.4,
                    'reference': 'ChIJIZX8lhRu5kcRGwYk8Ce3Vc8',
                    'types': [
                        'point_of_interest',
                        'establishment'
                    ],
                    'user_ratings_total':23
                }
            ],
            'status': 'OK'
        }
        return req


def request_response(url, params):
    """Method which mocks a response from the Google Maps API"""
    return RequestResponse()


class RequestResponseError:
    """Class defines the request response of the Google Maps API (!= 200 OK)"""
    def json(self):
        """Method which returns the data json conteining an error message"""
        req = {
            'error_message': 'You must use an API key to authenticate each \
             request to Google Maps Platform APIs. For additional information,\
             please refer to http://g.co/dev/maps-no-account',
            'html_attributions': [
            ],
            'results': [
            ],
            'status': 'REQUEST_DENIED'
            }
        return req


def request_response_error(url, params):
    """Method which mocks a response with an error message
    from the Google Maps API"""
    return RequestResponseError()


# ---Testing location.get_address

"""
def test_get_address():
    location.requests.get = request_response  # Response without Errors
    result = location.get_address("OpenClassrooms")
    assert result == ("Si je ne me trompe pas, l'adresse que tu cherche,"
    " c'est ... 7 Cité Paradis, 75010 Paris, France."
    " Sinon, dis-moi le nom de lieu exact")
"""

def test_get_address(monkeypatch):
    """Methode tests getting the address from the json data"""
    monkeypatch.setattr(requests, "get", request_response)  # Response without Errors
    result = location.get_address("OpenClassrooms")
    assert result == ("Si je ne me trompe pas, l'adresse que tu cherche,"
    " c'est ... 7 Cité Paradis, 75010 Paris, France."
    " Sinon, dis-moi le nom de lieu exact")

"""
def test_get_address_error():
    location.requests.get = request_response_error  # Response with an Error
    result = location.get_address("OpenClassrooms")
    assert result == "Désolé, je n'ai pas compris quel endroit tu cherches ?"
"""

def test_get_address_error(monkeypatch):
    """Methode tests the request of the address of the place from the json data
    which contains an error"""
    monkeypatch.setattr(requests, "get", request_response_error)  # Response with an Error
    result = location.get_address("OpenClassrooms")
    assert result == "Désolé, je n'ai pas compris quel endroit tu cherches ?"


# ---Testing location.get_latitude

"""
def test_get_lat():
    location.requests.get = request_response  # Response without Errors
    result = location.get_latitude("OpenClassrooms")
    assert result == 48.8748465
"""

def test_get_lat(monkeypatch):
    """Methode tests getting a latitude of the place from the json data"""
    monkeypatch.setattr(requests, "get", request_response)  # Response without Errors
    result = location.get_latitude("OpenClassrooms")
    assert result == 48.8748465

"""
def test_get_lat_error():
    location.requests.get = request_response_error  # Response with an Error
    result = location.get_latitude("OpenClassrooms")
    assert result == 48.856614
"""

def test_get_lat_error(monkeypatch):
    """Methode tests the request of a latitude of the place from the json data
    which contains an error"""
    monkeypatch.setattr(requests, "get", request_response_error)  # Response with an Error
    result = location.get_latitude("OpenClassrooms")
    assert result == 48.856614


# ---Testing location.get_longitude

"""
def test_get_lng():
    location.requests.get = request_response  # Response without Errors
    result = location.get_longitude("OpenClassrooms")
    assert result == 2.3504873
"""

def test_get_lng(monkeypatch):
    """Methode tests getting a longitude of the place from the json data"""
    monkeypatch.setattr(requests, "get", request_response)  # Response without Errors
    result = location.get_longitude("OpenClassrooms")
    assert result == 2.3504873

"""
def test_get_lng_error():
    location.requests.get = request_response_error  # Response with an Error
    result = location.get_longitude("OpenClassrooms")
    assert result == 2.3504873
"""

def test_get_lng_error(monkeypatch):
    """Methode tests the request of a longitude of the place from the json data
    which contains an error"""
    monkeypatch.setattr(requests, "get", request_response_error)  # Response with an Error
    result = location.get_longitude("OpenClassrooms")
    assert result == 2.3504873