#!/usr/bin/python
#Projet_test_2
# -*- coding: utf-8 -*-

from PyQt4.QtGui import *
from PyQt4.QtCore import *
from View import *
import sys

class Control :

	def __init__(self,view,model) :
		self.view = view
		self.model = model
		
		self.searchLineEdit()

	def searchLineEdit(self) :
		if (self.view.lineEditSearch.isModified()) :
			self.selectText = view.lineEditSearch.selectText()
			
		
	
