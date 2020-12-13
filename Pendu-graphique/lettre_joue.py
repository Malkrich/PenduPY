#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Verifie si la lettre est déjà joué
On prend en paramètre la lettre entrée par l'utilisateur et les lettres déjà utilisés
On retourne true si la lettre a déjà été joué
On retourne false si la lettre n'a pas déjà été joué
"""

def lettre_joue(lettre,lettres_donnees):
    for i in range(len(lettres_donnees)):
        if lettres_donnees[i]==lettre:
            return True

    return False