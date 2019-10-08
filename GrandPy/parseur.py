import json

from string import punctuation

def parser_list(question):
    parsedlist = []
    no_gp = question.replace("GrandPy", "")
    no_dash = no_gp.replace("-", " ")
    no_l_ap = no_dash.replace("l'", " ")
    no_d_ap = no_l_ap.replace("d'", " ") 
    wordlist = no_d_ap.split()
    with open('stoplist.json') as json_file:
        stoplist = list(json.load(json_file))
        stoplist_cap = [w.title() for w in stoplist]
        for word in stoplist_cap:
            stoplist.append(word)
        for sign in punctuation:
            stoplist.append(sign)     
    for word in wordlist:
        u = True
        for stopword in stoplist: 
            if stopword == word:
                u = False 
        if u:
            parsedlist.append(word)   
    return parsedlist

def parser_str(question):
    parsedlist = parser_list(question)
    parsedstr = " ".join(str(x) for x in parsedlist)   
    return parsedstr

#print(parser_list("Salut GrandPy ! Est-ce que tu connais l'adresse d'OpenClassrooms Paris ?"))
#print(parser_str("Salut GrandPy ! Est-ce que tu connais l'adresse d'OpenClassrooms Paris ?"))
