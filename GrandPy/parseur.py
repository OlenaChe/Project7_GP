"""Method which parses the question of the user for get a short query """

import json

from string import punctuation


def parse(question):
    """Method which parses the question of the user"""
    parsedlist = []
    i = 1
    for symbol in question:
        if symbol in punctuation:
            question = question.replace(symbol, " ")
            i = +1
    question = question.replace("Openclassrooms", "OpenClassrooms")
    question = question.replace("openclassrooms", "OpenClassrooms")
    wordlist = question.split()  # list of the words of a question
    with open('stoplist.json') as json_file:
        stoplist = list(json.load(json_file))  # list of stopwords in lowercase
    for word in wordlist:
        if len(word) > 3:
            include_in_parsedlist = True
        for stopword in stoplist:
            if stopword == word.casefold():
                include_in_parsedlist = False
        if include_in_parsedlist:
            parsedlist.append(word)
    parsedstr = " ".join(str(x) for x in parsedlist)
    return parsedstr


# print(parse("Peut-tu m'indiquer où se trouve l'OpenClassrooms?"))
