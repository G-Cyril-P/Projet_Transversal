Documentation du projet – Jeu de Loto
________________________________________
🔹 1. Documentation fonctionnelle
➤ Présentation du projet
Ce projet consiste à développer une application simulant un jeu de loto.
Le programme génère un tirage aléatoire de 10 numéros compris entre 1 et 49, puis permet à l’utilisateur de saisir ses propres numéros afin de les comparer avec le tirage.
L’objectif est de déterminer le nombre de numéros corrects et d’attribuer une récompense en fonction des résultats.
________________________________________
➤ Conception du projet
Avant de commencer le développement, nous avons identifié les étapes principales du programme :
1.	Générer un tirage aléatoire sans doublons 
2.	Permettre à l’utilisateur de saisir 10 numéros 
3.	Vérifier la validité des entrées 
4.	Comparer les numéros 
5.	Compter les correspondances 
6.	Ajouter un système de récompense 
7.	Implémenter un bonus basé sur l’ordre des numéros 
Nous avons également décidé de découper le programme en plusieurs fonctions pour améliorer la lisibilité et la maintenance.
________________________________________
➤ Lancement du programme
Pour exécuter le programme :
1.	Ouvrir un terminal 
2.	Se placer dans le dossier du projet 
3.	Exécuter la commande : 
python loto.py
________________________________________
➤ Fonctionnalités proposées
•	Génération automatique de 10 numéros aléatoires sans doublons 
•	Saisie utilisateur sécurisée : 
o	vérification de l’intervalle (1 à 49) 
o	refus des doublons 
o	gestion des erreurs de saisie 
•	Comparaison des numéros : 
o	affichage des numéros gagnants ou non 
•	Comptage du nombre de numéros corrects 
•	Système de récompense basé sur les résultats 
•	Bonus : 
o	vérification du nombre de numéros bien placés (même position) 
________________________________________
🔹 2. Documentation technique
➤ Choix techniques
•	Langage utilisé : Python 
•	Architecture : programmation modulaire avec fonctions 
•	Organisation du code : 
o	une fonction par fonctionnalité principale 
o	séparation claire des responsabilités 
Fonctions principales :
•	generer_tirage() : génère les numéros aléatoires 
•	saisir_numeros() : gère la saisie utilisateur 
•	comparer() : compare les résultats 
•	verifier_ordre() : gère le bonus 
•	recompense() : attribue les gains 
________________________________________
➤ Principales réalisations
•	Utilisation de random.sample() pour garantir l’absence de doublons 
•	Utilisation des ensembles (set) pour comparer efficacement les numéros 
•	Mise en place d’une gestion d’erreurs avec try/except 
•	Création d’un système de récompense basé sur deux critères : 
o	nombre de numéros corrects 
o	nombre de numéros bien placés 
________________________________________
➤ Problèmes rencontrés et solutions
Problème 1 : gestion des erreurs utilisateur
•	Entrées non numériques provoquant un crash 
•	Solution : utilisation de try/except 
Problème 2 : doublons dans la saisie
•	L’utilisateur pouvait entrer plusieurs fois le même numéro 
•	Solution : vérification avec if n in numeros 
Problème 3 : comparaison inefficace
•	Difficulté à comparer rapidement les listes 
•	Solution : utilisation des ensembles (set) 
Problème 4 : vérification de l’ordre
•	Comparaison position par position nécessaire 
•	Solution : boucle avec index 
________________________________________
➤ Outils utilisés
•	Langage : Python 
•	Gestion de version : Git 
•	IDE : (VS Code / PyCharm ) 
•	Outils d’assistance : IA (Copilot) 
________________________________________
➤ Utilisation de l’IA
Un outil d’intelligence artificielle a été utilisé pour :
•	améliorer la structure du code 
•	corriger certaines erreurs 
•	proposer des optimisations 
Le code a été compris, adapté et validé avant utilisation.
________________________________________


🔹 3. Conclusion
Ce projet nous a permis de :
•	maîtriser les bases du langage Python 
•	structurer un programme en plusieurs fonctions 
•	gérer les erreurs utilisateur 
•	utiliser Git pour le suivi du projet 
Le programme est fonctionnel, robuste et respecte les contraintes demandées.

