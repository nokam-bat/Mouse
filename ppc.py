
# Nadia Abdi Mohamoud - SICA1a
#INI-03: IDE PYTHON - Mini projet en python
#Date de rendu: 7 octobre 2025

#Projet: Pierre, papier,ciseaux

# Message de bienvenu dans le jeu: "Bienvenue dans pierre, papier, ciseaux!", "Sauriez-vous battre l'ordinateur à ce jeu...?", peut aussi rajouter des lignes vides pour fairce jolie ou crréer un encadré.
import time

#Creer des prints qui affiche les messages
#temps de pause entre le message de bienvenue et l'entree utilisateur
print(f"------------------------------------------------")
print(f"Bienvenue dans pierre, papier, ciseaux!")
print(f"Sauras-tu battre l'ordinateur à ce jeu...?")
print(f"------------------------------------------------")
time.sleep(3)


#Fonction de choix de l'utilisateur
def choix_utilisateur():
    choix = input("Choisissez pierre, papier ou ciseaux: ").lower()
    return choix
    #Sans return, une fonction exécute son code mais ne renvoie aucune valeur (retourne None par défaut), donc pour récupérer et réutiliser une donnée (comme le choix de l’utilisateur), il faut impérativement utiliser return.
    #rajouter .lower pour tout convertir en miniscule?
#print(choix_utilisateur())


#Fonction de choix de l'ordinateur (aléatoire)- partie Noor

#Fonction de comparaison des résultats pour déterminier le vainqueur
def comparer(utilisateur, ordinateur):
    if utilisateur == ordinateur:
        return "égalité"
    elif utilisateur == "pierre" and ordinateur == "papier":
        return "ordinateur"
    elif utilisateur == "papier" and ordinateur == "ciseaux":
        return "ordinateur"
    elif utilisateur == "ciseaux" and ordinateur == "pierre":
        return "ordinateur"
    else:
        return "utilisateur"

# Fonction du jeu:
def jeu():
    utilisateur = choix_utilisateur()
    # ordinateur = choix_ordinateur()
    ordinateur = "papier"
    gagnant = comparer(utilisateur, ordinateur)
    print(f"Tu as choisis {utilisateur}, l'ordinateur a choisi {ordinateur}.")
    print (f"Le vainqueur est: {gagnant}")

    if gagnant == "utilisateur":
        print(random.choice(phrases_victoires))
    elif gagnant == "ordinateur":
        print(random.choice(phrases_defaites))
    else:
        print(random.choice(phrases_egalite))
#l’indentation de la première condition if à l’intérieur de la fonction

# affficher des commentaires lorsque l'ordi ou l'user gagne: « Bravo, tu as battu la machine ! Qui aurait cru ? » « Haha, l’ordi t’a eu cette fois. Recommence, humain ! 🤖 »
    #Créer des listes
import random 
phrases_victoires=[
"Bravo, tu as battu la machine! Qui l'aurait cru ?",
"Tu as gagné… mais je soupçonne une alliance secrète avec les ciseaux.",
"Bravo ! Tu viens de faire buguer mon ego.",
]
phrases_defaites=[
"Haha, l'ordi t'as eu cette fois. Recommence, humain !",
"Battu par une machine, c'est le début de la fin... ",
"Aïe, aïe, aïe, envisage une stratégie peut-être? ",
"Tu viens de perdre contre un script. Réfléchis à tes choix de vie."
]
phrases_egalite=[
"Même choix ? On partage le même cerveau ou juste le même manque d'inspiration ?",
"Égalité ? On dirait que nos cerveaux sont synchronisés… enfin, le tien et mes lignes de code.",
"C'est beau l'harmonie… mais j'étais prêt à gagner."
]

#Trouver une solution qui évite que la même phrase se répète....?

#Tirage aléatoire:
random.choice(phrases_defaites)
# et pareil pour les autres...

#Fonction pour le score

#Une boucle qui arrête le jeu après 3 manches et affiche le score final
# --> la boucle a un compteur de manche qui arrête le jeu après être arrivé à 3.

#jeu ()
#jeu() — c’est quoi ?
#jeu() est le nom d’une fonction que tu as écrite dans ton programme.
#Une fonction, c’est un petit bloc de code que tu peux réutiliser et exécuter quand tu veux, en l’appelant par son nom.
#Que fait jeu() ?
#Quand tu écris jeu() (avec les parenthèses) dans ton code, tu dis à l’ordinateur : « Hé, lance cette fonction appelée jeu ! »
#L’ordinateur va alors exécuter tout le code à l’intérieur de la fonction jeu() : par exemple, demander ton choix, faire jouer l’ordinateur, comparer les résultats, afficher qui a gagné, etc.
#Pourquoi écrire jeu() ?
#Parce que ta fonction jeu() contient tout ce qu’il faut pour faire fonctionner une partie de pierre-papier-ciseaux.
#Au lieu d’écrire tout le code à chaque fois, tu écris juste jeu() pour lancer une partie.

#jeu() = « Lance le jeu ! »

# Et coment quitter, arrêter de jouer?
#-->voir la partei de Noor



jeu()