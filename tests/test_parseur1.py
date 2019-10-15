# Testing the method parse

from Projet7_GrandPy.GrandPy import parseur

def test_parser(question):
    question = "Salut GrandPy ! Est-ce que tu connais l'adresse d'OpenClassrooms ?"
    result = parseur.parse("Salut GrandPy ! Est-ce que tu connais l'adresse d'OpenClassrooms ?")
    assert result == "OpenClassrooms"

