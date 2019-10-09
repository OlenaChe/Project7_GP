# Testing the methods of parseur

# Tests for method parser

def test_pl_creation_parsedlist():
    parsedlist = []
    assert parsedlist == []

def test_pl_remove_dash():
    question = "Salut GrandPy ! Savez-vous l'adresse d'openclassrooms ?"
    no_dash = question.replace("-", " ")
    assert no_dash == "Salut GrandPy ! Savez vous l'adresse d'openclassrooms ?"

def test_pl_remove_article_l():
    no_dash = "Salut GrandPy ! Savez vous l'adresse d'openclassrooms ?"
    no_l_ap = no_dash.replace("l'", "")
    assert no_l_ap == "Salut GrandPy ! Savez vous adresse d'openclassrooms ?"

def test_pl_remove_article_d():
    no_l_ap = "Salut GrandPy ! Savez vous adresse d'openclassrooms ?"
    no_d_ap = no_l_ap.replace("d'", "")
    assert no_d_ap == "Salut GrandPy ! Savez vous adresse openclassrooms ?"

def test_pl_change_letter_at_the_beginning():
    no_d_ap = "Salut GrandPy ! Savez vous adresse openclassrooms ?"
    oc_b = no_d_ap.replace("openclassrooms", "Openclassrooms")
    assert oc_b == "Salut GrandPy ! Savez vous adresse Openclassrooms ?"

def test_pl_change_letter_in_the_middle():
    oc_b = "Salut GrandPy ! Savez vous adresse Openclassrooms ?"
    oc_m = oc_b.replace("Openclassrooms", "OpenClassrooms")
    assert oc_m == "Salut GrandPy ! Savez vous adresse OpenClassrooms ?"

def test_pl_split_string_for_create_list_of_words():
    oc_m = "Salut GrandPy ! Savez vous adresse OpenClassrooms ?"
    wordlist = oc_m.split()
    assert wordlist == ["Salut", "GrandPy", "!", "Savez", "vous", "adresse", "OpenClassrooms", "?"]

def test_pl_add_punctuation_in_stoplist():
    stoplist = ["salut", "grandpy", "vous", "savez", "adresse"]
    punctuation_list = ["!", "?", ",", ".", "$", "%" ]   
    for sign in punctuation_list:
        stoplist.append(sign)
    assert stoplist == ["salut", "grandpy", "vous", "savez", "adresse", "!", "?", ",", ".", "$", "%"]

def test_pl_u_equal_true():
    wordlist = ["Salut", "GrandPy", "!", "Savez", "vous", "adresse", "OpenClassrooms", "?"]
    for word in wordlist:
        u = True
    word
    assert u == True   

def test_pl_casefold():
    word = "GrandPy"
    word_cf = word.casefold()
    assert word_cf == "grandpy"

def word_casefold_grandpy():
    return "grandpy"

def test_pl_stopwords_u_equal_false():
    stopword = "grandpy"
    u = True
    if stopword == word_casefold_grandpy():
        u = False
    u
    assert u == False 
    
def word_casefold_openclassrooms():
    return "openclassrooms"

def test_pl_stopword_u_equal_true():
    stopword = "salut"
    u = True 
    if stopword == word_casefold_openclassrooms():
        u = False
    u
    assert u == True 

def test_pl_add_word_in_parsedlist():
    parsedlist = []
    word = "OpenClassrooms"
    u = True
    if u == True:
        parsedlist.append(word)
    assert parsedlist == ["OpenClassrooms"]

def test_append_a_word():
    parsedlist = []
    word = "OpenClassrooms"
    u = True
    if u:
        parsedlist.append(word) 
    assert parsedlist == ["OpenClassrooms"]

def test_pl_str():
    parsedlist = ["OpenClassrooms"]
    result = " ".join(str(x) for x in parsedlist) 
    assert result == "OpenClassrooms" 