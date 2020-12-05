#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Fonction vérifiant si le mot est au complet
auquel cas, on retourne une victoire
On prend en arguement d'entrée le tableau des lettres trouvées
En sortie, on retourne : 
    True si il y a victoire
    False si il n'y a pas de victoire
"""

def verif_victoire(lettres_trouvees):
    somme=0
    
    #On somme tous les termes du tableau
    for i in range(len(lettres_trouvees)):
        somme+=lettres_trouvees[i] #incrémente 1 pour chaque lettre trouvée
           
    #On vérifie que cette somme est égale à la longueur
    #Si ce cas est vrai, dans ce cas cela veut dire que tous les termes sont à 1
    if somme == len(lettres_trouvees):
        return True
    else:
        return False