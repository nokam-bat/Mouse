# Feuille, Caillou, Ciseaux
## Objectif: Créer un jeu en python ou l'utlisateur choisit parmi feuille, caillou ou ciseaux et affronte l'ordinateur.
## Auteurs:
Ce projet a été réalisé par Nadia Abdi Mohamoud et Noor Kammoun.
## Fonctionnnement du jeu:
L'utilisateur entre son choix par le clavier
L'ordinateur choisit aléatoirement 
Le programme affiche qui a gagné et un message de victoire, de défaite ou d'égalité
## Lancer le jeu
Pour lancer le jeu, il suffit d'exécuter le fichier "combiné.py" sur votre IDE Python.
```mermaid
flowchart TD
    A((Début)) --> B[Afficher le message d'accueil]
    B --> C[Définir les scores de départ]
    C --> D[Entrée: Choix de l’utilisateur]
    D -->|q| E((Fin))
    D -->|c/f/s| F[Sortie: Afficher le choix de l’utilisateur]
    F --> G[Choix aléatoire de l’ordinateur]
    G --> H[Sortie: Afficher le choix de l’ordinateur]
    H --> I[Comparer les choix]
    I --> J{Résultat}
    J -->|Victoire| K[Sortie: Afficher le message de victoire]
    J -->|Défaite| L[Sortie: Afficher le message de défaite]
    J -->|Égalité| M[Sortie: Afficher le message d’égalité]
    K --> N[ Sortie: Afficher les scores]
    L --> N
    M --> N
    N-->D



