"""
import sys
from PyQt5.QtWidgets import *

class Dessin(QWidget):
	def paintEvent(self, event):
		...

def main(args):
	app=QApplication(args)
	win = QMainWindow()
	win.setCentralWidget(Dessin())
	win.resize(300,200)
	win.show()
	app.exec_()
	return 

if __name__ == '__main__':
	main(sys.argv)
"""