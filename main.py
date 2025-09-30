#importer le choix aléatoire de l'ordi.
import random
import time

#faire un dictionnaire
choices = {
    "c" : "Caillou",
    "f" : "Feuille",
    "s" : "Ciseaux",
    "q" : "Quitter"
}

#récupérer le choix de l'utilisateur.
def get_user_choice():
    print("Faites votre choix: ")
    print("  c pour Caillou")
    print("  f pour Feuille")
    print("  s pour Ciseaux")
    print("  q pour Quitter")

#On entre dans la boucle while. Cette boucle est pour contrôler ce qui est entré par l'utilisateur. Afin qu'on n'accepte que ce que l'on a décidé.
    while True:
        choice = input("Entrez votre choix: ")
        choice = choice.lower()
        if choice in choices:
            print(f"Vous avez choisi {choices[choice]}.")
            return choice
        else:
            print("Choix incorrect, veuillez rééssayer.")

#on programme le choix de l'ordinateur
def get_computer_choice():
    choice = random.choice(["c", "f", "s"])
    return choice

#on détermine le vainqueur et on affiche des messages selon le résultat de la partie.
def determine_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        return "Egalité"
    elif (user_choice == "c" and computer_choice == "s") or (user_choice == "f" and computer_choice == "c") or (user_choice == "s" and computer_choice == "f"):
        return "Utilisateur"
    else:
        return "Ordinateur"

#on programme la logique de la partie.
def play():
    print("Bienvenue dans notre jeu Feuille, Caillou, Ciseaux.")
    score_user = 0
    score_computer = 0

    while True:
        user_choice = get_user_choice()
        if user_choice == "q":
            print("Au plaisir de vous revoir.")
            break
        computer_choice = get_computer_choice()
        print(f"L'ordinateur a choisi {choices[computer_choice]}.")
        winner = determine_winner(user_choice, computer_choice)
        if winner == "Utilisateur":
            score_user += 1
            print("Bravo! Vous avez gagné.")
        elif winner == "Ordinateur":
            score_computer += 1
            print("Dommage, vous avez perdu.")
        else:
            print("C'est une égalité!")
        print(f"Score: Utilisateur {score_user} - Ordinateur {score_computer}.")
        time.sleep(2)


#point d'entrée du jeu.
play()