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
    
	def affichage(self,view):
		cursor = self.db.cursor()
		cursor.execute("""SELECT name, lastName FROM contacts""")
		self.person = cursor.fetchall()
		self.db.commit()
		view.listContact.clear()
		for row in self.person:
		    view.listContact.addItem(row[0]+" "+row[1])
	
	def voirDetail(self,view):
		contact = view.listeContact.selectedItems()[0].text()
		item = contact.split()
		cursor = self.db.cursor()
		cursor.execute("""SELECT * FROM contacts WHERE name = ? AND lastName = ? """, (item[0],item[1]))
		self.person = cursor.fetchall()
		self.db.commit()
		view.nameEdit.clear()
		view.lastnameEdit.clear()
		view.mobileEdit.clear()
		view.locationEdit.clear()
		for row in self.person:
			nameEdit.setText(row[0])

		    
	def supprimer(self, listContact,view):
		contact = listContact.selectedItems()[0].text()
		item = contact.split()
		cursor = self.db.cursor()
		cursor.execute("""DELETE FROM contacts WHERE name = ? AND lastName = ? """
								, (item[0],item[1]) )
		self.db.commit()
		self.affichage(view)
		
	def ajouter(self,view):
		try:
			contactName = view.nameEdit.text()
			contactLName = view.lastnameEdit.text()
			contactMobile = view.mobileEdit.text()
			contactLocation = view.locationEdit.text()
			cursor = self.db.cursor()
			cursor.execute(""" INSERT INTO contacts(name,lastName,number,adress) 
				 					VALUES(?,?,?,?)""",
				 					(contactName,contactLName,contactMobile,contactLocation))
			self.db.commit()
			self.affichage(view)
		
		except sqlite3.IntegrityError:
		    QMessageBox.warning(view, "Erreur", "Ce contact existe déjà !!")


