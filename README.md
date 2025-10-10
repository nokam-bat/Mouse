INI-03: Mini projet de groupe -  Feuille, Caillou, Ciseaux 

Nadia Abdi Mohamoud et Noor Kammoun (SI-CA1a) 

Date de rendu: 12 octobre 2025 

# Feuille, Caillou, Ciseau 

Un jeu en python permettant de jouer à *Feuille, Caillou, Ciseaux* contre l’ordinateur. 

## Description 

Le projet consiste à créer une application simple permettant à un utilisateur de jouer à feuille, caillou, ciseaux contre l’ordinateur. L’utilisateur entre son choix, l’ordinateur génère le sien aléatoirement, puis le programme affiche le résultat, un message personnalisé en fonction de celui-ci et le score de chaque manche. 

## Fonctionnalités 

- Message d’accueil affiché au début de la partie 

- Entrée de l’utilisateur (feuille, caillou, ciseaux, quitter) 

- Choix de l’ordinateur généré aléatoirement 

- Affichage du résultat 

- Message personnalisé en fonction du résultat (victoire, défaite ou égalité) 

- Affichage du score utilisateur vs ordinateur cumulé 

- Possibilité de rejouer autant de fois que l’on souhaite

## Fonctions du programme 

- Fonction choix de l’utilisateur 

- Fonction choix de l’ordinateur 

- Fonction pour déterminer le résultat (victoire, défaite, égalité)

- Fonction du jeu 

## Niveau de difficulté : 

- Utilisation de boucle 

- Utilisation de structures conditionnelles  (if, else, elif) 

- Importation et utilisation de bibliothèques *time* et *random*

## Installation 

### Prérequis 

Python 3.13 doit être installé sur votre ordinateur.

### Étapes 

**Téléchargez le projet**: 

1. Aller sur le dépôt GitHub (repository).

2. Cliquez sur le bouton vert **Code** puis **Download ZIP**. 

3. Extrayez le fichier ZIP dans un dossier. 

4. **Ouvrez le dossier du projet**	 

Par exemple dans un terminal ou via un éditeur de code comme VS Code ou Pycharm. 

5. **Lancer le programme** avec la commande suivante dans le terminal : python Feuille_Caillou_Ciseaux.py. 

## Utilisation 

Après avoir lancer le programme, un message d’accueil s'affichera et vous demandera de choisir pami ces quatre options : feuille, caillou, ciseaux ou quitter. Il affichera ensuite : 

- Le choix de l’utilisateur (si quitter, il affichera un message d’adieu) 

- Le résultat de la manche 

- Un message personnalisé 

- Le score actuel 

- On peut rejouer ou quitter 

## Bibliothèques utilisées : 

Nous avons utilisé des bibliothèques python standards tels que : 

- random:  pour générer des choix aléatoires pour l’ordinateur et choisir les messages personnalisés 

- time : pour ajouter des pauses (laisser le temps de lire à l’utilisateur, simule une réflexion de l’ordinateur et effet de suspense) 

## Répartition du travail

| Membre du groupe        | Tâches réalisées                                      |
|-------------------------|-------------------------------------------------------|
| Nadia Abdi Mohamoud               | La fonction de choix de l’utilisateur, la création de listes avec des messages défaites/gagnants/égalités et le message d’accueil, la rédaction du read.me.
| Noor Kammoun                      | La fonction choix aléatoire de l’ordinateur, la gestion des saisies incorrectes de l'utilisateur, la création d'un dictionnaire pour les choix de l'utilisateur, la gestion des scores.                                                     |
| Ensemble                | La fonction pour déterminer le résultat (victoire, défaite, égalité), les diagrammes de flux, les commentaires, la fonction du jeu.                   |

## Références
Ce projet s'est appuyé sur les ressources suivantes: 
- Documentation python du cours
- Documentation GitHub: https://docs.github.com/fr/get-started/start-your-journey/hello-world  
- Bibliothèques standards de python *time* et *random*
- Camarade de classe: Amin Torrisi
- Enseignants: Claude Rochat (CPNV), Julien Savary (CPNV) et Yassine Kammoun (HEIGVD)
- Microsoft Copilot
- ChatGPT
- Draw.io
