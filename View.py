#!/usr/bin/python
#Projet_test_2
# -*- coding: utf-8 -*-

from PyQt4.QtGui import *
from PyQt4.QtCore import *
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
		
		#Création bar recherche
		lineEditSearch = QLineEdit()
		lineEditSearch.setPlaceholderText("Nom, Prénom, Mail")
		lineEditSearch.setStyleSheet("background-color:white")
		toolBar.addWidget(lineEditSearch)
		lineEditSearch.setMaximumWidth(300)
		
		#Création icon search
		actionSearch = toolBar.addAction("Rechercher")
		actionSearch.setIcon(QIcon("Pictures/person1.png"))
		
		
		#Création icon add contact
		actionAdd = toolBar.addAction("Ajouter")
		actionAdd.setIcon(QIcon("Pictures/sign.png"))
		
		#Création icon delete contact
		actionDelete = toolBar.addAction("Supprimer")
		actionDelete.setIcon(QIcon("Pictures/contacts.png"))
		
		#Création widget central
		centralWidget = QWidget(self)
		centralWidget.setStyleSheet("background-color:white")
		self.setCentralWidget(centralWidget)
		centralLayout = QGridLayout()
		button = QPushButton("Patron")
		centralLayout.addWidget(button)
		centralWidget.setLayout(centralLayout)
		
		#Création dockWidget left
		dockDisplay = QDockWidget("Répertoire",self)
		dockDisplay.setStyleSheet("background-color:white")
		dockDisplay.setFeatures(QDockWidget.DockWidgetFloatable)
		dockDisplay.setAllowedAreas(Qt.LeftDockWidgetArea | 
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
		listContact = list()
		listContact.append("Axel Camara")
		listContact.append("Marine Bandeira")
		listContact.append("Cyril Monti")
		listContact.append("Kevin Engel")
		listContact.append("Samuel Camara")
		listContact.append("Tommy Guillot")
		listContact.append("Léo Cochin")		
		listContact.append("Léo Cochin")
		listContact.append("Léo Cochin")
		listContact.append("Léo Cochin")
		listContact.append("Léo Cochin")
		listContact.append("Léo Cochin")
		listContact.append("Léo Cochin")
		listContact.append("Léo Cochin")
		model = QStringListModel(listContact)
		listView = QListView()
		listView.setModel(model)
		displayWidget.setWidget(listView)
		
		
	def connectWidgets(self) :
		pass
		
		#Afficher une liste :
		#QStringList numbers;
 		#numbers << "One" << "Two" << "Three" << "Four" << "Five";
 
 		#QAbstractItemModel *model = new StringListModel(numbers);
 		#QListView *view = new QListView;
 		#view->setModel(model);
		#view->show();
		
		
		
