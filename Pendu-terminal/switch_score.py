#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Cette fonction lit le fichier de score et le modifie en incrémentant de 1 le score
Cette fonction ne prend aucunes entrées, en sortie on a le score actuelle du joueur
"""

#La fonction lit dans un premier temps la valeur du score du joueur
#Dans un deuxième temps, elle réécrit dans le même fichier texte le score mis à jour
def switch_score():
    score=open('score.txt')
    
    val_score = score.readline().split(":")
    val_score=int(val_score[1][1])
    val_score+=1
    score.close()
    
    score=open('score.txt','w')
    print("score : "+str(val_score))
    score.write("score : "+str(val_score))
    score.close()
    return val_score