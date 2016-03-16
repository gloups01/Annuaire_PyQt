#!/usr/bin/python
# -*- coding: utf-8 -*-

from PyQt4.QtGui import *
from PyQt4.QtCore import *
import sqlite3
import sys

class Model :
	def __init__(self) :
		self.db = sqlite3.connect('DataBase.db')
		self.createDatabase()
		

	def createDatabase(self):
		#création et remplissage de la database
		cursor = self.db.cursor()

		 
		cursor.execute("""
		DROP TABLE IF EXISTS contacts
		""")

		cursor.execute("""
		CREATE TABLE contacts(
			name TEXT NOT NULL,
			lastName TEXT NOT NULL,
			number TEXT NOT NULL,
			adress TEXT NOT NULL,
			CONSTRAINT name_unique UNIQUE (name, lastName)
			);
		""")
		cursor.execute("""INSERT INTO contacts(name, lastName, number, adress) 
							VALUES(?,?,?,?)""",("Richard", "Latan","0123456789",
							"01 rue de l'Egalite"))
            
		cursor.execute("""INSERT INTO contacts(name, lastName, number, adress) 
							VALUES(?,?,?,?)""",("Jean", "Aymarre","0612345678",
							"01 rue de la Fraternité"))

		cursor.execute("""INSERT INTO contacts(name, lastName, number, adress) 
							VALUES(?,?,?,?)""",("Claire", "Fontaine","0213456598",
							"01 rue de la Liberté"))

		cursor.execute("""INSERT INTO contacts(name, lastName, number, adress) 
							VALUES(?,?,?,?)""",("Jennifer", "Arepasser","0345678941",
							"01 rue de la Linéarité"))

		cursor.execute("""INSERT INTO contacts(name, lastName, number, adress) 
							VALUES(?,?,?,?)""",("Marc", "Okette","07451289456",
							"01 avenue Bonbonville"))
        	
		cursor.execute("""INSERT INTO contacts(name, lastName, number, adress) 
							VALUES(?,?,?,?)""",("Kevin", "Tage","0123456543",
							"Massachussetts"))
            
		cursor.execute("""INSERT INTO contacts(name, lastName, number, adress) 
							VALUES(?,?,?,?)""",("Paul", "Ho","04788856123",
							"Australie"))

		cursor.execute("""INSERT INTO contacts(name, lastName, number, adress) 
							VALUES(?,?,?,?)""",("Madame", "Gourmande","0224569887",
							"45 boulevard de ChocolateTown"))

		cursor.execute("""INSERT INTO contacts(name, lastName, number, adress) 
							VALUES(?,?,?,?)""",("Monsieur", "Colère","0635646897",
							"78 chemin de la Route"))

		cursor.execute("""INSERT INTO contacts(name, lastName, number, adress) 
							VALUES(?,?,?,?)""",("Madame", "Coquette","07454189456",
							"21 allée de Guillaume"))    

		cursor.execute("""
		SELECT name, lastName FROM contacts""")
		self.person = cursor.fetchall()
		self.db.commit()
    
	def affichage(self):
		cursor = self.db.cursor()
		cursor.execute("""SELECT name, lastName FROM contacts""")
		self.person = cursor.fetchall()
		self.db.commit()
		self.listContact.clear()
		for row in self.person:
		    self.listContact.addItem(row[0]+" "+row[1])
		
		    
	def supprimer(self, args):
		self.args = args
		contact = args.selectedItems()[0].text()
		item = contact.split()
		cursor = self.db.cursor()
		cursor.execute("""DELETE FROM contacts WHERE name = ? AND lastName = ? """
								, (item[0],item[1]) )
		self.db.commit()
		self.affichage()
		
	def ajouter(self):
		try:
		    contactName = self.nameEdit.text()
		    contactLName = self.lastnameEdit.text()
		    contactMobile = self.mobileEdit.text()
		    contactLocation = self.locationEdit.text()
		    cursor = self.db.cursor()
		    cursor.execute(""" INSERT INTO contacts(name,lastName,number,adress) 
		    					VALUES(?,?,?,?)""",
		    					(contactName,contactLName,contactMobile,contactLocation))
		    self.db.commit()
		    self.affichage()
		except sqlite3.IntegrityError:
		    QMessageBox.warning(self, "Erreur", "Ce contact existe déjà !!")


