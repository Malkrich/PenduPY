"""
Cette fonction est appelé au début du programme et permet de lancer
la fenètre pour commencer le jeux
"""

#Import des fonctions
from choix_mots import choix_mots #permet de choisir un mots au hasard dans la liste de mots
from mots_cache import mots_cache #permet d'afficher sur la console le mots avec des '_' lorsque les lettres sont cachées
from verif_lettre import verif_lettre #permet de vérifier si la lettre entrée est compris dans le mot ou non et modifie le nombre d'essais restants
from verif_victoire import verif_victoire #permet de vérifier si le mot joué a été trouvé ou non
from lettre_joue import lettre_joue #vérifie si une lettre a déjà été trouvé ou non
from switch_score import switch_score #permet de modifier le score du joueur lorsqu'il gagne
from maj_fichiertxt import sort_fichier #permet de mettre à jour le fichiers de mots dans l'ordre de taille puis par ordre alphabétique
from tkinter import Tk, Label, Entry, Canvas, PhotoImage, Button, Menu


def jouer():
    print("Jouer")

def recommencer():
    print("Recommencer")


#Cette fonction est en void, elle n'a ni entrées ni sorties
def fenetre():
    #Création de la fenêtre
    fen_jeux = Tk()
    
    #Ajout menu
    menubar=Menu(fen_jeux)
    menu_action= Menu(menubar,tearoff=0)
    menu_action.add_command(label="Quitter",command=fen_jeux.destroy)
    menubar.add_cascade(label="Action",menu=menu_action)
    
    #Ajout wigget interface
    lbl_mots=Label(fen_jeux, text='MOT')
    txt_lettre=Entry(fen_jeux)
    bouton_jouer = Button(fen_jeux, text="Jouer", fg='black', command=jouer)
    bouton_recommencer = Button(fen_jeux, text="Recommencer", fg='black', command=recommencer)
    
    can = Canvas(fen_jeux, width=300, height=300, bg='white')
    Image_pendu = PhotoImage(file='images/bonhomme1.gif')
    item_pendu = can.create_image(150, 150, image=Image_pendu)    
    can.grid(row=1, rowspan=3, column=3)

    #Mise en place de l'interface
    lbl_mots.grid(row=1, column=1, columnspan=2)
    txt_lettre.grid(row=2, column=1, columnspan=2)
    bouton_jouer.grid(row=3, column=1)
    bouton_recommencer.grid(row=3, column=2)
    
    fen_jeux.mainloop()