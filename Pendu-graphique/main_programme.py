#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Ce programme principal permet de créer la fenêtre et de lancer le jeux
Les lettres jouées seront en majuscule et le mot est en majuscule
"""

"""LIBRAIRIES"""
from choix_mots import choix_mots #permet de choisir un mots au hasard dans la liste de mots
from mots_cache import mots_cache #permet d'afficher sur la console le mots avec des '_' lorsque les lettres sont cachées
from verif_victoire import verif_victoire #permet de vérifier si le mot joué a été trouvé ou non
from lettre_joue import lettre_joue #vérifie si une lettre a déjà été trouvé ou non
from switch_score import switch_score #permet de modifier le score du joueur lorsqu'il gagne
from maj_fichiertxt import sort_fichier #permet de mettre à jour le fichiers de mots dans l'ordre de taille puis par ordre alphabétique
from main_interface import jouer, recommencer #fonction jouer et recommencer des boutons
from tkinter import Tk, Label, Entry, Canvas, PhotoImage, Button, Menu, StringVar, IntVar #ajouts librairie de l'interface


"""
Fonction appelé lorque l'on appuis sur le bouton recommencer
Ce bouton permet de rechoisir un mot et réinitialiser les variables qui vont avec soit :
essais, mots, table_lettre
On remet en place le champ texte à remplir pour une nouvelle partie
"""

#Cette fonction n'as aucunes entrées ni sorties
def macro_recommencer():
    global mots,table_lettres,lettre_jeu,essais
    lettre_jeu=[]
    essais.set(8)
    mots,table_lettres = recommencer(mots_inter) #rechoisie une mots parmis la table de mots
    txt_lettre=Entry(fen_jeux) #réinitialisation de txt_lettre pour une nouvelle partie
    txt_lettre.grid(row=2, column=1, columnspan=2)

"""
Fonction appelé lorsque l'on appuis sur le bouton jouer
Elle permet dans un premier temps de vérifier si la lettre à déjà été joué ou non
Si la lettre n'a pas été joué, elle vérifie si la lettre joué est juste ou non.
Si la lettre n'est pas juste on perd 1 essais sinon on continu
La fonction vérifie à la fin le cas d'une victoire (toutes les lettres trouvées)
ou d'une défaite (le nombre d'essais est à 0)
"""

#Cette fonction prend la lettre entrée par l'utilisateur en entrée et n'a pas de sorties
def macro_jouer(lettre):
    global mots,table_lettres,mots_inter,essais,lettre_jeu,table_images,fen_jeux,img_file,val_score
    global score_inter
    
    if lettre_joue(lettre.upper(),lettre_jeu) == False:
        essais,lettre_jeu = jouer(lettre,mots,table_lettres,essais,mots_inter,lettre_jeu)
        print(essais.get())
        print(lettre_jeu)
        
        """
        partie changement de l'image non fonctionnelle
        img_file = table_images[essais.get()-1]
        can.delete('all')
        print(img_file)
        image=PhotoImage(file=img_file)
        can.create_image(150, 150, image=image)
        can.config(height = image.height(),width = image.width())
        """

    else:
        print("Lettre déjà jouée")
        print(essais.get())
    
    if verif_victoire(table_lettres):
        #ajout d'un label "Vous avez gagné !" lorsque l'utilisateur a gagné
        txt_lettre=Label(fen_jeux, text="Vous avez gagné !")
        txt_lettre.grid(row=2, column=1, columnspan=2)
        val_score = switch_score()
        score_inter.set("Score : "+str(val_score))
    elif essais.get()==0:
        #ajout d'un label "Perdu..." lorsque l'utilisateur a perdu
        txt_lettre=Label(fen_jeux, text="Perdu...")
        txt_lettre.grid(row=2, column=1, columnspan=2)


"""INITIALISATION DES VARIABLES :"""
#définition d'une table permettant de changer l'image durant la partie
table_images=[]
for i in range(8): #8 car 8 essais
    table_images.append('images/bonhomme'+str(i+1)+'.gif')

img_file = table_images[7] #initialisation de la première image à afficher (bonhomme8)

"""
initialisation du jeux
    1) choisie un mot au hasard (qu'on enregistre dans mots)
    2) on initialise la table de lettre du mot (dans table_lettres)
    3) modifie ce mot pour le cacher (qu'on enregistre dans mots_jeux)
    4) on initialise la table de lettres déjà trouvées (dans lettre_jeu)
    5) on récupère la valeur du score actuel
"""
mots,table_lettres=choix_mots('mots_sort.txt')
mots_jeux=mots_cache(mots,table_lettres)
lettre_jeu=[] #table des lettres jouées durant une partie
print("Mots joué :",mots)
val_score = open('score.txt').readline().split(":")
val_score=int(val_score[1][1])
print(val_score)

"""CREATION DE L'INTERFACE :"""
#Création de la fenêtre
fen_jeux = Tk()

#Bar de menu
menubar=Menu(fen_jeux)
menu_action= Menu(menubar,tearoff=0)
menu_action.add_command(label="Quitter",command=fen_jeux.destroy)
menu_action.add_command(label="Mettre à jour les mots",command=lambda:sort_fichier('mots.txt','mots_sort.txt'))
menubar.add_cascade(label="Menu",menu=menu_action)

#Wigget interface
mots_inter=StringVar()
mots_inter.set(mots_jeux)
score_inter=IntVar()
score_inter.set("Score : "+str(val_score))
essais = IntVar()
essais.set(8)
lbl_mots=Label(fen_jeux, textvariable=mots_inter)
txt_lettre=Entry(fen_jeux)
bouton_jouer = Button(fen_jeux, text="Proposer", fg='black', command=lambda:macro_jouer(txt_lettre.get()))
bouton_recommencer = Button(fen_jeux, text="Recommencer", fg='black', command=macro_recommencer)
can = Canvas(fen_jeux, width=300, height=300, bg='white')
Image_pendu = PhotoImage(file=img_file)
can.create_image(150, 150, image=Image_pendu)
can.grid(row=1, rowspan=4, column=3)
lbl_score=Label(fen_jeux, textvariable=score_inter)

#Mise en forme de l'interface à l'aide d'un grid
fen_jeux.title("Jeux du pendu")
fen_jeux.config(menu=menubar)
lbl_mots.grid(row=1, column=1, columnspan=2)
txt_lettre.grid(row=2, column=1, columnspan=2)
bouton_jouer.grid(row=3, column=1)
bouton_recommencer.grid(row=3, column=2)
lbl_score.grid(row=4,column=1,columnspan=2)

#lancement de la fenêtre
fen_jeux.mainloop()