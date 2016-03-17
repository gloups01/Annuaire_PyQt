#!/usr/bin/python
#Projet_test_2
# -*- coding: utf-8 -*-

from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import QMainWindow
from PyQt5.QtCore import *
from View import *
from Model import *
from Control import *
import sys

def main(args) :

	app = QApplication(args)
	
	view = View()
	model = Model()
	control = Control(view,model)
	
	view.show()
	
	app.exec_()
	
if __name__ == "__main__" :
	main(sys.argv)
