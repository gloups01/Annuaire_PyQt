#!/usr/bin/python
#Projet_test_2
# -*- coding: utf-8 -*-

from PyQt4.QtGui import *
from PyQt4.QtCore import *
from View import *
from Model import *
import sys

class Control :
	signalDisplay = pyqtSignal()
	
	def __init__(self,view,model) :
		self.view = view
		self.model = model
		
		self.displayContact()
		self.searchLineEdit()
		self.view.signalButton.connect(self.ajoutContact)
		self.suppContact()
		#self.detailContact()

	def searchLineEdit(self) :
		if (self.view.lineEditSearch.isModified()) :
			self.selectText = view.lineEditSearch.selectText()
			
	def displayContact(self) :
		self.model.affichage(self.view)
		
	#def detailContact(self) :
		#if (self.view.listContact.SelectedItems()) :
			
			#self.model.voirDetail(self.view)
	
	def ajoutContact(self):
		self.view.signalAdd.connect(self.model.ajouter)
		
	def suppContact(self):
		self.view.signalDelete.connect(self.model.supprimer)
	
