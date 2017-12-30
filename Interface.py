# coding: utf-8

from tkinter import *
from tkinter.messagebox import *

class Interface:
    def __init__(self, master, liste_regles) :
        self.master = master
        self.master.geometry("690x300")
        self.master.wm_title("Stack Renamer")
        self.drawMenubar()
        self.makeCreateFrame()

    def disable(self):
        self.entry_nom_fichier.config(state="disabled")

    def enable(self):
        self.entry_nom_fichier.config(state="normal")

    def lister(self):
        self.frame_up.destroy()
        self.frame_down.destroy()
        self.makeListFrame()

    def renommer(selfself):
        return 0

    def check_amorce(self,amorce):
        if(amorce == "Aucune"):
            self.entry_a_partir_de.config(state="disabled")
        else:
            self.entry_a_partir_de.config(state="normal")

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
        self.partieExtension()

    def makeListFrame(self):
        self.mainComponents()
        self.drawLogo("test")
        self.partieAmorce()
        self.partiePrefixe()
        self.partieNomFichier()

    def alert(self):
        showinfo("A propos","StackRenamer v1.0\nDéveloppé par : Arthur DESCHAUD\n")

    def drawMenubar(self):
        self.menubar = Menu(self.master)

        self.menu1 = Menu(self.menubar, tearoff=0)
        self.menu1.add_command(label="Lister", command=self.lister)
        self.menu1.add_command(label="Créer", command=self.creer)
        self.menubar.add_cascade(label="Règles", menu=self.menu1)

        self.menu2 = Menu(self.menubar, tearoff=0)
        self.menu2.add_command(label="A propos", command=self.alert)
        self.menubar.add_cascade(label="?", menu=self.menu2)

        self.master.config(menu=self.menubar)

    def mainComponents(self):
        self.frame_up = Frame(self.master)
        self.frame_up.pack(side=TOP)
        self.frame_down = Frame(self.master)
        self.frame_down.pack(side=TOP)

    def selectionRepertoire(self):
        self.label_nom_repertoire = Label(self.frame_up, text="Nom de répertoire")
        self.label_nom_repertoire.pack(side=LEFT, padx=15)
        self.frame_renommer_en_lot = Frame(self.frame_up)
        self.frame_renommer_en_lot.pack(side=LEFT, padx=15)
        self.label_renommer_en_lot = Label(self.frame_renommer_en_lot, text="Renommer en lot")
        self.label_renommer_en_lot.pack(side=TOP)
        self.nom_repertoire = StringVar()
        self.entry_nom_repertoire = Entry(self.frame_renommer_en_lot, textvariable=self.nom_repertoire)
        self.entry_nom_repertoire.pack(side=LEFT)


    def drawLogo(self,image_path):
        self.image = PhotoImage(file='assets/logov2_tp.png')
        self.label_image = Label(self.frame_up, image=self.image)
        self.label_image.pack(side=LEFT,pady=15,padx=25)

    def partieAmorce(self):
        self.frame_amorce = Frame(self.frame_down)
        self.frame_amorce.pack(side=LEFT, padx=15, pady=15, fill=Y, expand=1)
        self.label_amorce = Label(self.frame_amorce, text="Amorce")
        self.label_amorce.pack(side=TOP)
        self.amorce = StringVar()
        self.amorce.set("Aucune")
        self.optionmenu_amorce = OptionMenu(self.frame_amorce, self.amorce, "Aucune", "Lettre", "Chiffre",command=self.check_amorce)
        self.optionmenu_amorce.pack()
        self.label_a_partir_de = Label(self.frame_amorce, text="A partir de")
        self.label_a_partir_de.pack()
        self.a_partir_de = StringVar()
        self.entry_a_partir_de = Entry(self.frame_amorce, textvariable=self.a_partir_de)
        self.entry_a_partir_de.config(state="disabled")
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
        self.frame_nom_fichier.pack(side=LEFT, padx=15, pady=15,fill=BOTH)
        self.label_nom_fichier = Label(self.frame_nom_fichier, text="Nom du fichier")
        self.label_nom_fichier.pack(side=TOP,padx=30)
        self.value = StringVar()
        self.value.set(1)
        self.radiobutton_nom_original = Radiobutton(self.frame_nom_fichier, text="Nom original", variable=self.value, value=1, command=self.disable)
        self.radiobutton_nom_original.place(x=0,y=18)
        self.radiobutton_nom_fichier = Radiobutton(self.frame_nom_fichier, variable=self.value, value=2, command=self.enable)
        self.radiobutton_nom_fichier.place(x=0,y=45)
        self.nom_fichier = StringVar()
        self.entry_nom_fichier = Entry(self.frame_nom_fichier, textvariable=self.nom_fichier)
        self.entry_nom_fichier.config(state="disabled")
        self.entry_nom_fichier.place(x=22,y=47)

    def partieExtension(self):
        self.frame_extension = Frame(self.frame_down)
        self.frame_extension.pack(side=LEFT, padx=15, pady=15,fill=BOTH)
        self.label_extension = Label(self.frame_extension, text="Extension concernée")
        self.label_extension.pack(side=TOP)
        self.extension = StringVar()
        self.entry_extension = Entry(self.frame_extension,textvariable=self.extension)
        self.entry_extension.pack()
        self.button_renommer = Button(self.frame_extension, text="Renommer", command=self.renommer)
        self.button_renommer.pack(side=BOTTOM)