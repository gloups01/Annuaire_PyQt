#!/usr/bin/python
# -*- coding: utf-8 -*-

from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
import sqlite3
import sys

class Model :
	def __init__(self) :
		self.db = sqlite3.connect('DataBase.db')
		self.createDatabase()

	def createDatabase(self):
		#création et remplissage de la database
		cursor = self.db.cursor()
		
		#cursor.execute("""DROP TABLE contacts""")

		cursor.execute("""
        CREATE TABLE IF NOT EXISTS contacts(
            name TEXT NOT NULL CHECK(name NOT LIKE '% %'),
            lastName TEXT NOT NULL CHECK(lastName NOT LIKE '% %'),
            number TEXT NOT NULL CHECK (number LIKE '%0_________%'),
            adress TEXT NOT NULL,
            email TEXT DEFAULT 'champ non renseigné',
            CONSTRAINT name_unique UNIQUE (name, lastName)
			);
			""")    

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
	
	def tri(self,view):
		contact = view.lineEditSearch.text()
		cursor = self.db.cursor()
		cursor.execute("""SELECT name,lastName FROM contacts WHERE name LIKE ? OR lastName LIKE ?""", ('%'+contact+'%','%'+contact+'%',) )
		self.person = cursor.fetchall()
		self.db.commit()
		view.listContact.clear()
		for row in self.person:
			view.listContact.addItem(row[0]+" "+row[1])	
	
	def displayDetail(self,view):
		contact = view.listContact.selectedItems()[0].text()
		item = contact.split()
		cursor = self.db.cursor()
		cursor.execute("""SELECT * FROM contacts WHERE name = ? AND lastName = ? """, (item[0],item[1]))
		self.person = cursor.fetchall()
		self.db.commit()
		for row in self.person:
                        view.dNameEdit.setText(row[0])
                        view.dLastnameEdit.setText(row[1])
                        view.dMobileEdit.setText(row[2])
                        view.dLocationEdit.setText(row[3])
                        view.dMailEdit.setText(row[4])

		    
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
			contactMail = view.mailEdit.text()
			cursor = self.db.cursor()
			cursor.execute(""" INSERT INTO contacts(name,lastName,number,adress,email) 
				 					VALUES(?,?,?,?,?)""",
				 					(contactName,contactLName,contactMobile,contactLocation,contactMail))
			self.db.commit()
			self.affichage(view)
		
		except sqlite3.IntegrityError:
		    QMessageBox.warning(view, "Erreur", "Ce contact existe déjà !!")

	'''	    

	def modifier(self,view):
		try:
                        contact = view.listContact.selectedItems()[0].text()
                        item = contact.split()
                        cursor = self.db.cursor() 
			contactName = view.dNameEdit.text()
			contactLName = view.dLastnameEdit.text()
			contactMobile = view.dMobileEdit.text()
			contactLocation = view.dLocationEdit.text()
			contactMail = view.dMailEdit.text()
			cursor.execute(""" UPDATE contacts SET name = ?, lastName = ?,number = ?,adress=?,email=?) VALUES(?,?,?,?,?) WHERE name = ? AND lastName = ? """,
				 					(contactName,contactLName,contactMobile,contactLocation,contactMail,item[0],item[1],))
			self.db.commit()
                        view.dNameEdit.setText(contactName)
                        view.dLastnameEdit.setText(contactLName)
                        view.dMobileEdit.setText(contactMobile)
                        view.dLocationEdit.setText(contactLocation)
                        view.dMailEdit.setText(contactMail)
		
		except sqlite3.IntegrityError:
		    QMessageBox.warning(view, "Erreur", "Ce contact existe déjà !!")		    
        '''

