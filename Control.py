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
		self.view.signalButton.connect(self.addContact)
		self.view.signalDisplay.connect(self.model.displayDetail)
		self.deleteContact()
		self.searchContact()
		self.editContact()

	def searchLineEdit(self) :
		if (self.view.lineEditSearch.isModified()) :
			self.selectText = view.lineEditSearch.selectText()
		
	def searchContact(self) :
		self.view.signalSearch.connect(self.model.sort)
			
	def displayContact(self) :
		self.model.display(self.view)
	
	def addContact(self):
		self.view.signalAdd.connect(self.model.addContact)
		
	def deleteContact(self):
		self.view.signalDelete.connect(self.model.deleteContact)
	
	def editContact(self) :
		self.view.signalModify.connect(self.model.modify)

