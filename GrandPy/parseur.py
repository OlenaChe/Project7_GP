import json

from string import punctuation

def parse(question):
    """Method which parses the question of the user """
    parsedlist = []
    no_dash = question.replace("-", " ") # removed the dashes from question
    no_l_ap = no_dash.replace("l'", " ") # removed "l'"
    no_d_ap = no_l_ap.replace("d'", " ") # removed "d'"
    oc_upper = no_d_ap.replace("Openclassrooms", "OpenClassrooms")
    ocl_lower = oc_upper.replace("openclassrooms", "OpenClassrooms")
    wordlist = ocl_lower.split() # list of the words of a question   
    with open('stoplist.json') as json_file:
        stoplist = list(json.load(json_file)) # list of stopwords in lowercase  
        for sign in punctuation:
            stoplist.append(sign) # added punctuation to the stoplist    
    for word in wordlist:
        u = True
        for stopword in stoplist: 
            if stopword == word.casefold():
                u = False 
        if u:
            parsedlist.append(word) 
    parsedstr = " ".join(str(x) for x in parsedlist)   
    return parsedstr

print(parser("Salut GrandPy ! Est-ce que tu connais l'adresse de google ?"))
