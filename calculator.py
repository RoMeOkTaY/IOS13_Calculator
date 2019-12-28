from PyQt5 import QtWidgets
from PyQt5.QtWidgets import *
from ui_calculator import Ui_Calculator


class CalculatorWindow(QtWidgets.QMainWindow,Ui_Calculator,QPushButton):
    firstNum=None
    userisTypingSecNum=False
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.show()
        for i in range(0,10):
            self.findChild(QPushButton,"button"+str(i)).clicked.connect(self.digit_pressed)
        self.buttonvirgul.clicked.connect(self.decimal_pressed)
        self.buttonae.clicked.connect(self.artieksiyuzde)
        self.buttonyuzde.clicked.connect(self.artieksiyuzde)
        self.buttonarti.clicked.connect(self.islemler_basildi)
        self.buttoncikar.clicked.connect(self.islemler_basildi)
        self.buttoncarp.clicked.connect(self.islemler_basildi)
        self.buttonbol.clicked.connect(self.islemler_basildi)
        self.buttonarti.setCheckable(True)
        self.buttoncikar.setCheckable(True)
        self.buttoncarp.setCheckable(True)
        self.buttonbol.setCheckable(True)
        self.buttonesittir.clicked.connect(self.result)
        self.buttonclear.clicked.connect(self.cleartable)

    def digit_pressed(self):
        button=self.sender()
        
        
        if ((self.buttonarti.isChecked() or self.buttoncikar.isChecked() or
                self.buttoncarp.isChecked() or self.buttonbol.isChecked()) and (not self.userisTypingSecNum)):
            newLabel=format(float(button.text()),".15g")
            self.userisTypingSecNum=True
        else:
            if (("." in self.label.text()) and (button.text()=="0")):
                newLabel=format(self.label.text()+button.text(),".15")
            else:
                newLabel=format(float(self.label.text()+button.text()),".15g")

        self.label.setText(newLabel)


    def decimal_pressed(self):
        self.label.setText(self.label.text()+".")

    def artieksiyuzde(self):
        button=self.sender()
        labelNumber=float(self.label.text())
        if button.text()=="+/-":
            labelNumber=labelNumber*(-1)
        else:
            labelNumber=labelNumber*0.01
        
        newlabel=format(labelNumber,".15g")
        self.label.setText(newlabel)

    def islemler_basildi(self):
        button=self.sender()
        self.firstNum=float(self.label.text())
        button.setChecked(True)

        
    
    def result(self):
        secNum=float(self.label.text())
        if self.buttonarti.isChecked():
            labelNumber=self.firstNum + secNum
            newLabel=format(labelNumber,".15g")
            self.label.setText(newLabel)
            self.buttonarti.setChecked(False)
        elif self.buttoncikar.isChecked():
            labelNumber=self.firstNum - secNum
            newLabel=format(labelNumber,".15g")
            self.label.setText(newLabel)
            self.buttoncikar.setChecked(False)
        elif self.buttoncarp.isChecked():
            labelNumber=self.firstNum * secNum
            newLabel=format(labelNumber,".15g")
            self.label.setText(newLabel)
            self.buttoncarp.setChecked(False)
        elif self.buttonbol.isChecked():
            labelNumber=self.firstNum / secNum
            newLabel=format(labelNumber,".15g")
            self.label.setText(newLabel)
            self.buttonbol.setChecked(False)
        
        self.userisTypingSecNum=False
    def cleartable(self):
        self.buttonarti.setChecked(False)
        self.buttoncikar.setChecked(False)
        self.buttoncarp.setChecked(False)
        self.buttonbol.setChecked(False)

        self.userisTypingSecNum=False

        self.label.setText("0")