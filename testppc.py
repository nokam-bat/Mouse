
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


import time
def choix_utilisateur():
    choix = input("Choisissez pierre, papier ou ciseaux: ")
    return choix

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

def jeu():

    print(f"------------------------------------------------")
    print(f"Bienvenue dans pierre, papier, ciseaux!")
    print(f"Saurais-tu battre l'ordinateur à ce jeu...?")
    print(f"------------------------------------------------")
    time.sleep(3)

    utilisateur = choix_utilisateur()
    ordinateur = "papier"
    gagnant = comparer(utilisateur, ordinateur)
    print(f"Tu as choisis {utilisateur}, l'ordinateur a choisi {ordinateur}.")
    print(f"Le vainqueur est: {gagnant}")

    if gagnant == "utilisateur":
        print(random.choice(phrases_victoires))
    elif gagnant == "ordinateur":
        print(random.choice(phrases_defaites))
    else:
        print(random.choice(phrases_egalite))

jeu()