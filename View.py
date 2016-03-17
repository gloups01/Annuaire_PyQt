#!/usr/bin/python
#Projet_test_2
# -*- coding: utf-8 -*-

from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QPushButton, QLineEdit, QListWidget, QTextBrowser, QMessageBox,  QLabel, QGridLayout, QFormLayout, QAction
from PyQt5.QtCore import *
from PyQt5.QtWidgets import QDockWidget, QVBoxLayout, QScrollArea
from PyQt5.QtGui import QIcon, QPixmap
from PyQt5 import QtCore
import sys
import sip

class View(QMainWindow) :
	signalAdd = pyqtSignal(QMainWindow)
	signalButton = pyqtSignal()
	signalWidget = pyqtSignal(QMainWindow)
	signalDelete = pyqtSignal(QListWidget,QMainWindow)
	signalDisplay = pyqtSignal(QMainWindow)
	signalSearch = pyqtSignal(QMainWindow)
	signalModify = pyqtSignal(QMainWindow)

	def __init__(self):
		
		QMainWindow.__init__(self)	
		self.setWindowOpacity(0.98)
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
		self.actionDelete = QAction("supprimer (Ctrl+D)",self)
		toolBar.addAction(self.actionDelete)	
		self.actionDelete.setShortcut("Ctrl+D")
		self.actionDelete.setIcon(QIcon("Pictures/contacts.png"))
		
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
		
		if (self.centralWidget.layout()) :
			sip.delete(self.centralWidget.layout())
			
		#Label prénom/nom
		labelPictureContact = QLabel()	
		pictureContact = QPixmap("Pictures/avatar.png")
		labelPictureContact.setPixmap(pictureContact)
		
		#Ajouter prénom
		self.nameEdit = QLineEdit()
		self.nameEdit.setMaximumWidth(250)
		self.nameEdit.setPlaceholderText("Entrez le prénom")
		
		#Ajouter nom
		self.lastnameEdit = QLineEdit()
		self.lastnameEdit.setMaximumWidth(250)
		self.lastnameEdit.setPlaceholderText("Entrez le nom")
		#layout nom/prénom
		layoutContact = QVBoxLayout()
		layoutContact.setSpacing(10)
		layoutContact.addWidget(self.nameEdit)
		layoutContact.addWidget(self.lastnameEdit)
		
		#Label numéro
		labelPictureMobile = QLabel()
		pictureMobile = QPixmap("Pictures/mobile.png")
		labelPictureMobile.setPixmap(pictureMobile)
		
		#Ajouter numéro
		self.mobileEdit = QLineEdit()
		self.mobileEdit.setMaximumWidth(250)
		self.mobileEdit.setPlaceholderText("Entrez le numéro")
		
		#Label mail
		labelPictureMail = QLabel()
		pictureMail = QPixmap("Pictures/mail.png")
		labelPictureMail.setPixmap(pictureMail)
		
		#Ajouter mail
		self.mailEdit = QLineEdit()
		self.mailEdit.setMaximumWidth(250)
		self.mailEdit.setPlaceholderText("Entrez le mail")
		
		
		#Label adresse
		labelPictureLocation = QLabel()
		pictureLocation = QPixmap("Pictures/web.png")
		labelPictureLocation.setPixmap(pictureLocation)
		
		#Ajouter adresse
		self.locationEdit = QLineEdit()
		self.locationEdit.setMaximumWidth(250)
		self.locationEdit.setPlaceholderText("Entrez l'adresse")
		
		#boutton ajouter
		self.addButton = QPushButton()
		self.addButton.setStyleSheet("background-image : url('Pictures/add.png')")
		self.addButton.setFixedWidth(38)
		self.addButton.setFixedHeight(38)
		self.addButton.clicked.connect(self.clickHandlerAdd)
		#layout boutton
		layoutAddButton = QVBoxLayout()
		layoutAddButton.addStretch(100)
		layoutAddButton.addWidget(self.addButton)
	
		#Layout pour le formulaire
		layoutForm = QFormLayout()
		layoutForm.setHorizontalSpacing(30)
		layoutForm.setVerticalSpacing(30)
		layoutForm.setFormAlignment(Qt.AlignCenter)
		layoutForm.setLabelAlignment(Qt.AlignRight)
		layoutForm.addRow(labelPictureContact,layoutContact)
		layoutForm.addRow(labelPictureMobile,self.mobileEdit)
		layoutForm.addRow(labelPictureMail,self.mailEdit)		
		layoutForm.addRow(labelPictureLocation,self.locationEdit)	
		
		#Layout central
		self.layoutCentral = QGridLayout()
		self.layoutCentral.addLayout(layoutForm,0,0)  
		self.layoutCentral.addLayout(layoutAddButton,0,1)        
		self.centralWidget.setLayout(self.layoutCentral)
	
	def widgetDetail(self) :
		if (self.centralWidget.layout()) :
			sip.delete(self.centralWidget.layout())
			
		#Label prénom/nom
		dLabelPictureContact = QLabel()	
		dPictureContact = QPixmap("Pictures/avatar.png")
		dLabelPictureContact.setPixmap(dPictureContact)
		
		#Ajouter prénom
		self.dNameEdit = QLineEdit()
		self.dNameEdit.setMaximumWidth(250)
		#self.dNameEdit.setPlaceholderText("Entrez le prénom")
		self.dNameEdit.setText(self.listContact.selectedItems()[0].text())
		
		#Ajouter nom
		self.dLastnameEdit = QLineEdit()
		self.dLastnameEdit.setMaximumWidth(250)
		self.dLastnameEdit.setPlaceholderText("Entrez le nom")
		#layout nom/prénom
		dLayoutContact = QVBoxLayout()
		dLayoutContact.setSpacing(10)
		dLayoutContact.addWidget(self.dNameEdit)
		dLayoutContact.addWidget(self.dLastnameEdit)
		
		#Label numéro
		dLabelPictureMobile = QLabel()
		dPictureMobile = QPixmap("Pictures/mobile.png")
		dLabelPictureMobile.setPixmap(dPictureMobile)
		
		#Ajouter numéro
		self.dMobileEdit = QLineEdit()
		self.dMobileEdit.setMaximumWidth(250)
		self.dMobileEdit.setPlaceholderText("Entrez le numéro")
		
		#Label mail
		dLabelPictureMail = QLabel()
		dPictureMail = QPixmap("Pictures/mail.png")
		dLabelPictureMail.setPixmap(dPictureMail)
		
		#Ajouter mail
		self.dMailEdit = QLineEdit()
		self.dMailEdit.setMaximumWidth(250)
		self.dMailEdit.setPlaceholderText("Entrez le mail")
		
		#Label adresse
		dLabelPictureLocation = QLabel()
		dPictureLocation = QPixmap("Pictures/web.png")
		dLabelPictureLocation.setPixmap(dPictureLocation)
		
		#Ajouter adresse
		self.dLocationEdit = QLineEdit()
		self.dLocationEdit.setMaximumWidth(250)
		self.dLocationEdit.setPlaceholderText("Entrez l'adresse")
		
		#boutton delete
		self.editButton = QPushButton()
		self.editButton.setStyleSheet("background-image : url('Pictures/edit.png')")
		self.editButton.setFixedWidth(38)
		self.editButton.setFixedHeight(38)
		self.editButton.clicked.connect(self.clickHandlerModify)

		#layout boutton
		dLayoutAddButton = QVBoxLayout()
		dLayoutAddButton.addStretch(100)
		dLayoutAddButton.addWidget(self.editButton)	
	
		#Layout pour le formulaire
		dLayoutForm = QFormLayout()
		dLayoutForm.setHorizontalSpacing(30)
		dLayoutForm.setVerticalSpacing(30)
		dLayoutForm.setFormAlignment(Qt.AlignCenter)
		dLayoutForm.setLabelAlignment(Qt.AlignRight)
		dLayoutForm.addRow(dLabelPictureContact,dLayoutContact)
		dLayoutForm.addRow(dLabelPictureMobile,self.dMobileEdit)	
		dLayoutForm.addRow(dLabelPictureMail,self.dMailEdit)	
		dLayoutForm.addRow(dLabelPictureLocation,self.dLocationEdit)	
		
		#Layout central
		dLayoutCentral = QGridLayout()
		dLayoutCentral.addLayout(dLayoutForm,0,0)  
		dLayoutCentral.addLayout(dLayoutAddButton,0,1)        
		self.centralWidget.setLayout(dLayoutCentral)
		
		self.signalDisplay.emit(self)
	
	def existButton(self) :
		self.signalButton.emit()
	
	def clickHandlerModify(self) :
		self.signalModify.emit(self)
	
	def clickHandlerDisplay(self) :
		self.signalDisplay.emit(self)
		
	def clickHandlerAdd(self):
		self.signalAdd.emit(self)
	
	def clickHandlerSearch(self) :
		self.signalSearch.emit(self)
		
	def clickHandlerDelete(self):
		self.signalDelete.emit(self.listContact,self)
		
	def connectWidgets(self) :
		self.actionQuitter.triggered.connect(self.close)
			
		self.actionAdd.triggered.connect(self.existButton)
			
		self.actionAdd.triggered.connect(self.widgetFormulaire)
			
		self.actionDelete.triggered.connect(self.clickHandlerDelete)
		
		self.listContact.itemClicked.connect(self.widgetDetail)
		
		self.lineEditSearch.textEdited.connect(self.clickHandlerSearch)

		#self.editButton.triggered.connect(self.clickHandlerModify)
		

