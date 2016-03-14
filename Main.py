#!/usr/bin/python
#Projet_test_2
# -*- coding: utf-8 -*-

from PyQt4.QtGui import *
from PyQt4.QtCore import *
from View import *
import sys

def main(args) :

	app = QApplication(args)
	
	view = View()
	
	view.show()
	
	app.exec_()
	
if __name__ == "__main__" :
	main(sys.argv)
