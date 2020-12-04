#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Cette fonciont permet de lire le fichiers de mots et de trier celui ci.
Ce fichier prend en entrée le fichier de mots 'brut' et le fichier de mots
où l'on écrira les mots triés.
Cette fonction n'a pas de paramètres de sortie.
"""

"""
La fonction ouvre les deux fichiers texte : 
    - Le premier est le fichier dans lequelle on peut inscrire des mots
    - Le deuxième est en mode écriture, on écrira dedans les mots dans l'ordre de taille et alphabétique
"""
def sort_fichier(nom_fichier_brut,nom_fichier_sorted):
    mots=open(nom_fichier_brut)
    mots_sorted=open(nom_fichier_sorted,"w")
    
    mots_liste=mots.readlines() #création d'une liste avec un mots par ligne
    
    #troncature de chaque mot pour enlever le "\n" à la fin
    for i in range(len(mots_liste)):
        mots_liste[i]=mots_liste[i][0:-1]
    
    mots_liste.sort()
    mots_liste.sort(key=len) #trie des mots par ordre de taille
    print(mots_liste)
    
    #écriture dans un nouveau fichier :
    for i in range(len(mots_liste)):
        mots_sorted.write(mots_liste[i]+"\n")
    
    mots.close()
    mots_sorted.close()