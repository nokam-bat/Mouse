#En-tête:
#Nadia Abdi Mohamoud et Noor Kammoun (SI-CA1a)
#INI-03: Mini projet de groupe - Feuille , Caillou, Ciseaux
#Date de rendu: 11 octobre 2025


#Importation des bibliothèques random et time
import random
import time

#Création de listes avec des messages personnalisés en fonction de résultat: victoire, défaite ou égalité
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

#Faire un dictionnaire avec les choix possibles:
choices = {
    "c" : "Caillou",
    "f" : "Feuille",
    "s" : "Ciseaux",
    "q" : "Quitter"
}

#Fonction qui génère le choix de l'utilisateur:
def get_choix_utilisateur():
    print("Faites votre choix: ")
    print("  c pour Caillou")
    print("  f pour Feuille")
    print("  s pour Ciseaux")
    print("  q pour Quitter")

#Boucle de contrôle des entrées utlisateurs:
    while True:
        choix = input("Entrez votre choix: ").lower()
        if choix in choices:
            print(f"Vous avez choisi {choices[choix]}.")
            return choix
        else:
            print("Choix incorrect, veuillez réessayer.")

#Fonction qui génère le choix aléatoire de l'ordinateur:
def get_choix_ordinateur():
    choix = random.choice(["c", "f", "s"])
    return choix

#Fonction qui compare les choix et affiche le gagnant, le perdant ou l'égalité:
def determine_gagnant(utilisateur, ordinateur):
    if utilisateur == ordinateur:
        return "égalité"
    elif (utilisateur == "c" and ordinateur == "s") or (utilisateur == "f" and ordinateur == "c") or (utilisateur == "s" and ordinateur == "f"):
        return "Utilisateur"
    else:
        return "Ordinateur"

# La fonction principale du jeu qui regroupe toutes les étapes d'une manche :
# - affichage du message d'accueil 
# - demande du choix utilisateur
# - génération du choix ordinateur
# - comparaison des deux choix
# - affichage du gagnant et d’un message personnalisé

def jeu():
    print(f"------------------------------------------------------")
    print(f"Bienvenue dans notre jeu \033[3mFeuille, Caillou, Ciseaux\033[0m !")
    print(f"Sauras-tu battre l'ordinateur à ce jeu...?")
    print(f"------------------------------------------------------")

#On rajoute un time.sleep afin d'avoir 3 secondes de délai entre le message d'accueil et le début de la partie:
    time.sleep(3)

#Suivi des scores de l'utilisateur et de l'ordinateur:
    score_utilisateur = 0
    score_ordinateur = 0

#Boucle principale du jeu qui permet à l'utilisateur de jouer autant de fois qu'il le souhaite jusqu'à ce qu'il entre "q" pour quitter:

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
            time.sleep(2)
            print(f"Le vainqueur est: {gagnant}")
            time.sleep(1)
            print(random.choice(phrases_defaites))

        else:
            print("C'est une égalité!")
            time.sleep(1)
            print(random.choice(phrases_egalite))

#Le score est mis à jour à chaque tour de boucle:
        print(f"Score: Utilisateur {score_utilisateur} - Ordinateur {score_ordinateur}.")
        time.sleep(3)
        print(f"------------------------------------------------------")
        print(f"------------------------------------------------------")

#Lancement du jeu:

jeu()

