##!/usr/bin/python
#Projet_test_2
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

		cursor.execute(""" CREATE TABLE IF NOT EXISTS contacts(
                                    name TEXT CHECK(name NOT LIKE '% %' AND name NOT LIKE '' ),
                                    lastName TEXT CHECK(lastName NOT LIKE '% %' AND lastName NOT LIKE '' ),
                                    number TEXT CHECK (number LIKE '0_________'),
                                    adress TEXT CHECK (adress NOT LIKE '' ),
                                    email TEXT,
                                    CONSTRAINT name_unique UNIQUE (name, lastName)
			);
			""")    
		self.db.commit()
		
    
	def display(self,view):
		cursor = self.db.cursor()
		cursor.execute("""SELECT name, lastName FROM contacts""")
		self.person = cursor.fetchall()
		self.db.commit()
		view.listContact.clear()
		for row in self.person:
		    view.listContact.addItem(row[0]+" "+row[1])
	
	def sort(self,view):
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
                        view.nameEdit.setText(row[0])
                        view.lastnameEdit.setText(row[1])
                        view.mobileEdit.setText(row[2])
                        view.locationEdit.setText(row[3])
                        view.mailEdit.setText(row[4])

		    
	def deleteContact(self, listContact,view):
		contact = listContact.selectedItems()[0].text()
		item = contact.split()
		cursor = self.db.cursor()
		cursor.execute("""DELETE FROM contacts WHERE name = ? AND lastName = ? """
								, (item[0],item[1]) )
		self.db.commit()
		self.display(view)
		listContact.item(0).setSelected(1)
		view.deleteWidget()
		QMessageBox.information(view, "Information", "Suppression réussie")
		view.widgetDetail()
		self.displayDetail(view)
		
	def addContact(self,view):
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
			self.display(view)
			
			view.nameEdit.clear()
			view.lastnameEdit.clear()
			view.mobileEdit.clear()
			view.locationEdit.clear()
			view.mailEdit.clear()
			
		
		except sqlite3.IntegrityError as e:
		    QMessageBox.warning(view, "Erreur", "Informations non valides, les champs nom, prénom, numéro et adresse sont obligatoires")

	def modify(self,view):
		try:
			contact = view.listContact.selectedItems()[0].text()
			item = contact.split()
			cursor = self.db.cursor() 
			contactName = view.nameEdit.text()
			contactLName = view.lastnameEdit.text()
			contactMobile = view.mobileEdit.text()
			contactLocation = view.locationEdit.text()
			contactMail = view.mailEdit.text()
			cursor.execute(""" UPDATE contacts SET name = ?, lastName = ?,number = ?,adress=?,email=? 
					 WHERE name = ? AND lastName = ? """,
						(contactName,contactLName,contactMobile,contactLocation,contactMail,item[0],item[1]) )

			self.db.commit()
			view.nameEdit.setText(contactName)
			view.lastnameEdit.setText(contactLName)
			view.mobileEdit.setText(contactMobile)
			view.locationEdit.setText(contactLocation)
			view.mailEdit.setText(contactMail)
			self.display(view)
			view.deleteWidget()
			view.listContact.item(0).setSelected(1)
			view.widgetDetail()
			QMessageBox.information(view, "Information", "Modification réussie")
		
		except sqlite3.IntegrityError:
		    QMessageBox.warning(view, "Erreur", "Informations non valides, les champs nom, prénom, numéro et adresse sont obligatoires")		    

