from GrandPy import location

import requests

class RequestResponse:
    def json(self):
        r = {'html_attributions': [], 'results': [{'formatted_address': '7 Cité Paradis, 75010 Paris, France', 'geometry': {'location': {'lat': 48.8748465, 'lng': 2.3504873}, 'viewport': {'northeast': {'lat': 48.87622362989272, 'lng': 2.351843679892722}, 'southwest': {'lat': 48.87352397010727, 'lng': 2.349144020107278}}}, 'icon': 'https://maps.gstatic.com/mapfiles/place_api/icons/generic_business-71.png', 'id': 'dd80dc7de1802674cba35cce4e303e6862a4f3ed', 'name': 'Openclassrooms', 'opening_hours': {'open_now': False}, 'photos': [{'height': 385, 'html_attributions': ['<a href="https://maps.google.com/maps/contrib/110718279865691618892/photos">Openclassrooms</a>'], 'photo_reference': 'CmRaAAAAx8lDL9wtVR8snIpkaMu3DqJpGeKGelZxq5uIfXxlOr60teOeg3U2eyNJW-5eNbJXyU6nY3y-Mxsa1LUdtcDuXBIT_H76THsbvEKMbISIk2SVIvT9xBQ-wWf1dxnTth8KEhBQ9kAa48krjQ84uWcVgvhGGhTOPhLc_mFCf2cY_JZTFRe8p4vxTg', 'width': 385}], 'place_id': 'ChIJIZX8lhRu5kcRGwYk8Ce3Vc8', 'plus_code': {'compound_code': 'V9F2+W5 Paris', 'global_code': '8FW4V9F2+W5'}, 'rating': 3.4, 'reference': 'ChIJIZX8lhRu5kcRGwYk8Ce3Vc8', 'types': ['point_of_interest', 'establishment'], 'user_ratings_total': 23}], 'status': 'OK'}
        return r
    
def request_response(url, params):
    return RequestResponse()

def test_get_lat_for_rstatus200():
    location.requests.get = request_response
    result = location.get_latitude("OpenClassrooms")
    assert result == 48.8748465

