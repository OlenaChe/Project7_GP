 Le programme GrandPy cherche l'adresse de l'endroit que l'uttilisateur demande 
et l'indique sur la carte. De plus, GrandPy fournit une brève information sur
cet endroit et le lien sur la page pertinente de Wikipedia.

 Le programme se trouve en ligne à l'adresse 
https://project7-grandpy.herokuapp.com/

 Pour démarrer le programme l'utilisateur tape une question dans la fenêtre et 
touche un bouton "Envoyer". Le programme affiche les réponses et la carte de 
l'endroit recherché.

---Fonctionnalités--- 
Pour réaliser les fonctionnalités du programme on a créé les méthodes suivantes :
- méthode "parse" 
qui analyse une question de l'utilisateur afin de defenir l'endroit recherché.
- méthodes "get_data", "get_address", "get_latitude", "get_longitude" 
qui récupèrent les données géographiques de l'API Google Maps 
à l'aide de "requests".
- méthodes "get_wiki_info", "get_wiki_extract", "get_wiki_url" 
qui récupèrent l'information sur l'endroit de l'API Wikipedia 
à l'aide de "requests".

Pour le projet on a utilisé la méthodologie de l'AJAX. 
Front-end du site a été réaliser avec Bootstrap.
