from GrandPy import wiki_info

import requests

class RequestResponse:
    def json(self):
        r ={ 
            'batchcomplete':'',
            'warnings':{ 
                'extracts':{ 
                    '*':'"exlimit" was too large for a whole article extracts request, lowered to 1.'
                }
            },
            'query':{ 
                'pages':{ 
                    '4338589':{ 
                        'pageid':4338589,
                        'ns':0,
                        'title':'OpenClassrooms',
                        'contentmodel':'wikitext',
                        'pagelanguage':'fr',
                        'pagelanguagehtmlcode':'fr',
                        'pagelanguagedir':'ltr',
                        'touched':'2019-10-03T16:15:59Z',
                        'lastrevid':160299000,
                        'length':31087,
                        'fullurl':'https://fr.wikipedia.org/wiki/OpenClassrooms',
                        'editurl':'https://fr.wikipedia.org/w/index.php?title=OpenClassrooms&action=edit',
                        'canonicalurl':'https://fr.wikipedia.org/wiki/OpenClassrooms',
                        'extract':'OpenClassrooms est une école en ligne qui propose à ses membres des cours certifiants et des parcours débouchant sur un métier d\'avenir, réalisés en interne, par des écoles, des universités, ou encore par des entreprises partenaires comme Microsoft ou IBM. Jusqu\'en 2018, n\'importe quel membre du site pouvait être auteur, via un outil nommé "Course Lab". De nombreux cours sont issus de la communauté, mais ne sont plus mis en avant.'
                    }
                }
            }
        }
        return r

def request_response(url, params):
    return RequestResponse()

def test_wiki_url():
    wiki_info.requests.get = request_response
    result = wiki_info.get_wiki_url("OpenClassrooms")
    assert result == "https://fr.wikipedia.org/wiki/OpenClassrooms"

# --- Response Error ---

class RequestResponseError:
    def json(self):   
        r = {'batchcomplete': ''}
        return r
    
def request_response_error(url, params):
    return RequestResponseError()

def test_wiki_url_error():
    wiki_info.requests.get = request_response_error
    result = wiki_info.get_wiki_url("OpenClassrooms")
    assert result == "https://fr.wikipedia.org/wiki/Wikip%C3%A9dia:Accueil_principal"