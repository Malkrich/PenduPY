#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Fonction permettant de changer une image en fonction du nombre d'essais restant
"""

from tkinter import PhotoImage

#Cette fonction prend en entrée : essais et table image et l'objet canvas dans lequel
#il faut changer  d'image
#cette fonction retourne en sortie le nouveau canvas à afficher

def change_image(essais,table_images,can):
    can.delete("all")
    print(table_images[essais.get()-1])
    Image=PhotoImage(file=table_images[essais.get()-1])
    can.create_image(150, 150, image=Image)