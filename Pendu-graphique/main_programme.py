#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Ce programme principal permet de créer la fenêtre et de lancer le jeux
"""

from choix_mots import choix_mots #permet de choisir un mots au hasard dans la liste de mots
from mots_cache import mots_cache #permet d'afficher sur la console le mots avec des '_' lorsque les lettres sont cachées
from verif_lettre import verif_lettre #permet de vérifier si la lettre entrée est compris dans le mot ou non et modifie le nombre d'essais restants
from verif_victoire import verif_victoire #permet de vérifier si le mot joué a été trouvé ou non
from lettre_joue import lettre_joue #vérifie si une lettre a déjà été trouvé ou non
from switch_score import switch_score #permet de modifier le score du joueur lorsqu'il gagne
from maj_fichiertxt import sort_fichier #permet de mettre à jour le fichiers de mots dans l'ordre de taille puis par ordre alphabétique
from main_interface import jouer, recommencer #fonction jouer et recommencer des boutons
from change_image import change_image
from tkinter import Tk, Label, Entry, Canvas, PhotoImage, Button, Menu, StringVar, IntVar

def macro_recommencer():
    global mots,table_lettres,lettre_jeu,essais
    lettre_jeu=[]
    essais.set(8)
    mots,table_lettres = recommencer(mots_inter) #rechoisie une mots parmis la table de mots

def macro_jouer(lettre):
    global mots,table_lettres,mots_inter,essais,lettre_jeu,table_images,can,fen_jeux
    if lettre_joue(lettre,lettre_jeu) == False:
        essais = jouer(lettre,mots,table_lettres,essais,mots_inter)
        print(essais.get())
        #change_image(essais,table_images,can)
        can.delete("all")
        print(table_images[essais.get()-1])
        Image=PhotoImage(file=table_images[essais.get()-1])
        can.create_image(150, 150, image=Image)
    
    else:
        print("Lettre déjà jouée")
        print(essais.get())
    
    lettre_jeu.append(lettre)

#définition d'une table permettant de changer l'image durant la partie
table_images=[]
for i in range(8):
    table_images.append('images/bonhomme'+str(i+1)+'.gif')

print(table_images)

sort_fichier('mots.txt','mots_sort.txt')
mots,table_lettres=choix_mots('mots_sort.txt')
mots_jeux=mots_cache(mots,table_lettres)
lettre_jeu=[] #table des lettres jouées durant une partie
print("Mots joué :",mots)

#Création de la fenêtre
fen_jeux = Tk()

#Ajout menu
menubar=Menu(fen_jeux)
menu_action= Menu(menubar,tearoff=0)
menu_action.add_command(label="Quitter",command=fen_jeux.destroy)
menubar.add_cascade(label="Action",menu=menu_action)

#Ajout wigget interface
mots_inter=StringVar()
mots_inter.set(mots_jeux)
essais = IntVar()
essais.set(8)
lbl_mots=Label(fen_jeux, textvariable=mots_inter)
txt_lettre=Entry(fen_jeux)
bouton_jouer = Button(fen_jeux, text="Proposer", fg='black', command=lambda:macro_jouer(txt_lettre.get()))
bouton_recommencer = Button(fen_jeux, text="Recommencer", fg='black', command=macro_recommencer)
can = Canvas(fen_jeux, width=300, height=300, bg='white')
Image_pendu = PhotoImage(file=table_images[essais.get()-1])
can.create_image(150, 150, image=Image_pendu)
can.grid(row=1, rowspan=3, column=3)


#Mise en place de l'interface
#fen_jeux.config(menu=menubar)
fen_jeux.title("Jeux du pendu")
lbl_mots.grid(row=1, column=1, columnspan=2)
txt_lettre.grid(row=2, column=1, columnspan=2)
bouton_jouer.grid(row=3, column=1)
bouton_recommencer.grid(row=3, column=2)

fen_jeux.mainloop()