# coding: utf-8

import os

from App.Regle import *


class Action:
	
	def __init__(self,nomdurepertoire,regle):
		self.nomdurepertoire = nomdurepertoire
		self.regle = regle
		
	def __str__(self):
		return "desc action"
		
	def getNomDuRepertoire(self):
		return self.nomdurepertoire
	
	def setNomDuRepertoire(self,nomdurepertoire):
		self.nomdurepertoire = nomdurepertoire
		
	def getRegle(self):
		return self.regle
	
	def setRegle(self,regle):
		self.regle = regle
	
	def simule(self):
		amorce = self.regle.getAmorce()
		apartirde = self.regle.getAPartirDe()
		prefixe = self.regle.getPrefixe()
		nomfichier = self.regle.getNomFichier()
		postfixe = self.regle.getPostFixe()
		extension = self.regle.getExtension()
		if (apartirde == ""):
			if (amorce == "Chiffre"):
				apartirde = "1"
			elif (amorce == "Lettre"):
				apartirde = "A"
		if (nomfichier == ""):
			nomfichier = os.listdir(self.nomdurepertoire)[0]
		print(nomfichier)
		print(apartirde+"-"+prefixe+"-"+nomfichier+"-"+postfixe+extension)

regle1 = Regle("Aucune","","Vacances à Angoulême","nomdufichier","2017",".jpg")
regle2 = Regle("Chiffre","23","Conférence sur le pain","","042016",".jpg")

action1 = Action("E:\Documents\Developpement\Python\\renommage\\test",regle2)
action1.simule()

renommage1 = Renommage("E:\Documents\Developpement\Python\\renommage\\test",regle2)
renommage1.renommer()