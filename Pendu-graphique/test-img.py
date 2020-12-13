#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Dec 13 15:55:37 2020

@author: lemarie
"""

from tkinter import Tk, Label, Entry, Canvas, PhotoImage, Button, Menu, StringVar, IntVar


def img_change():
    global can
    can.delete("all")
    new_img=PhotoImage(file='images/bonhomme5.gif')
    can.create_image(150, 150, image=new_img)
    can.pack()
    
    
fen_jeux = Tk()
can = Canvas(fen_jeux, width=300, height=300, bg='white')
Image_pendu = PhotoImage(file='images/bonhomme3.gif')
can.create_image(150, 150, image=Image_pendu)
bouton = Button(fen_jeux, text="changer", fg='black', command=img_change)

can.pack()
bouton.pack()

fen_jeux.mainloop()