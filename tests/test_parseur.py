# Testing the method parse

from Projet7_GrandPy.GrandPy import parseur

def test_parser_phrase1():
    """Methode tests the parsing of the question of a user"""
    result = parseur.parse("Salut GrandPy ! Est-ce que tu connais"
    " l'adresse d'OpenClassrooms ?")
    assert result == "OpenClassrooms"

def test_parser_phrase2():
    """Methode tests the parsing of the question of a user"""
    result = parseur.parse("Je cherche l'adresse d'OpenClassrooms,"
    " peux-tu m'aider ?")
    assert result == "OpenClassrooms"

def test_parser_phrase3():
    """Methode tests the parsing of the question of a user"""
    result = parseur.parse("OpenClassrooms se trouve où ?")
    assert result == "OpenClassrooms"
