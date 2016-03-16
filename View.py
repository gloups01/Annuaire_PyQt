#!/usr/bin/python
#Projet_test_2
# -*- coding: utf-8 -*-

from PyQt4.QtGui import *
from PyQt4.QtCore import *
from PyQt4 import QtCore
import sys

class View(QMainWindow) :
	mySignal = pyqtSignal(QListWidget)

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
		
		#Création bar recherche
		self.lineEditSearch = QLineEdit()
		self.lineEditSearch.setPlaceholderText("Recherche")
		self.lineEditSearch.setStyleSheet("background-color:white")
		toolBar.addWidget(self.lineEditSearch)
		self.lineEditSearch.setMaximumWidth(300)
		
		#Création séparateur
		toolBar.addSeparator()
		
		#Création icon add contact
		self.actionAdd = QAction("Ajouter (Ctrl+P)",self)
		toolBar.addAction(self.actionAdd)
		self.actionAdd.setShortcut("Ctrl+P")
		self.actionAdd.setIcon(QIcon("Pictures/sign.png"))
		
		#Création icon delete contact
		actionDelete = toolBar.addAction("Supprimer (DEL)")	
		actionDelete.setShortcut("DEL")
		actionDelete.setIcon(QIcon("Pictures/contacts.png"))
		
		#Création icon quit
		self.actionQuitter = QAction("Quitter (Ctrl+Q)",self)
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
		"""Fonction donner à la QAction "Ajouter" de la toolbar"""
		
		#Label prénom/nom
		labelPictureContact = QLabel()	
		pictureContact = QPixmap("Pictures/avatar.png")
		labelPictureContact.setPixmap(pictureContact)
		
		#Ajouter prénom
		nameEdit = QLineEdit()
		nameEdit.setMaximumWidth(200)
		nameEdit.setPlaceholderText("Entrez le prénom")
		
		#Ajouter nom
		lastnameEdit = QLineEdit()
		lastnameEdit.setMaximumWidth(200)
		lastnameEdit.setPlaceholderText("Entrez le nom")
		#layout nom/prénom
		layoutContact = QVBoxLayout()
		layoutContact.setSpacing(10)
		layoutContact.addWidget(nameEdit)
		layoutContact.addWidget(lastnameEdit)
		
		#Label numéro
		labelPictureMobile = QLabel()
		pictureMobile = QPixmap("Pictures/mobile.png")
		labelPictureMobile.setPixmap(pictureMobile)
		
		#Ajouter numéro
		mobileEdit = QLineEdit()
		mobileEdit.setMaximumWidth(200)
		mobileEdit.setPlaceholderText("Entrez le numéro")
		
		#Label adresse
		labelPictureLocation = QLabel()
		pictureLocation = QPixmap("Pictures/web.png")
		labelPictureLocation.setPixmap(pictureLocation)
		
		#Ajouter adresse
		locationEdit = QLineEdit()
		locationEdit.setMaximumWidth(200)
		locationEdit.setPlaceholderText("Entrez l'adresse")
		
		#boutton ajouter
		addButton = QPushButton()
		addButton.setStyleSheet("background-image : url('Pictures/add.png')")
		addButton.setFixedWidth(38)
		addButton.setFixedHeight(38)
		#layout boutton
		layoutAddButton = QVBoxLayout()
		layoutAddButton.addStretch(100)
		layoutAddButton.addWidget(addButton)
	
		#Layout pour le formulaire
		layoutForm = QFormLayout()
		layoutForm.setHorizontalSpacing(30)
		layoutForm.setVerticalSpacing(30)
		layoutForm.setFormAlignment(Qt.AlignCenter)
		layoutForm.setLabelAlignment(Qt.AlignRight)
		layoutForm.addRow(labelPictureContact,layoutContact)
		layoutForm.addRow(labelPictureMobile,mobileEdit)		
		layoutForm.addRow(labelPictureLocation,locationEdit)	
		
		#Layout central
		layoutCentral = QGridLayout()
		layoutCentral.addLayout(layoutForm,0,0)  
		layoutCentral.addLayout(layoutAddButton,0,1)        
		self.centralWidget.setLayout(layoutCentral)
		
		
	def connectWidgets(self) :
		self.connect(self.actionQuitter,
			QtCore.SIGNAL("triggered()"),self, QtCore.SLOT('close()'))
			
		self.connect(self.actionAdd,QtCore.SIGNAL("triggered()"), 
			self.widgetFormulaire)
		self.addButton.clicked.connect(self.clickHandler)
		
	def clickHandler(self):
		self.mySignal.emit(self.listContact)
		
		
		
		
		
