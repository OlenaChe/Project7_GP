# Testing the methods get_wiki_extract, get_wiki_url

import requests

from Projet7_GrandPy.GrandPy import wiki_info


class RequestResponse:
    """Class defines the response of the Wikipedia API (200 OK)"""
    def json(self):
        """Method which returns the data in json format"""
        r = {
            'batchcomplete': '',
            'warnings': {
                'extracts': {
                    '*': ('"exlimit" was too large for a whole article'
                    ' extracts request, lowered to 1.')
                }
            },
            'query': {
                'pages': {
                    '4338589': {
                        'pageid': 4338589,
                        'ns': 0,
                        'title': 'OpenClassrooms',
                        'contentmodel': 'wikitext',
                        'pagelanguage': 'fr',
                        'pagelanguagehtmlcode': 'fr',
                        'pagelanguagedir': 'ltr',
                        'touched': '2019-10-03T16:15:59Z',
                        'lastrevid': 160299000,
                        'length': 31087,
                        'fullurl': \
                            'https://fr.wikipedia.org/wiki/OpenClassrooms',
                        'editurl': \
                            'https://fr.wikipedia.org/w/index.php?title=Open\
                                Classrooms&action=edit',
                        'canonicalurl': \
                            'https://fr.wikipedia.org/wiki/OpenClassrooms',
                        'extract': ('OpenClassrooms est une école en ligne qui'
                        ' propose à ses membres des cours certifiants et des'
                        ' parcours débouchant sur un métier d\'avenir,'
                        ' réalisés en interne, par des écoles, des'
                        ' universités, ou encore par des entreprises'
                        ' partenaires comme Microsoft ou IBM. Jusqu\'en 2018,'
                        ' n\'importe quel membre du site pouvait être auteur,'
                        ' via un outil nommé "Course Lab". De nombreux cours'
                        ' sont issus de la communauté, mais ne sont plus mis'
                        ' en avant.')
                    }
                }
            }
        }
        return r


def request_response(url, params):
    """Method which mocks a response from the Wikipedia API"""
    return RequestResponse()


class RequestResponseError:
    """Class defines the response of the Wikipedia API (!= 200 OK)"""
    def json(self):
        """Method which returns the data json 
        which doesn't contein requested information"""
        r = {'batchcomplete': ''}
        return r


def request_response_error(url, params):
    """Method which mocks a response 
    which doesn't contein requested information"""
    return RequestResponseError()


# ---Testing wiki_info.get_wiki_url

"""
def test_wiki_url():
    wiki_info.requests.get = request_response  # Response without Errors
    result = wiki_info.get_wiki_url("OpenClassrooms")
    assert result == "https://fr.wikipedia.org/wiki/OpenClassrooms"
"""

def test_wiki_url(monkeypatch):
    monkeypatch.setattr(requests, "get", request_response)
    result = wiki_info.get_wiki_url("OpenClassrooms")
    assert result == "https://fr.wikipedia.org/wiki/OpenClassrooms"

"""
def test_wiki_url_error():
    wiki_info.requests.get = request_response_error  # Response with an Error
    result = wiki_info.get_wiki_url("OpenClassrooms")
    assert result == \
        "https://fr.wikipedia.org/wiki/Wikip%C3%A9dia:Accueil_principal"
"""

def test_wiki_url_error(monkeypatch):
    """Methode tests the request of the url of the corresponding page 
    of the wikipedi from the json data which contains an error"""
    monkeypatch.setattr(requests, "get", request_response_error)  # Response with an Error
    result = wiki_info.get_wiki_url("OpenClassrooms")
    assert result == \
        "https://fr.wikipedia.org/wiki/Wikip%C3%A9dia:Accueil_principal"


# ---Testing wiki_info.get_wiki_extract

"""
def test_wiki_extract():
    wiki_info.requests.get = request_response  # Response without Errors
    result = wiki_info.get_wiki_extract("OpenClassrooms")
    assert result == ('''D'ailleurs, est-ce que tu sais que OpenClassrooms'''
    ''' est une école en ligne qui propose à ses membres des cours'''
    ''' certifiants et des parcours débouchant sur un métier d'avenir,'''
    ''' réalisés en interne, par des écoles, des universités, ou encore par'''
    ''' des entreprises partenaires comme Microsoft ou IBM. Jusqu'en 2018,'''
    ''' n'importe quel membre du site pouvait être auteur, via un outil'''
    ''' nommé "Course Lab". De nombreux cours sont issus de la communauté,'''
    ''' mais ne sont plus mis en avant.''')
"""

def test_wiki_extract(monkeypatch):
    """Methode tests getting the info from the corresponding page 
    of the wikipedia from the json data"""
    monkeypatch.setattr(requests, "get", request_response)  # Response without Errors
    result = wiki_info.get_wiki_extract("OpenClassrooms")
    assert result == ('''D'ailleurs, est-ce que tu sais que OpenClassrooms'''
    ''' est une école en ligne qui propose à ses membres des cours'''
    ''' certifiants et des parcours débouchant sur un métier d'avenir,'''
    ''' réalisés en interne, par des écoles, des universités, ou encore par'''
    ''' des entreprises partenaires comme Microsoft ou IBM. Jusqu'en 2018,'''
    ''' n'importe quel membre du site pouvait être auteur, via un outil'''
    ''' nommé "Course Lab". De nombreux cours sont issus de la communauté,'''
    ''' mais ne sont plus mis en avant.''')

"""
def test_wiki_extract_error():
    wiki_info.requests.get = request_response_error  # Response with an Error
    result = wiki_info.get_wiki_extract("OpenClassrooms")
    assert result == "Je ne sais rien par rapport à ce sujet. C'est bizarre!"
"""

def test_wiki_extract_error(monkeypatch):
    """Methode tests the request of the info from the corresponding page
    of the wikipedia from the json data which contains an error"""
    monkeypatch.setattr(requests, "get", request_response_error)  # Response with an Error
    result = wiki_info.get_wiki_extract("OpenClassrooms")
    assert result == "Je ne sais rien par rapport à ce sujet. C'est bizarre!"
