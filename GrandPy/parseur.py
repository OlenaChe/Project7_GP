from flask import Flask
import json

from string import punctuation

class Parseur():
    
    def parser_list(self, question):
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

    def parser_str(self, question):
        parsedlist = self.parser_list(question)
        parsedstr = " ".join(str(x) for x in parsedlist)   
        return parsedstr

#data = Parseur()
#print(data.parser_list("Salut GrandPy ! Est-ce que tu connais l'adresse d'openclassrooms ?"))
#print(data.parser_str("Salut GrandPy ! Est-ce que tu connais l'adresse d'OpenClassrooms ?"))
