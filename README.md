# Feuille, Caillou, Ciseaux
*Feuille, Caillou, Ciseaux* : un jeu classique codé en Python. 

### Informations générales
- Cours: INI-03 - Mini projet de groupe
- Date de rendu: 12 octobre 2025 
- Élèves: Nadia Abdi Mohamoud et Noor Kammoun (SI-CA1a) 

## Description 
Le projet consiste à créer une application simple en Python permettant à un utilisateur de jouer à *Feuille, Caillou, Ciseaux* contre l’ordinateur. L’utilisateur entre son choix, l’ordinateur génère le sien aléatoirement, puis le programme affiche le résultat, un message personnalisé en fonction de celui-ci et le score actuel.

## Fonctionnalités 

- Affichage d'un message d’accueil au lancement du jeu

- Saisie du choix de l’utilisateur (*feuille*, *caillou*, *ciseaux* ou *quitter*) 

- Choix aléatoire de l’ordinateur 

- Affichage du résultat 

- Affichage d'un message personnalisé en fonction du résultat (victoire, défaite ou égalité) 

- Affichage du score cumulé entre l'utilisateur et l'ordinateur 

- Possibilité de rejouer ou de quitter à tout moment

## Fonctions du programme 

- **get_choix_utilisateur()**: affiche les choix de jeu et récupère le choix valide de l'utilisateur grâce une boucle de contrôle des saisies (*c*, *f*, *s* ou *q*).

- **get_choix_ordinateur()**: génère aléatoirement le choix de l'ordinateur parmi le choix *c*,*f* ou *s*.

- **determine_gagnant(utilisateur, ordinateur)**: compare les choix de l'utilisateur et l'ordinateur puis retourne le résultat de la manche (victoire, défaite ou égalité)

- **jeu()**:la boucle principale qui gère le déroulement complet du jeu.  
Elle affiche un message de bienvenue, puis permet à l’utilisateur de jouer plusieurs manches contre l’ordinateur jusqu’à ce qu’il souhaite s'arrêter. 
  - À chaque manche, elle récupère les choix de l’utilisateur et de l’ordinateur, détermine le gagnant, met à jour les scores, et affiche des messages personnalisés en fonction du résultat.

## Diagrammes de flux
### Diagramme 1: get_choix_utilisateur
<img width="600" alt="get_choix_utilisateur drawio" src="https://github.com/user-attachments/assets/144fac77-6218-4a4a-add5-73c97cfe04e6" />

### Diagramme 2: get_choix_ordinateur
<img width="600" alt="get_choix_ordi drawio" src="https://github.com/user-attachments/assets/9ed20010-9c84-4566-be0b-b9fc0d3c8257" />

### Diagramme 3: determine_gagnant
<img width="600" alt="determine_gagnant() drawio" src="https://github.com/user-attachments/assets/ca80448f-e2ac-4462-a5e5-6e4c2ec462fa" />

### Diagramme 4: jeu
<img width="600" alt="jeu() drawio" src="https://github.com/user-attachments/assets/aea03131-5047-43c4-a5ad-0b1a2df04de3" />

  
## Niveau de difficulté : 
- Utilisation de boucles `while` pour gérer et contrôler les entrées   utilisateurs
- Boucle principale pour le déroulement du jeu
- Utilisation de structures conditionnelles  (`if`, `else`, `elif`)
- Utilisation d'un dictionnaire pour générer les choix
- Importation et utilisation de bibliothèques standards Python `time` (pauses entre les messages) et `random` (choix aléatoire)
- Utlisation de listes pour stocker et afficher les messages personnalisés
- Suivi et mis à jour du score de l'utilisateur et de l'ordinateur
- Organisation du code en fonctions claires et distinctes 

## Installation 

### Prérequis 

Python 3.12 doit être installé sur votre ordinateur.

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
Après avoir lancé le programme, un message d’accueil s'affichera et vous invitera à choisir parmi ces quatre options :*feuille*, *caillou*, *ciseaux* ou *quitter*.

Le programme affichera ensuite : 
- Le choix de l’utilisateur (si *quitter*, il affichera un message d’adieu) 
- Le résultat de la manche 
- Un message personnalisé selon le résultat
- Le score actuel 
- La possibilité de rejouer ou de quitter 

## Bibliothèques utilisées : 

Nous avons utilisé des bibliothèques python standards tels que : 

- `random`:  pour générer des choix aléatoires pour l’ordinateur et choisir les messages personnalisés 

- `time` : pour ajouter des pauses (laisser le temps de lire à l’utilisateur, simule une réflexion de l’ordinateur et effet de suspense) 

## Répartition du travail

| Membre du groupe        | Tâches réalisées                                      |
|-------------------------|-------------------------------------------------------|
| Nadia Abdi Mohamoud               | La fonction de choix de l’utilisateur, la création de listes avec des messages défaites/gagnants/égalités et le message d’accueil, la rédaction du README.
| Noor Kammoun                      | La fonction choix aléatoire de l’ordinateur, la gestion des saisies incorrectes de l'utilisateur, la création d'un dictionnaire pour les choix de l'utilisateur, la gestion des scores.                                                     |
| Ensemble                | La fonction pour déterminer le résultat (victoire, défaite, égalité), les diagrammes de flux, les commentaires, la fonction du jeu.                   |

## Ajustements du projet et choix réalisés
Au départ, nous avions prévu de limiter chaque partie à trois manches maximum. Néanmoins, cela s’est avéré trop rigide au niveau de l’expérience utilisateur. Par la suite, la possibilité de quitter (q) a été implémentée.
De plus, la boucle `while` utilisé pour contrôler les entrées utilisateurs n’est pas représenté dans les diagrammes de flux car elle alourdirait inutilement la structure Elle n’est pas nécessaire à la compréhension de la logique du programme tout comme les `time.sleep`. On souhaitait également trouver une façon d’éviter que les messages personnalisés d’une liste soient tous utilisées une fois avant de se répéter mais nous n’avons pas eu le temps.  

## Améliorations possibles
- Permettre à deux utilisateurs humains de jouer l’un contre l’autre. 
- Ajouter une interface graphique en utilisant Tkinter.
- Mettre en place un système pour éviter la répétition des messages personnalisés avant qu'ils ne soient tous utilisés.
  
## Conclusion
Ce projet nous a permis de mettre en pratique les notions de base de Python tels que les fonctions, les conditions et les boucles. Nous avons appris à structurer un petit projet en groupe et à utiliser GitHub.

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
