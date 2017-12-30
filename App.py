# coding: utf-8
from Interface import *
from Regle import *
from ListeRegle import *
from tkinter import *




liste_regle = ListeRegle([])
liste_regle.charger()

fenetre = Tk()

fen = Interface(fenetre, liste_regle)

fenetre.mainloop()