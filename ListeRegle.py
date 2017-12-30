# coding: utf-8

from Regle import *
from configparser import *

class ListeRegle:

    def __init__(self, regles):
        self.regles = regles

    def __str__(self):
        desc = "Liste des règles :\n"
        for regle in self.regles:
            desc += str(regle)
        return desc

    def getRegles(self):
        return self.regles

    def charger(self):
        config = configparser.ConfigParser()
        config.read("stack_renamer.ini","utf-8")
        for section in config.sections() :
            amorce = config[section]["amorce"]
            apartirde = config[section]["apartirde"]
            prefixe = config[section]["prefixe"]
            nom_fichier = config[section]["nom_fichier"]
            postfixe = config[section]["postfixe"]
            extension = config[section]["extension"]
            self.regles.append(Regle(section,amorce,apartirde,prefixe,nom_fichier,postfixe,extension))
        self.regles = list(set(self.regles))

    def sauvegarder(self):
        config = configparser.ConfigParser()
        for regle in self.regles:
            nom = regle.getNom()
            config[nom] = {}
            config[nom]["amorce"] = regle.getAmorce()
            config[nom]["apartirde"] = regle.getAPartirDe()
            config[nom]["prefixe"] = regle.getPrefixe()
            config[nom]["nom_fichier"] = regle.getNomFichier()
            config[nom]["postfixe"] = regle.getPostFixe()
            config[nom]["extension"] = regle.getExtension()
        with open('stack_renamer.ini', 'w+') as configfile:
            config.write(configfile)
