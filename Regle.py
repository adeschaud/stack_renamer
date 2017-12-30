# coding: utf-8

import configparser

#config = null

class Regle:
	def __init__(self,nom,amorce,apartirde,prefixe,nomfichier,postfixe,extension):
		self.nom = nom
		self.amorce = amorce
		self.apartirde = apartirde
		self.prefixe = prefixe
		self.nomfichier = nomfichier
		self.postfixe = postfixe
		self.extension = extension
		
	def __str__(self):
		desc = "=== " + self.nom + " === \n"
		desc += "Amorce : " + self.amorce + "\n"
		desc += "A partir de : " + self.apartirde + "\n"
		desc += "Préfixe : " + self.prefixe + "\n"
		desc += "Nom fichier : " + self.nomfichier + "\n"
		desc += "Postfixe : " + self.postfixe + "\n"
		desc += "Extension : " + self.extension + "\n"
		return desc

	def getNom(self):
		return self.nom

	def setNom(self, nom):
		self.nom = nom
	
	def getAmorce(self):
		return self.amorce
		
	def setAmorce(self,amorce):
		self.amorce = amorce
		
	def getAPartirDe(self):
		return self.apartirde
		
	def setAPartirDe(self,apartirde):
		self.apartirde = apartirde
	
	def getPrefixe(self):
		return self.prefixe
		
	def setPrefixe(self,prefixe):
		self.prefixe = prefixe
	
	def getNomFichier(self):
		return self.nomfichier
		
	def setNomFichier(self,nomfichier):
		self.nomfichier = nomfichier
		
	def getPostFixe(self):
		return self.postfixe
		
	def setPostFixe(self,postfixe):
		self.postfixe = postfixe
	
	def getExtension(self):
		return self.extension
		
	def setExtension(self,extension):
		self.extension = extension
		
		
class ListeRegle:
	def __init__(self,regles):
		self.regles = regles
		
	def __str__(self):
		return "description liste règles"
		
	def charger(self):
		return 1
		
	def sauvegarder(self):
		return 1
			
			