import sys
from PyQt5.QtWidgets import *
from calculator import CalculatorWindow
app=QApplication(sys.argv)
Calculator=CalculatorWindow()
sys.exit(app.exec())