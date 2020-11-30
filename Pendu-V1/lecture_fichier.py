#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Cette fonciont permet de lire le fichiers de mots.
La fonction classe ensuite ces mots par taille puis par ordre alphabétique pour chaque tailles
"""

#Cette fonction prend pour arguement d'entrée : le nom du fichier
#Cette n'a rien en sortie
def sort_fichier(nom_fichier_brut,nom_fichier_sorted):
    mots=open(nom_fichier_brut)
    mots_sorted=open(nom_fichier_sorted,"w")
    
    
        
    mots.close()
    mots_sorted.close()