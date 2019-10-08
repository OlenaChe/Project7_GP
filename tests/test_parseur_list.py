# Testing the methods of parseur

# Tests for method parser_list 

def test_pl_creation_parsedlist():
    parsedlist = []
    assert parsedlist == []

def test_pl_remove_word():
    question = "Salut GrandPy ! Savez-vous l'adresse d'OpenClassrooms ?"
    no_gp = question.replace("GrandPy", "")
    assert no_gp == "Salut  ! Savez-vous l'adresse d'OpenClassrooms ?"

def test_pl_remove_dash():
    no_gp = "Salut ! Savez-vous l'adresse d'OpenClassrooms ?"
    no_dash = no_gp.replace("-", " ")
    assert no_dash == "Salut ! Savez vous l'adresse d'OpenClassrooms ?"

def test_pl_remove_article_l():
    no_dash = "Salut ! Savez vous l'adresse d'OpenClassrooms ?"
    no_l_ap = no_dash.replace("l'", "")
    assert no_l_ap == "Salut ! Savez vous adresse d'OpenClassrooms ?"

def test_pl_remove_article_d():
    no_l_ap = "Salut ! Savez vous adresse d'OpenClassrooms ?"
    no_d_ap = no_l_ap.replace("d'", "")
    assert no_d_ap == "Salut ! Savez vous adresse OpenClassrooms ?"

def test_pl_split_string_for_create_list_of_words():
    no_d_ap = "Salut ! Savez vous adresse OpenClassrooms ?"
    wordlist = no_d_ap.split()
    assert wordlist == ["Salut", "!", "Savez", "vous", "adresse", "OpenClassrooms", "?"]

def test_pl_capitalize_words_of_stoplist():
    stoplist = ["salut", "vous", "savez", "adresse"]
    stoplist_cap = [w.title() for w in stoplist]
    assert stoplist_cap == ["Salut", "Vous", "Savez", "Adresse"]

def test_pl_add_capitalized_word_in_stoplist():
    stoplist = ["salut", "vous", "savez", "adresse"]
    stoplist_cap = ["Salut", "Vous", "Savez", "Adresse"]
    for word in stoplist_cap:
        stoplist.append(word)
    assert stoplist == ["salut", "vous", "savez", "adresse", "Salut", "Vous", "Savez", "Adresse"]

def test_pl_add_punctuation_in_stoplist():
    stoplist = ["salut", "vous", "savez", "adresse", "Salut", "Vous", "Savez", "Adresse"]
    punctuation_list = ["!", "?", ",", ".", "$", "%" ]   
    for sign in punctuation_list:
        stoplist.append(sign)
    assert stoplist == ["salut", "vous", "savez", "adresse", "Salut", "Vous", "Savez", "Adresse", "!", "?", ",", ".", "$", "%"]

def test_pl_u_equal_true():
    wordlist = ["Salut", "!", "Savez", "vous", "adresse", "OpenClassrooms", "?"]
    for word in wordlist:
        u = True
    word = "Salut"
    assert u == True   

def test_pl_u_equal_false_positive():
    stoplist = ["salut", "vous", "savez", "adresse", "Salut", "Vous", "Savez", "Adresse", "!", "?", ",", ".", "$", "%"]
    word = "Salut"
    u = True 
    for stopword in stoplist: 
        if stopword == word:
            u = False
    assert u == False  

def test_pl_u_equal_false_negative():
    stoplist = ["salut", "vous", "savez", "adresse", "Salut", "Vous", "Savez", "Adresse", "!", "?", ",", ".", "$", "%"]
    word = "OpenClassrooms"
    u = True 
    for stopword in stoplist: 
        if stopword == word:
            u = False
    assert u == True 

def test_pl_add_word_in_parsedlist():
    parsedlist = []
    word = "OpenClassrooms"
    u = True
    if u == True:
        parsedlist.append(word)
    assert parsedlist == ["OpenClassrooms"]

# Tests for method parser_str

def parser_list_response(question):
    parsedlist = ["OpenClassrooms", "Paris"]
    return parsedlist

def test_parser_str1():
    parsedlist = parser_list_response("Est-ce que tu connais l'adresse d'OpenClassrooms ?")
    result = " ".join(str(x) for x in parsedlist) 
    assert result == "OpenClassrooms Paris" 