#!/usr/bin/python
#Projet_test_2
# -*- coding: utf-8 -*-

from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QPushButton, QLineEdit, QListWidget, QTextBrowser, QMessageBox,  QLabel, QGridLayout, QFormLayout, QAction
from PyQt5.QtCore import *
from PyQt5.QtWidgets import QDockWidget, QVBoxLayout, QScrollArea
from PyQt5.QtGui import QIcon, QPixmap, QFont
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
	signalUnlock = pyqtSignal()

	def __init__(self):
		
		QMainWindow.__init__(self)	
		self.setWindowOpacity(0.98)
		self.setWindowIcon(QIcon("Pictures/telephone.png"))	
		self.resize(700,500)
		self.setWindowTitle("Annuaire")
		self.setStyleSheet("background-color:pink")
		self.activeLayout = 0
		self.activeButtonAdd = 0
		self.activeButtonEdit = 0
		self.activeButtonSave = 0
		self.alreadyClicked = 0
		
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
		self.listContact = QListWidget()
		displayWidget.setWidget(self.listContact)
	
	def widgetFormulaire(self) :
		"""Fonction donner à la QAction "Ajouter" de la toolbar"""
		
		self.deleteWidget()
			
		#Label prénom/nom
		self.labelPictureContact = QLabel("*")	
		pictureContact = QPixmap("Pictures/avatar.png")
		self.labelPictureContact.setPixmap(pictureContact)
		
		#Ajouter prénom
		self.nameEdit = QLineEdit()
		self.nameEdit.setToolTip("Entrez un prénom sans espace")
		self.nameEdit.setMaximumWidth(250)
		self.nameEdit.setPlaceholderText("Entrez le prénom")
		
		#Ajouter nom
		self.lastnameEdit = QLineEdit()
		self.lastnameEdit.setToolTip("Entrez un nom sans espace")
		self.lastnameEdit.setMaximumWidth(250)
		self.lastnameEdit.setPlaceholderText("Entrez le nom")
		#layout nom/prénom
		layoutContact = QVBoxLayout()
		layoutContact.setSpacing(10)
		layoutContact.addWidget(self.nameEdit)
		layoutContact.addWidget(self.lastnameEdit)
		
		#Label numéro
		self.labelPictureMobile = QLabel()
		pictureMobile = QPixmap("Pictures/mobile.png")
		self.labelPictureMobile.setPixmap(pictureMobile)
		
		#Ajouter numéro
		self.mobileEdit = QLineEdit()
		self.mobileEdit.setMaxLength(10)
		self.mobileEdit.setToolTip("Entrez un numéro de 10 chiffres commencant par 0")
		self.mobileEdit.setMaximumWidth(250)
		self.mobileEdit.setPlaceholderText("Entrez le numéro")
		
		#Label mail
		self.labelPictureMail = QLabel()
		pictureMail = QPixmap("Pictures/mail.png")
		self.labelPictureMail.setPixmap(pictureMail)
		
		#Ajouter mail
		self.mailEdit = QLineEdit()
		self.mailEdit.setMaximumWidth(250)
		self.mailEdit.setPlaceholderText("Entrez le mail")
		
		
		#Label adresse
		self.labelPictureLocation = QLabel()
		pictureLocation = QPixmap("Pictures/web.png")
		self.labelPictureLocation.setPixmap(pictureLocation)
		
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
		layoutForm.addRow(self.labelPictureContact,layoutContact)
		layoutForm.addRow(self.labelPictureMobile,self.mobileEdit)
		layoutForm.addRow(self.labelPictureMail,self.mailEdit)		
		layoutForm.addRow(self.labelPictureLocation,self.locationEdit)	
		
		#Layout central
		self.layoutCentral = QGridLayout()
		self.layoutCentral.addLayout(layoutForm,0,0)  
		self.layoutCentral.addLayout(layoutAddButton,0,1)        
		self.centralWidget.setLayout(self.layoutCentral)
		
		self.activeButtonAdd = 1
		self.activeLayout = 1
	
	def widgetDetail(self) :
		self.deleteWidget()
			
		#Label prénom/nom
		self.labelPictureContact = QLabel()	
		pictureContact = QPixmap("Pictures/avatar.png")
		self.labelPictureContact.setPixmap(pictureContact)
		
		#Ajouter prénom
		self.nameEdit = QLineEdit()
		self.nameEdit.setMaximumWidth(250)
		self.nameEdit.setReadOnly(1)
		
		#Ajouter nom
		self.lastnameEdit = QLineEdit()
		self.lastnameEdit.setMaximumWidth(250)
		self.lastnameEdit.setReadOnly(1)
		#layout nom/prénom
		layoutContact = QVBoxLayout()
		layoutContact.setSpacing(10)
		layoutContact.addWidget(self.nameEdit)
		layoutContact.addWidget(self.lastnameEdit)
		
		#Label numéro
		self.labelPictureMobile = QLabel()
		pictureMobile = QPixmap("Pictures/mobile.png")
		self.labelPictureMobile.setPixmap(pictureMobile)
		
		#Ajouter numéro
		self.mobileEdit = QLineEdit()
		self.mobileEdit.setMaximumWidth(250)
		self.mobileEdit.setReadOnly(1)
		
		#Label mail
		self.labelPictureMail = QLabel()
		pictureMail = QPixmap("Pictures/mail.png")
		self.labelPictureMail.setPixmap(pictureMail)
		
		#Ajouter mail
		self.mailEdit = QLineEdit()
		self.mailEdit.setPlaceholderText("champ non renseigné")
		self.mailEdit.setMaximumWidth(250)
		self.mailEdit.setReadOnly(1)
		
		#Label adresse
		self.labelPictureLocation = QLabel()
		pictureLocation = QPixmap("Pictures/web.png")
		self.labelPictureLocation.setPixmap(pictureLocation)
		
		#Ajouter adresse
		self.locationEdit = QLineEdit()
		self.locationEdit.setMaximumWidth(250)
		self.locationEdit.setReadOnly(1)
		
		#boutton edit
		self.editButton = QPushButton()
		self.editButton.setStyleSheet("background-image : url('Pictures/edit.png')")
		self.editButton.setFixedWidth(38)
		self.editButton.setFixedHeight(38)
		self.editButton.clicked.connect(self.unlock)

		#layout boutton
		self.dLayoutAddButton = QVBoxLayout()
		self.dLayoutAddButton.addStretch(100)
		self.dLayoutAddButton.addWidget(self.editButton)	
	
		#Layout pour le formulaire
		dLayoutForm = QFormLayout()
		dLayoutForm.setHorizontalSpacing(30)
		dLayoutForm.setVerticalSpacing(30)
		dLayoutForm.setFormAlignment(Qt.AlignCenter)
		dLayoutForm.setLabelAlignment(Qt.AlignRight)
		dLayoutForm.addRow(self.labelPictureContact,layoutContact)
		dLayoutForm.addRow(self.labelPictureMobile,self.mobileEdit)	
		dLayoutForm.addRow(self.labelPictureMail,self.mailEdit)	
		dLayoutForm.addRow(self.labelPictureLocation,self.locationEdit)	
		
		#Layout central
		self.layoutCentral = QGridLayout()
		self.layoutCentral.addLayout(dLayoutForm,0,0)  
		self.layoutCentral.addLayout(self.dLayoutAddButton,0,1)        
		self.centralWidget.setLayout(self.layoutCentral)
		
		self.signalDisplay.emit(self)
		
		self.activeButtonEdit = 1
		self.activeLayout = 1
	
	def unlock(self) :
		#delete button edit
		self.layoutCentral.removeWidget(self.editButton)
		self.editButton.deleteLater()
		self.editButton = None
		self.activeButtonEdit= 0
		
		self.saveButton = QPushButton()
		self.saveButton.setStyleSheet("background-image : url('Pictures/save.png')")
		self.saveButton.setFixedWidth(38)
		self.saveButton.setFixedHeight(38)
		self.saveButton.clicked.connect(self.clickHandlerModify)
		self.activeButtonSave = 1
		
		
		self.dLayoutAddButton.addWidget(self.saveButton)
		
		self.nameEdit.setReadOnly(0)
		self.lastnameEdit.setReadOnly(0)
		self.locationEdit.setReadOnly(0)
		self.mobileEdit.setReadOnly(0)
		self.mailEdit.setReadOnly(0)
	
	def deleteWidget(self) :
		if (self.activeLayout) :
			self.activeLayout = 0
			#delete name edit
			self.layoutCentral.removeWidget(self.nameEdit)
			self.nameEdit.deleteLater()
			self.nameEdit = None
			#delete last name
			self.layoutCentral.removeWidget(self.nameEdit)
			self.lastnameEdit.deleteLater()
			self.lastnameEdit = None
			#delete label
			self.layoutCentral.removeWidget(self.labelPictureContact)
			self.labelPictureContact.deleteLater()
			self.labelPictureContact = None
			
			#delete mobileedit
			self.layoutCentral.removeWidget(self.mobileEdit)
			self.mobileEdit.deleteLater()
			self.mobileEdit = None
			#delete label
			self.layoutCentral.removeWidget(self.labelPictureMobile)
			self.labelPictureMobile.deleteLater()
			self.labelPictureMobile = None
			
			#delete mailedit
			self.layoutCentral.removeWidget(self.mailEdit)
			self.mailEdit.deleteLater()
			self.mailEdit = None
			#delete label
			self.layoutCentral.removeWidget(self.labelPictureMail)
			self.labelPictureMail.deleteLater()
			self.labelPictureMail = None
			
			if (self.activeButtonAdd) :
				#delete buttonAdd
				self.layoutCentral.removeWidget(self.addButton)
				self.addButton.deleteLater()
				self.addButton = None
				self.activeButtonAdd = 0
			
			if (self.activeButtonEdit) :
				#delete button edit
				self.layoutCentral.removeWidget(self.editButton)
				self.editButton.deleteLater()
				self.editButton = None
				self.activeButtonEdit= 0
			
			if(self.activeButtonSave) :
				#delete button save
				self.layoutCentral.removeWidget(self.saveButton)
				self.saveButton.deleteLater()
				self.saveButton = None
				self.activeButtonSave= 0
			
			#delete locationEdit
			self.layoutCentral.removeWidget(self.locationEdit)
			self.locationEdit.deleteLater()
			self.locationEdit = None
			#delete label
			self.layoutCentral.removeWidget(self.labelPictureLocation)
			self.labelPictureLocation.deleteLater()
			self.labelPictureLocation = None
			sip.delete(self.centralWidget.layout())
			
		
	def connectWidgets(self) :
		self.actionQuitter.triggered.connect(self.close)
			
		self.actionAdd.triggered.connect(self.existButton)
			
		self.actionAdd.triggered.connect(self.widgetFormulaire)
			
		self.actionDelete.triggered.connect(self.clickHandlerDelete)
		
		self.listContact.itemClicked.connect(self.widgetDetail)
		
		self.lineEditSearch.textEdited.connect(self.clickHandlerSearch)
	
	#############################################
	#SIGNAUX
	#############################################
	
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
		
