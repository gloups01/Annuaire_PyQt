#!/usr/bin/python
# -*- coding: utf-8 -*-

from PyQt4.QtGui import *
from PyQt4.QtCore import *
import sqlite3
import sys
from View import *

class Model :
	def __init__(self,args) :
		self.args = args
		self.db = sqlite3.connect('DataBase.db')
		self.createDatabase()
		self.affichage(args)

	def createDatabase(self):
		#création et remplissage de la database
		cursor = self.db.cursor()

		 
		cursor.execute("""
		DROP TABLE IF EXISTS contacts
		""")

		cursor.execute("""
		CREATE TABLE contacts(
			name TEXT,
			lastName TEXT,
			number INT,
			adress TEXT
			);
		""")
		 
		cursor.execute("""
		INSERT INTO contacts(name, lastName) VALUES(?,?)""",("Machin", "tac",))

		cursor.execute("""
		INSERT INTO contacts(name, lastName) VALUES(?,?)""",("Bidule", "tic",))

		cursor.execute("""
		INSERT INTO contacts(name, lastName) VALUES(?,?)""",("Monsieur", "mme",))

		cursor.execute("""
		INSERT INTO contacts(name, lastName) VALUES(?,?)""",("Maman", "truc",))

		cursor.execute("""
		INSERT INTO contacts(name, lastName) VALUES(?,?)""",("Travail", "bueno",))

		cursor.execute("""
		INSERT INTO contacts(name, lastName) VALUES(?,?)""",("Ecole", "kinder",))

		cursor.execute("""
		SELECT name, lastName FROM contacts""")
		self.person = cursor.fetchall()
		self.db.commit()
    
	def affichage(self,args):
		for row in self.person:
			self.args.listContact.addItem(row[0]+" "+row[1])

