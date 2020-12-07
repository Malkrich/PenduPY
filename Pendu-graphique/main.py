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
