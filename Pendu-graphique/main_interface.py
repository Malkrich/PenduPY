"""
Ce programme repertorie toutes les fonctions des actions que l'on peut effectuer
sur l'interface
"""

#Import des fonctions
from choix_mots import choix_mots #permet de choisir un mots au hasard dans la liste de mots
from mots_cache import mots_cache #permet d'afficher sur la console le mots avec des '_' lorsque les lettres sont cachées
from verif_lettre import verif_lettre #permet de vérifier si la lettre entrée est compris dans le mot ou non et modifie le nombre d'essais restants
from verif_victoire import verif_victoire #permet de vérifier si le mot joué a été trouvé ou non
from lettre_joue import lettre_joue #vérifie si une lettre a déjà été trouvé ou non
from switch_score import switch_score #permet de modifier le score du joueur lorsqu'il gagne
from maj_fichiertxt import sort_fichier #permet de mettre à jour le fichiers de mots dans l'ordre de taille puis par ordre alphabétique
from tkinter import Tk, Label, Entry, Canvas, PhotoImage, Button, Menu, StringVar, IntVar

def jouer(lettre,mots,table_lettres,essais,mots_inter):
    print("Jouer")
    lettre=lettre.upper()
    table_lettre,essais_int,valid_lettre=verif_lettre(lettre,mots,table_lettres,essais.get())
    essais.set(essais_int)
    
    if valid_lettre:
        mots_jeux=mots_cache(mots,table_lettres)
        mots_inter.set(mots_jeux)
    else:
        print(essais.get())

def recommencer(mots_inter):
    mots, table_lettres=choix_mots('mots_sort.txt')
    mots_jeux=mots_cache(mots,table_lettres)
    print("Mots joué :",mots)
    mots_inter.set(mots_jeux)
    return mots, table_lettres