#!/usr/bin/python
#Projet_test_2
# -*- coding: utf-8 -*-

from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from View import *
from Model import *
import sys

class Control :
	
	def __init__(self,view,model) :
		self.view = view
		self.model = model
		
		self.displayContact()
		self.searchLineEdit()
		self.view.signalButton.connect(self.ajoutContact)
		self.view.signalDisplay.connect(self.model.displayDetail)
		self.suppContact()
		self.searchContact()

	def searchLineEdit(self) :
		if (self.view.lineEditSearch.isModified()) :
			self.selectText = view.lineEditSearch.selectText()
		
	def searchContact(self) :
		self.view.signalSearch.connect(self.model.tri)
			
	def displayContact(self) :
		self.model.affichage(self.view)
	
	def ajoutContact(self):
		self.view.signalAdd.connect(self.model.ajouter)
		
	def suppContact(self):
		self.view.signalDelete.connect(self.model.supprimer)

