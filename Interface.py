# coding: utf-8

from tkinter import *

class Interface:
    def __init__(self) :
        self.fenetre = Tk()
        self.fenetre.geometry("790x420")

        self.drawMenubar()
        self.makeCreateFrame()

        self.fenetre.mainloop()

    def lister(self):
        self.frame_up.destroy()
        self.frame_down.destroy()
        self.makeListFrame()


    def creer(self):
        self.frame_up.destroy()
        self.frame_down.destroy()
        self.makeCreateFrame()

    def makeCreateFrame(self):
        self.mainComponents()
        self.selectionRepertoire()
        self.drawLogo("test")
        self.partieAmorce()
        self.partiePrefixe()
        self.partieNomFichier()

    def makeListFrame(self):
        self.mainComponents()
        self.drawLogo("test")
        self.partieAmorce()
        self.partiePrefixe()
        self.partieNomFichier()

    def drawMenubar(self):
        self.menubar = Menu(self.fenetre)
        self.menu1 = Menu(self.menubar, tearoff=0)
        self.menu1.add_command(label="Lister", command=self.lister)
        self.menu1.add_command(label="Créer", command=self.creer)
        self.menubar.add_cascade(label="Règles", menu=self.menu1)
        self.fenetre.config(menu=self.menubar)

    def mainComponents(self):
        self.frame_up = Frame(self.fenetre)
        self.frame_up.pack(side=TOP)
        self.frame_down = Frame(self.fenetre)
        self.frame_down.pack(side=TOP)

    def selectionRepertoire(self):
        self.label_nom_repertoire = Label(self.frame_up, text="Nom de répertoire")
        self.label_nom_repertoire.pack(side=LEFT, padx=15)
        self.frame_renommer_en_lot = Frame(self.frame_up)
        self.frame_renommer_en_lot.pack(side=LEFT, padx=15, pady=15)
        self.label_renommer_en_lot = Label(self.frame_renommer_en_lot, text="Renommer en lot")
        self.label_renommer_en_lot.pack(side=TOP)
        self.nom_repertoire = StringVar()
        self.entry_nom_repertoire = Entry(self.frame_renommer_en_lot, textvariable=self.nom_repertoire)
        self.entry_nom_repertoire.pack(side=BOTTOM)


    def drawLogo(self,image_path):
        self.canvas_logo = Canvas(self.frame_up, width=160, height=100, background="white")
        self.canvas_logo.pack(side=LEFT, padx=15, pady=15)

    def partieAmorce(self):
        self.frame_amorce = Frame(self.frame_down)
        self.frame_amorce.pack(side=LEFT, padx=15, pady=15, fill=Y, expand=1)
        self.label_amorce = Label(self.frame_amorce, text="Amorce")
        self.label_amorce.pack(side=TOP)
        self.amorce = StringVar()
        self.amorce.set("Aucune")
        self.optionmenu_amorce = OptionMenu(self.frame_amorce, self.amorce, "Aucune", "Lettre", "Chiffre")
        self.optionmenu_amorce.pack()
        self.label_a_partir_de = Label(self.frame_amorce, text="A partir de")
        self.label_a_partir_de.pack()
        self.a_partir_de = StringVar()
        self.entry_a_partir_de = Entry(self.frame_amorce, textvariable=self.a_partir_de)
        self.entry_a_partir_de.pack()

    def partiePrefixe(self):
        self.frame_prefixe = Frame(self.frame_down)
        self.frame_prefixe.pack(side=LEFT, padx=15, pady=15, fill=Y, expand=1)
        self.label_prefixe = Label(self.frame_prefixe, text="Préfixe")
        self.label_prefixe.pack(side=TOP)
        self.prefixe = StringVar()
        self.entry_prefixe = Entry(self.frame_prefixe, textvariable=self.prefixe)
        self.entry_prefixe.pack()

    def partieNomFichier(self):
        self.frame_nom_fichier = Frame(self.frame_down)
        self.frame_nom_fichier.pack(side=LEFT, padx=15, pady=15, fill=Y, expand=1)
        self.label_nom_fichier = Label(self.frame_nom_fichier, text="Nom du fichier")
        self.label_nom_fichier.pack(side=TOP)
        self.value = StringVar()
        self.value.set(1)
        self.radiobutton_nom_original = Radiobutton(self.frame_nom_fichier, text="Nom original", variable=self.value, value=1)
        self.radiobutton_nom_original.pack(side=TOP)
        self.radiobutton_nom_fichier = Radiobutton(self.frame_nom_fichier, variable=self.value, value=2, )
        self.radiobutton_nom_fichier.pack(side=LEFT)
        self.nom_fichier = StringVar()
        self.entry_nom_fichier = Entry(self.frame_nom_fichier, textvariable=self.nom_fichier)
        self.entry_nom_fichier.pack(side=RIGHT)

fen = Interface()
#
#
#
#
#
#
# frame_postfixe = Frame(frame_down)
# frame_postfixe.pack(expand=1, fill=Y, pady=15, padx=15)
# label_postfixe = Label(frame_postfixe, text="Postfixe")
# label_postfixe.pack()
# postfixe = StringVar()
# entry_postfixe = Entry(frame_postfixe, textvariable=postfixe)
# entry_postfixe.pack()
#
#fenetre.mainloop()