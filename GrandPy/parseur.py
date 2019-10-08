import json

from string import punctuation
"""    
def parser_list(question):
    no_dash = question.replace("-", " ") # removed the dashes from question
    no_l_ap = no_dash.replace("l'", " ") # removed "l'" 
    no_d_ap = no_l_ap.replace("d'", " ") # removed "d'"
    wordlist = no_d_ap.split() # list of the words of a question 
    wordlist_lowercase = [word.lower() for word in wordlist] # list of the words of a quetion in lowercase 
    with open('stoplist.json') as json_file: # list of stopwords in lowercase 
        stoplist = list(json.load(json_file))
        for sign in punctuation:
            stoplist.append(sign) # added punctuation to the stoplist
    parsedlist_lowercase = []  
    for word_lowercase in wordlist_lowercase:
        u = True
        for stopword in stoplist: 
            if stopword == word_lowercase:
                u = False 
        if u:
            parsedlist_lowercase.append(word_lowercase) # parsedlist in lowercase 
    
    parsedlist = []
    for word in wordlist:
        u = True
    for word_pl_lowercase in parsedlist_lowercase:
        if word.lower() != word_pl_lowercase:
            u = False
            if u:
                parsedlist.append(word)
            
                return parsedlist
"""
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
        for sign in punctuation:
            stoplist.append(sign)
    for word in wordlist:
        u = True
        for stopword in stoplist: 
            if stopword == word:
                u = False 
        for stopword in stoplist_cap:   
            if stopword == word:
                u = False
        if u:
            parsedlist.append(word)   
    return parsedlist

def parser_str(question):
    parsedlist = parser_list(question)
    parsedstr = " ".join(str(x) for x in parsedlist)   
    return parsedstr




print(parser_list("Est-ce que tu connais l'adresse d'OpenClassrooms Paris ?"))
print(parser_str("Est-ce que tu connais l'adresse d'OpenClassrooms Paris ?"))
