#!/usr/bin/python
#Projet_test_2
# -*- coding: utf-8 -*-

from PyQt4.QtGui import *
from PyQt4.QtCore import *
from PyQt4 import QtCore
import sys

class View(QMainWindow) :

	def __init__(self):
		
		QMainWindow.__init__(self)	
		self.setWindowOpacity(0.9)
		self.setWindowIcon(QIcon("Pictures/telephone.png"))	
		self.resize(700,500)
		self.setWindowTitle("Annuaire")
		self.setStyleSheet("background-color:pink")
		
		self.createWidgets()
		self.connectWidgets()
		
	def createWidgets(self):
		"""Cette fonction permet la création de tous les widgets de la
		mainWindow"""
		
		#Création toolbar
		toolBar = self.addToolBar("Tools")
		toolBar.setAttribute(Qt.WA_TranslucentBackground)
		
		#Création bar recherche
		self.lineEditSearch = QLineEdit()
		self.lineEditSearch.setPlaceholderText("Nom, Prénom, Mail")
		self.lineEditSearch.setStyleSheet("background-color:white")
		toolBar.addWidget(self.lineEditSearch)
		self.lineEditSearch.setMaximumWidth(300)
		
		#Création icon search
		actionSearch = toolBar.addAction("<b>Rechercher</b> (Ctrl+J)")
		actionSearch.setShortcut("Ctrl+J")
		actionSearch.setIcon(QIcon("Pictures/person1.png"))
		
		#Création séparateur
		toolBar.addSeparator()
		
		#Création icon add contact
		self.actionAdd = QAction("<b>Ajouter</b> (Ctrl+A)",self)
		toolBar.addAction(self.actionAdd)
		actionSearch.setShortcut("Ctrl+A")
		self.actionAdd.setIcon(QIcon("Pictures/sign.png"))
		
		#Création icon delete contact
		actionDelete = toolBar.addAction("<b>Supprimer</b> (DEL)")	
		actionSearch.setShortcut("DEL")
		actionDelete.setIcon(QIcon("Pictures/contacts.png"))
		
		#Création icon quit
		self.actionQuitter = QAction("<b>&Quitter</b> (Ctrl+Q)",self)
		toolBar.addAction(self.actionQuitter)
		self.actionQuitter.setShortcut("Ctrl+Q")
		self.actionQuitter.setIcon(QIcon("Pictures/arrows.png"))
		
		#Création widget central
		self.centralWidget = QWidget()
		self.centralWidget.setStyleSheet("background-color:white")
		self.setCentralWidget(self.centralWidget)
		
		
		#Création dockWidget left
		dockDisplay = QDockWidget("Répertoire")
		dockDisplay.setStyleSheet("background-color:white")
		dockDisplay.setFeatures(QDockWidget.DockWidgetFloatable)
		dockDisplay.setAllowedAreas(Qt.LeftDockWidgetArea and 
			Qt.RightDockWidgetArea)
		self.addDockWidget(Qt.LeftDockWidgetArea,dockDisplay)
		containDock = QWidget(dockDisplay)
		dockDisplay.setWidget(containDock)
		dockLayout = QVBoxLayout()
		displayWidget = QScrollArea()
		displayWidget.setWidgetResizable(1)
		dockLayout.addWidget(displayWidget)
		containDock.setLayout(dockLayout)
		
		#Ajouter la list au dockwidget
		self.listContact = QListWidget()
		displayWidget.setWidget(self.listContact)
	
	def widgetFormulaire(self) :
		nom = QLabel('Nom')
		prenom = QLabel('Prénom')
		telephone = QLabel('Numéro de téléphone')
		adresse = QLabel('Adresse')
		couleur = QLabel('Couleur de peau xD')
		
		nomEdit = QLineEdit()
		prenomEdit = QLineEdit()
		telephoneEdit = QLineEdit()
		adresseEdit = QLineEdit()
		couleurEdit = QLineEdit()

		grid = QGridLayout()
		grid.setSpacing(2)

		grid.addWidget(nom, 1, 0)
		grid.addWidget(nomEdit, 1, 1)

		grid.addWidget(prenom, 2, 0)
		grid.addWidget(prenomEdit, 2, 1)

		grid.addWidget(adresse, 3, 0)
		grid.addWidget(adresseEdit, 3, 1)

		grid.addWidget(telephone, 4, 0)
		grid.addWidget(telephoneEdit, 4, 1)

		grid.addWidget(couleur, 5, 0)
		grid.addWidget(couleurEdit, 5, 1)

		QToolTip.setFont(QFont('SansSerif', 10))
                
		self.centralWidget.setLayout(grid)
		
		
	def connectWidgets(self) :
		self.connect(self.actionQuitter,
			QtCore.SIGNAL("triggered()"),self, QtCore.SLOT('close()'))
			
		self.connect(self.actionAdd,QtCore.SIGNAL("triggered()"), 
			self.widgetFormulaire)
		
		
		
		
		
		
		
