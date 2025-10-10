# Feuille, Caillou, Ciseau 
*Feuille, Caillou, Ciseaux* : un jeu classqiue codé en Python. 

### Informations générales
- Cours: INI-03 - Mini projet de groupe
- Date de rendu: 12 octobre 2025 
- Élèves: Nadia Abdi Mohamoud et Noor Kammoun (SI-CA1a) 

## Description 
Le projet consiste à créer une application simple en Python permettant à un utilisateur de jouer à *Feuille, Caillou, Ciseaux* contre l’ordinateur. L’utilisateur entre son choix, l’ordinateur génère le sien de manière aléatoire, puis le programme affiche le résultat, un message personnalisé en fonction de celui-ci et le score actuel.

## Fonctionnalités 

- Affichage d'un message d’accueil au lancement du jeu

- Saisie du choix de l’utilisateur (*feuille*, *caillou*, *ciseaux* ou *quitter*) 

- Choix aléatoire de l’ordinateur 

- Affichage du résultat 

- Affichage d'un message personnalisé en fonction du résultat (victoire, défaite ou égalité) 

- Affichage du score cumulé entre l'utilisateur et l'ordinateur 

- Possibilité de rejouer ou de quitter à tout moment

## Fonctions du programme 

- **get_choix_utlisateur()**: affiche les choix de jeu et recupère le choix valide de l'utilisateur grâce une boucle de contrôle des saisies (*c*, *f*, *s* ou *q*).

- **get_choix_ordinateur()**: génère aléatoire le choix de l'ordinateur parmi le choix *c*,*f* ou *s*.

- **determine_gagnant(utilisateur, ordinateur)**: compare les choix de l'utlisateur et l'ordinateur puis retourne le résultat de la manche (victoire, défaite ou égalité)

- **jeu()**:la boucle principale qui gère le déroulement complet du jeu.  
Elle affiche un message de bienvenue, puis permet à l’utilisateur de jouer plusieurs manches contre l’ordinateur jusqu’à ce qu’il souahite s'arrêter. 
  - À chaque manche, elle récupère les choix de l’utilisateur et de l’ordinateur, détermine le gagnant, met à jour les scores, et affiche des messages personnalisés en fonction du résultat.

## Diagrammes de flux
![Diagramme 1:get_choix_utlisateur()] (./images/)

  
## Niveau de difficulté : 
- Utilisation de boucles *while* pour gérer et contrôler les entrées   utlisateurs
- Boucle principale pour le délourement du jeu
- Utilisation de structures conditionnelles  (*if*, *else*, *elif*)
- Utilisation d'un dictionnaire pour générer les choix
- Importation et utilisation de bibliothèques standards Python *time* (pauses entre les messages) et *random* (choix aléatoire)
- Utlisation de listes pour stocker et afficher les messages personnalisés
- Suivi et mis à jour du score de l'utlisateur et de l'ordinateur
- Organisation du code en fonctions claires et disctinctes 

## Installation 

### Prérequis 

Python 3.13 doit être installé sur votre ordinateur.

### Étapes 

**Téléchargez le projet**: 

1. Allez sur le dépôt GitHub (repository).

2. Cliquez sur le bouton vert **Code** puis sélectionnez **Download ZIP**. 

3. Extrayez le fichier ZIP dans un dossier de votre choix. 

4. **Ouvrez le dossier du projet**, par exemple dans un terminal ou via un éditeur de code comme VS Code ou Pycharm. 

5. **Lancez le programme** avec la commande suivante dans le terminal :
```bash
   python Feuille_Caillou_Ciseaux.py.
```
## Utilisation 
Après avoir lancé le programme, un message d’accueil s'affichera et vous invitera à choisir parmi ces quatre options : *feuille*, *caillou*, *ciseaux* ou *quitter*. 
Le programme affichera ensuite : 
- Le choix de l’utilisateur (si *quitter*, il affichera un message d’adieu) 
- Le résultat de la manche 
- Un message personnalisé selon le résultat
- Le score actuel 
- La possibilité de rejouer ou de quitter 

## Bibliothèques utilisées : 

Nous avons utilisé des bibliothèques python standards tels que : 

- random:  pour générer des choix aléatoires pour l’ordinateur et choisir les messages personnalisés 

- time : pour ajouter des pauses (laisser le temps de lire à l’utilisateur, simule une réflexion de l’ordinateur et effet de suspense) 

## Répartition du travail

| Membre du groupe        | Tâches réalisées                                      |
|-------------------------|-------------------------------------------------------|
| Nadia Abdi Mohamoud               | La fonction de choix de l’utilisateur, la création de listes avec des messages défaites/gagnants/égalités et le message d’accueil, la rédaction du READ.me.
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
