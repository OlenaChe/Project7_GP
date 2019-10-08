from GrandPy import parseur

import json

from string import punctuation

def parser_list_response(question):
    parsedlist = ["OpenClassrooms", "Sorbonne"]
    return parsedlist

def test_parser_str1():
    parsedlist = parser_list_response("Est-ce que tu connais l'adresse d'OpenClassrooms ?")
    result = " ".join(str(x) for x in parsedlist) 
    assert result == "OpenClassrooms Sorbonne"