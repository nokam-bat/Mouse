
import random
import time

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

choices = {
    "c" : "Caillou",
    "f" : "Feuille",
    "s" : "Ciseaux",
    "q" : "Quitter"
}

def get_choix_utilisateur():
    print("Faites votre choix: ")
    print("  c pour Caillou")
    print("  f pour Feuille")
    print("  s pour Ciseaux")
    print("  q pour Quitter")

    while True:
        choix = input("Entrez votre choix: ").lower()
        if choix in choices:
            print(f"Vous avez choisi {choices[choix]}.")
            return choix
        else:
            print("Choix incorrect, veuillez réessayer.")

def get_choix_ordinateur():
    choix = random.choice(["c", "f", "s"])
    return choix

def determine_gagnant(utilisateur, ordinateur):
    if utilisateur == ordinateur:
        return "égalité"
    elif (utilisateur == "c" and ordinateur == "s") or (utilisateur == "f" and ordinateur == "c") or (utilisateur == "s" and ordinateur == "f"):
        return "Utilisateur"
    else:
        return "Ordinateur"

def jeu():

    print(f"------------------------------------------------")
    print(f"Bienvenue dans notre jeu Feuille, Caillou, Ciseaux!")
    print(f"Saurais-tu battre l'ordinateur à ce jeu...?")
    print(f"------------------------------------------------")
    time.sleep(3)

    score_utilisateur = 0
    score_ordinateur = 0

    while True:
        choix_utilisateur = get_choix_utilisateur()
        if choix_utilisateur == "q":
            print("Au plaisir de vous revoir.")
            break
        choix_ordinateur = get_choix_ordinateur()
        print(f"L'ordinateur a choisi {choices[choix_ordinateur]}.")
        gagnant = determine_gagnant(choix_utilisateur, choix_ordinateur)
        if gagnant == "Utilisateur":
            score_utilisateur += 1
            print(random.choice(phrases_victoires))
        elif gagnant == "Ordinateur":
            score_ordinateur += 1
            print(random.choice(phrases_defaites))
        else:
            print(random.choice(phrases_egalite))
        print(f"Score: Utilisateur {score_utilisateur} - Ordinateur {score_ordinateur}.")
        time.sleep(2)

jeu()