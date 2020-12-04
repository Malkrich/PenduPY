#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Nov 30 14:25:29 2020

@author: lemarie
"""

#Ce fichier prend en entrée le fichier de mot
#En sortie on retournera un mot aléatoire dans la liste de mo
import random

def choix_mots(fichier_mots):
    mots=open(fichier_mots)

    
    mots_liste=mots.readlines() #création d'une liste avec un mots par ligne
    
    #troncature de chaque mot pour enlever le "\n" à la fin
    for i in range(len(mots_liste)):
        mots_tronc=mots_liste[i]
        mots_tronc=mots_tronc[0:-1]
        mots_liste[i]=mots_tronc
        
    i = random.randint(0,len(mots_liste)-1) #choix d'un mots aléatoire dans la liste
    mots_retour=mots_liste[i].upper()
    
    #On définie un tableau donnant les lettres à afficher ou non
    #Si 0 : la lettre n'est pas affichée
    #Si 1 : la lettre est affichée
    lettres=[1]
    for i in range(len(mots_retour)-1):
        lettres.append(0)
    
    mots.close()
    return  mots_retour,lettres#on retourne le mot en majuscule