#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Cette fonction permet de vérifier si la lettre donnée par l'utilisateur
est comprise dans le mot
En entrée on donne donc la lettre donnée, le mot, le tableau de lettre trouvées et le nombre d'essai
On retourne en sortie le tableau de lettres trouvées, le nombre d'essai restant et :
    True si une lettre a été trouvé
    False si aucunes lettres n'a été trouvé
"""

def verif_lettre(lettre,mots,lettres_trouvees,essais):
    valid_lettre=False
    
    #vérification qu'une lettre existe dans ce mot
    for i in range(len(mots)):
        if mots[i] == lettre:
            lettres_trouvees[i]=1
            valid_lettre=True
    
    if valid_lettre == False:
        essais-=1
    
    return lettres_trouvees,essais,valid_lettre