#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
programme principale executant les fonctions
"""

#Import des fonctions
from choix_mots import choix_mots
from mots_cache import mots_cache
from verif_lettre import verif_lettre
from verif_victoire import verif_victoire
from lettre_joue import lettre_joue
from switch_score import switch_score

reponse = "O"
score = 0

while reponse == "O":
    #Démarage du jeux : choix d'un mots et mise à 8 le nombre d'essais
    mots,lettres_trouvees = choix_mots("mots.txt")
    essais=8
    
    
    #Rappelle du tableau lettre :
    #Pour un 0 : la lettre n'est pas trouvée
    #Pour un 1 : la lettre est trouvée
    #On définie le mot cache en fonction du tableau de lettres trouvées
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
    
    #On part du principe que le score est le nombre d'essais non utilisés : 
    #   Un score de 8 veut dire que l'on a utilisé aucuns essais
    score,new_score=switch_score(essais,score) #on change de score si il est supérieur
    
    
    if verif_victoire(lettres_trouvees) == True:
        print("Bravo ! vous avez gagné !")
        if new_score == True:
            print("NOUVEAU RECORD ! Il est de ",score," essais non utilisés")
    elif essais == 0:
        print("Malhereusement, malgrés vos essais acharnés vous n'avez pas pu trouver le mots")
        print("Le mot était en fait : ",mots)
    
    print("Voulez vous recommencer ? (tapez O pour oui et N pour non)")
    reponse=input()
    reponse=reponse.upper() #on repasse en majuscule la lettre de réponse
    
print("Fin du jeux ! Au revoir")