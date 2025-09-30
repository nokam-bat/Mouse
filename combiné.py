#Importer le choix aléatoire de l'ordi et le temps.
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

#Faire un dictionnaire.
choices = {
    "c" : "Caillou",
    "f" : "Feuille",
    "s" : "Ciseaux",
    "q" : "Quitter"
}

#Récupérer le choix de l'utilisateur.
def get_choix_utilisateur():
    print("Faites votre choix: ")
    print("  c pour Caillou")
    print("  f pour Feuille")
    print("  s pour Ciseaux")
    print("  q pour Quitter")

# On entre dans la boucle while. Cette boucle est pour contrôler ce qui est entré par l'utilisateur. Afin qu'on n'accepte que ce que l'on a décidé. Aussi on s'assure de transformer une potentielle majuscule en minuscule.
    while True:
        choix = input("Entrez votre choix: ").lower()
        if choix in choices:
            print(f"Vous avez choisi {choices[choix]}.")
            return choix
        else:
            print("Choix incorrect, veuillez réessayer.")

#On programme le choix de l'ordinateur.
def get_choix_ordinateur():
    choix = random.choice(["c", "f", "s"])
    return choix

#On détermine le vainqueur et on affiche des messages selon le résultat de la partie.
def determine_gagnant(utilisateur, ordinateur):
    if utilisateur == ordinateur:
        return "égalité"
    elif (utilisateur == "c" and ordinateur == "s") or (utilisateur == "f" and ordinateur == "c") or (utilisateur == "s" and ordinateur == "f"):
        return "Utilisateur"
    else:
        return "Ordinateur"

#On programme la logique de la partie.
def jeu():

    print(f"------------------------------------------------------")
    print(f"Bienvenue dans notre jeu \033[3mFeuille, Caillou, Ciseaux\033[0m !")
    print(f"Sauras-tu battre l'ordinateur à ce jeu...?")
    print(f"------------------------------------------------------")
#On rajoute un time.sleep afin d'avoir 3 secondes de délai.
    time.sleep(3)
#On note les scores pour garder le compte.
    score_utilisateur = 0
    score_ordinateur = 0

#On fait une boucle while qui permettras de relancer le jeu jusqu'à ce que l'utilisateur choisit de quitter par lui-même.
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
            time.sleep(2)
            print(f"Le vainqueur est: {gagnant}")
            time.sleep(1)
            print(random.choice(phrases_victoires))

        elif gagnant == "Ordinateur":
            score_ordinateur += 1
            print(f"Le vainqueur est: {gagnant}")
            time.sleep(1)
            print(random.choice(phrases_defaites))

        else:
            print("C'est une égalité!")
            time.sleep(1)
            print(random.choice(phrases_egalite))
#On note le score qui sera mis à jour à chaque réitération de la boucle.
        print(f"Score: Utilisateur {score_utilisateur} - Ordinateur {score_ordinateur}.")
        time.sleep(3)
        print(f"------------------------------------------------------")
        print(f"------------------------------------------------------")

#On initie le jeu.
jeu()