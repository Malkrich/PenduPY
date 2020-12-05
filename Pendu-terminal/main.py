#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Programme principale du jeux de pendu en mode console
Ce programme n'as pas de fonctions mais exécute toutes celle indiqués au début
Dans un premier temps on choisie parmis des actions
Puis :
    - On lance le jeux
    - On met à jour la liste des mots
    - On quitte le jeux
"""

#Import des fonctions
from choix_mots import choix_mots #permet de choisir un mots au hasard dans la liste de mots
from mots_cache import mots_cache #permet d'afficher sur la console le mots avec des '_' lorsque les lettres sont cachées
from verif_lettre import verif_lettre #permet de vérifier si la lettre entrée est compris dans le mot ou non et modifie le nombre d'essais restants
from verif_victoire import verif_victoire #permet de vérifier si le mot joué a été trouvé ou non
from lettre_joue import lettre_joue #vérifie si une lettre a déjà été trouvé ou non
from switch_score import switch_score #permet de modifier le score du joueur lorsqu'il gagne
from maj_fichiertxt import sort_fichier #permet de mettre à jour le fichiers de mots dans l'ordre de taille puis par ordre alphabétique

reponse = "O" #réponse pour recommencer
action = ""

while reponse == "O" and action != "Q":
    #Démarage du jeux : choix d'un mots et mise à 8 le nombre d'essais
    print("Que voulez-vous faire ? ")
    print("  - M pour mettre à jour la feuille de mots\n  - J pour jouer\n  - Q pour quitter")
    action = input("? ").upper()

    if action == "M":
        sort_fichier("mots.txt","mots_sort.txt")
        print("Le fichier de mot a bien été mis à jour !\n")
    
    if action == "J":
        """NOTES, détails du tableau de lettre :
        Pour un 0 : la lettre n'est pas trouvée
        Pour un 1 : la lettre est trouvée
        On définie le mot cache en fonction du tableau de lettres trouvées"""
        
        mots,lettres_trouvees = choix_mots("mots_sort.txt")
        essais=8
        mots_affiche = mots_cache(mots,lettres_trouvees)
        lettres_donnees=[] #liste des lettres qui ont déjà été tentées par l'utilisateur
        
        
        while essais != 0 and verif_victoire(lettres_trouvees)==False:
            #Affichage du début du tour
            print(mots_affiche)
            print("Il vous reste : ",essais," essai(s)")
            if len(lettres_donnees) != 0:
                print("Vous avez déjà tenté les lettres suivante : \n")
                for i in range(len(lettres_donnees)):
                    print(lettres_donnees[i],",")
            
            #Saisi d'une lettre
            lettre = input("Donnez une lettre : ")
            lettre=lettre.upper() #on repasse en majuscule la lettre entrée pour éviter les soucis de comparaison
            
            #vérification que la lettre entrée par l'utilisateur n'est pas déjà utilisé
            if lettre_joue(lettre,lettres_donnees)==False:
                lettres_trouvees,essais,valid_lettre=verif_lettre(lettre,mots,lettres_trouvees,essais)
        
                if valid_lettre==True:
                    print("Yes ! Vous avez trouvé une lettre\n\n")
                    mots_affiche = mots_cache(mots,lettres_trouvees) #mise à jour du mot à afficher
                elif valid_lettre==False:
                    print("Mince.. Cette lettre n'est pas dans ce mots\n\n")
                    
                lettres_donnees.append(lettre) #on ajoute la lettre dans la liste de lettres qui ne fonctionnent pas
            
            else:
                print("La lettre que vous avez entrée à déjà été donné, ce serait dommage de retenter la même chose...")

        print("FIN DU JEUX")

    #Le score enregistre le nombre de mots devinés
    #On enregistre ce score dans un fichier texte pour le garder en mémoire

        if verif_victoire(lettres_trouvees) == True:
            new_score=switch_score() #si il y a victoire, on incrémente de 1 le score
            print("Bravo ! vous avez gagné !")
            print("Vous avez deviné ",new_score," mots !")
        elif essais == 0:
            print("Malhereusement, malgrés vos essais acharnés vous n'avez pas pu trouver le mots")
            print("Le mot était en fait : ",mots)
    
        print("Voulez vous recommencer ? (tapez O pour oui et N pour non)")
        reponse=input()
        reponse=reponse.upper() #on repasse en majuscule la lettre de réponse

print("Fin du jeux ! Au revoir")