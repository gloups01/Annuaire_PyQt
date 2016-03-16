#!/usr/bin/python
#Projet_test_2
# -*- coding: utf-8 -*-

from PyQt4.QtGui import *
from PyQt4.QtCore import *
import sys
from View import *
from Model import *

class Control :

	def __init__(self,view, model) :
		self.view = view
		self.model = model
		

	def searchLineEdit() :
		if (view.lineEditSearch.isModified()) :
			#Glolo a toi de bosser
			pass
	
	def ajoutContact(self):
		self.view.addButton.mySignal.connect(self.model.ajouter)

