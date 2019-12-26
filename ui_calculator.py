# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'hesapmakinesi.ui'
#
# Created by: PyQt5 UI code generator 5.14.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Calculator(object):
    def setupUi(self, Calculator):
        Calculator.setObjectName("Calculator")
        Calculator.setEnabled(True)
        Calculator.resize(289, 421)
        Calculator.setStyleSheet("background-color: rgb(48, 48, 48);")
        self.centralwidget = QtWidgets.QWidget(Calculator)
        self.centralwidget.setObjectName("centralwidget")
        self.buttonyuzde = QtWidgets.QPushButton(self.centralwidget)
        self.buttonyuzde.setGeometry(QtCore.QRect(150, 60, 61, 61))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(17)
        font.setBold(False)
        font.setWeight(50)
        font.setKerning(True)
        self.buttonyuzde.setFont(font)
        self.buttonyuzde.setStyleSheet("QPushButton {\n"
"    color: #000;\n"
"    border-radius: 30px;\n"
"    border-style: outset;\n"
"    background-color: rgb(194, 194, 194);\n"
"    padding: 5px;\n"
"    }\n"
"QPushButton:hover {\n"
"background-color: rgb(232, 232, 232);\n"
"    }")
        self.buttonyuzde.setObjectName("buttonyuzde")
        self.buttonae = QtWidgets.QPushButton(self.centralwidget)
        self.buttonae.setGeometry(QtCore.QRect(80, 60, 61, 61))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(17)
        font.setBold(False)
        font.setWeight(50)
        font.setKerning(True)
        self.buttonae.setFont(font)
        self.buttonae.setStyleSheet("QPushButton {\n"
"    color: #000;\n"
"    border-radius: 30px;\n"
"    border-style: outset;\n"
"    background-color: rgb(194, 194, 194);\n"
"    padding: 5px;\n"
"    }\n"
"QPushButton:hover {\n"
"background-color: rgb(232, 232, 232);\n"
"    }")
        self.buttonae.setObjectName("buttonae")
        self.buttonbol = QtWidgets.QPushButton(self.centralwidget)
        self.buttonbol.setGeometry(QtCore.QRect(220, 60, 61, 61))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(24)
        font.setBold(False)
        font.setWeight(50)
        font.setKerning(True)
        self.buttonbol.setFont(font)
        self.buttonbol.setStyleSheet("QPushButton {\n"
"    color: #fff;\n"
"    border-radius: 30px;\n"
"    border-style: outset;\n"
"    padding: 5px;\n"
"    background-color: rgb(255, 184, 61);\n"
"    }\n"
"QPushButton:hover {background-color: rgb(255, 219, 174);\n"
"    }\n"
"\n"
"\n"
"")
        self.buttonbol.setObjectName("buttonbol")
        self.buttonclear = QtWidgets.QPushButton(self.centralwidget)
        self.buttonclear.setGeometry(QtCore.QRect(10, 60, 61, 61))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(17)
        font.setBold(False)
        font.setWeight(50)
        font.setKerning(True)
        self.buttonclear.setFont(font)
        self.buttonclear.setStyleSheet("QPushButton {\n"
"    color: #000;\n"
"    border-radius: 30px;\n"
"    border-style: outset;\n"
"    background-color: rgb(194, 194, 194);\n"
"    padding: 5px;\n"
"    }\n"
"QPushButton:hover {\n"
"background-color: rgb(232, 232, 232);\n"
"    }")
        self.buttonclear.setObjectName("buttonclear")
        self.button4 = QtWidgets.QPushButton(self.centralwidget)
        self.button4.setGeometry(QtCore.QRect(10, 200, 61, 61))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(24)
        font.setBold(False)
        font.setWeight(50)
        font.setKerning(True)
        self.button4.setFont(font)
        self.button4.setStyleSheet("QPushButton {\n"
"    color: #fff;\n"
"    border-radius: 30px;\n"
"    border-style: outset;\n"
"    background-color: rgb(99, 99, 99);\n"
"    selection-background-color: rgb(172, 172, 172);\n"
"    padding: 5px;\n"
"    }\n"
"QPushButton:hover {\n"
"background-color: rgb(135, 135, 135);\n"
"    }")
        self.button4.setObjectName("button4")
        self.button9 = QtWidgets.QPushButton(self.centralwidget)
        self.button9.setGeometry(QtCore.QRect(150, 130, 61, 61))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(24)
        font.setBold(False)
        font.setWeight(50)
        font.setKerning(True)
        self.button9.setFont(font)
        self.button9.setStyleSheet("QPushButton {\n"
"    color: #fff;\n"
"    border-radius: 30px;\n"
"    border-style: outset;\n"
"    background-color: rgb(99, 99, 99);\n"
"    selection-background-color: rgb(172, 172, 172);\n"
"    padding: 5px;\n"
"    }\n"
"QPushButton:hover {\n"
"background-color: rgb(135, 135, 135);\n"
"    }")
        self.button9.setObjectName("button9")
        self.button5 = QtWidgets.QPushButton(self.centralwidget)
        self.button5.setGeometry(QtCore.QRect(80, 200, 61, 61))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(24)
        font.setBold(False)
        font.setWeight(50)
        font.setKerning(True)
        self.button5.setFont(font)
        self.button5.setStyleSheet("QPushButton {\n"
"    color: #fff;\n"
"    border-radius: 30px;\n"
"    border-style: outset;\n"
"    background-color: rgb(99, 99, 99);\n"
"    selection-background-color: rgb(172, 172, 172);\n"
"    padding: 5px;\n"
"    }\n"
"QPushButton:hover {\n"
"background-color: rgb(135, 135, 135);\n"
"    }")
        self.button5.setObjectName("button5")
        self.button8 = QtWidgets.QPushButton(self.centralwidget)
        self.button8.setGeometry(QtCore.QRect(80, 130, 61, 61))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(24)
        font.setBold(False)
        font.setWeight(50)
        font.setKerning(True)
        self.button8.setFont(font)
        self.button8.setStyleSheet("QPushButton {\n"
"    color: #fff;\n"
"    border-radius: 30px;\n"
"    border-style: outset;\n"
"    background-color: rgb(99, 99, 99);\n"
"    selection-background-color: rgb(172, 172, 172);\n"
"    padding: 5px;\n"
"    }\n"
"QPushButton:hover {\n"
"background-color: rgb(135, 135, 135);\n"
"    }")
        self.button8.setObjectName("button8")
        self.buttoncarp = QtWidgets.QPushButton(self.centralwidget)
        self.buttoncarp.setGeometry(QtCore.QRect(220, 130, 61, 61))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(24)
        font.setBold(False)
        font.setWeight(50)
        font.setKerning(True)
        self.buttoncarp.setFont(font)
        self.buttoncarp.setAutoFillBackground(False)
        self.buttoncarp.setStyleSheet("QPushButton {\n"
"    color: #fff;\n"
"    border-radius: 30px;\n"
"    border-style: outset;\n"
"    padding: 5px;\n"
"    background-color: rgb(255, 184, 61);\n"
"    }\n"
"QPushButton:hover {background-color: rgb(255, 219, 174);\n"
"    }\n"
"\n"
"\n"
"")
        self.buttoncarp.setObjectName("buttoncarp")
        self.buttoncikar = QtWidgets.QPushButton(self.centralwidget)
        self.buttoncikar.setGeometry(QtCore.QRect(220, 200, 61, 61))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(24)
        font.setBold(False)
        font.setWeight(50)
        font.setKerning(True)
        self.buttoncikar.setFont(font)
        self.buttoncikar.setStyleSheet("QPushButton {\n"
"    color: #fff;\n"
"    border-radius: 30px;\n"
"    border-style: outset;\n"
"    padding: 5px;\n"
"    background-color: rgb(255, 184, 61);\n"
"    }\n"
"QPushButton:hover {background-color: rgb(255, 219, 174);\n"
"    }\n"
"\n"
"\n"
"")
        self.buttoncikar.setObjectName("buttoncikar")
        self.button7 = QtWidgets.QPushButton(self.centralwidget)
        self.button7.setGeometry(QtCore.QRect(10, 130, 61, 61))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(24)
        font.setBold(False)
        font.setWeight(50)
        font.setKerning(True)
        self.button7.setFont(font)
        self.button7.setStyleSheet("QPushButton {\n"
"    color: #fff;\n"
"    border-radius: 30px;\n"
"    border-style: outset;\n"
"    background-color: rgb(99, 99, 99);\n"
"    selection-background-color: rgb(172, 172, 172);\n"
"    padding: 5px;\n"
"    }\n"
"QPushButton:hover {\n"
"background-color: rgb(135, 135, 135);\n"
"    }")
        self.button7.setObjectName("button7")
        self.button6 = QtWidgets.QPushButton(self.centralwidget)
        self.button6.setGeometry(QtCore.QRect(150, 200, 61, 61))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(24)
        font.setBold(False)
        font.setWeight(50)
        font.setKerning(True)
        self.button6.setFont(font)
        self.button6.setStyleSheet("QPushButton {\n"
"    color: #fff;\n"
"    border-radius: 30px;\n"
"    border-style: outset;\n"
"    background-color: rgb(99, 99, 99);\n"
"    selection-background-color: rgb(172, 172, 172);\n"
"    padding: 5px;\n"
"    }\n"
"QPushButton:hover {\n"
"background-color: rgb(135, 135, 135);\n"
"    }")
        self.button6.setObjectName("button6")
        self.buttonvirgul = QtWidgets.QPushButton(self.centralwidget)
        self.buttonvirgul.setGeometry(QtCore.QRect(150, 340, 61, 61))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(24)
        font.setBold(False)
        font.setWeight(50)
        font.setKerning(True)
        self.buttonvirgul.setFont(font)
        self.buttonvirgul.setStyleSheet("QPushButton {\n"
"    color: #fff;\n"
"    border-radius: 30px;\n"
"    border-style: outset;\n"
"    background-color: rgb(99, 99, 99);\n"
"    selection-background-color: rgb(172, 172, 172);\n"
"    padding: 5px;\n"
"    }\n"
"QPushButton:hover {\n"
"background-color: rgb(135, 135, 135);\n"
"    }")
        self.buttonvirgul.setObjectName("buttonvirgul")
        self.button0 = QtWidgets.QPushButton(self.centralwidget)
        self.button0.setGeometry(QtCore.QRect(10, 340, 131, 61))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(24)
        font.setBold(False)
        font.setWeight(50)
        font.setKerning(True)
        self.button0.setFont(font)
        self.button0.setStyleSheet("QPushButton {\n"
"    color: #fff;\n"
"    border-radius: 30px;\n"
"    border-style: outset;\n"
"    background-color: rgb(99, 99, 99);\n"
"    selection-background-color: rgb(172, 172, 172);\n"
"    padding: 5px;\n"
"    }\n"
"QPushButton:hover {\n"
"background-color: rgb(135, 135, 135);\n"
"    }")
        self.button0.setObjectName("button0")
        self.buttonesittir = QtWidgets.QPushButton(self.centralwidget)
        self.buttonesittir.setGeometry(QtCore.QRect(220, 340, 61, 61))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(24)
        font.setBold(False)
        font.setWeight(50)
        font.setKerning(True)
        self.buttonesittir.setFont(font)
        self.buttonesittir.setStyleSheet("QPushButton {\n"
"    color: #fff;\n"
"    border-radius: 30px;\n"
"    border-style: outset;\n"
"    padding: 5px;\n"
"    background-color: rgb(255, 184, 61);\n"
"    }\n"
"QPushButton:hover {background-color: rgb(255, 219, 174);\n"
"    }\n"
"\n"
"\n"
"")
        self.buttonesittir.setObjectName("buttonesittir")
        self.buttonarti = QtWidgets.QPushButton(self.centralwidget)
        self.buttonarti.setGeometry(QtCore.QRect(220, 270, 61, 61))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(24)
        font.setBold(False)
        font.setWeight(50)
        font.setKerning(True)
        self.buttonarti.setFont(font)
        self.buttonarti.setStyleSheet("QPushButton {\n"
"    color: #fff;\n"
"    border-radius: 30px;\n"
"    border-style: outset;\n"
"    padding: 5px;\n"
"    background-color: rgb(255, 184, 61);\n"
"    }\n"
"QPushButton:hover {background-color: rgb(255, 219, 174);\n"
"    }\n"
"\n"
"\n"
"")
        self.buttonarti.setObjectName("buttonarti")
        self.button2 = QtWidgets.QPushButton(self.centralwidget)
        self.button2.setGeometry(QtCore.QRect(80, 270, 61, 61))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(24)
        font.setBold(False)
        font.setWeight(50)
        font.setKerning(True)
        self.button2.setFont(font)
        self.button2.setStyleSheet("QPushButton {\n"
"    color: #fff;\n"
"    border-radius: 30px;\n"
"    border-style: outset;\n"
"    background-color: rgb(99, 99, 99);\n"
"    selection-background-color: rgb(172, 172, 172);\n"
"    padding: 5px;\n"
"    }\n"
"QPushButton:hover {\n"
"background-color: rgb(135, 135, 135);\n"
"    }")
        self.button2.setObjectName("button2")
        self.button1 = QtWidgets.QPushButton(self.centralwidget)
        self.button1.setGeometry(QtCore.QRect(10, 270, 61, 61))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(24)
        font.setBold(False)
        font.setWeight(50)
        font.setKerning(True)
        self.button1.setFont(font)
        self.button1.setStyleSheet("QPushButton {\n"
"    color: #fff;\n"
"    border-radius: 30px;\n"
"    border-style: outset;\n"
"    background-color: rgb(99, 99, 99);\n"
"    selection-background-color: rgb(172, 172, 172);\n"
"    padding: 5px;\n"
"    }\n"
"QPushButton:hover {\n"
"background-color: rgb(135, 135, 135);\n"
"    }")
        self.button1.setObjectName("button1")
        self.button3 = QtWidgets.QPushButton(self.centralwidget)
        self.button3.setGeometry(QtCore.QRect(150, 270, 61, 61))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(24)
        font.setBold(False)
        font.setWeight(50)
        font.setKerning(True)
        self.button3.setFont(font)
        self.button3.setStyleSheet("QPushButton {\n"
"    color: #fff;\n"
"    border-radius: 30px;\n"
"    border-style: outset;\n"
"    background-color: rgb(99, 99, 99);\n"
"    selection-background-color: rgb(172, 172, 172);\n"
"    padding: 5px;\n"
"    }\n"
"QPushButton:hover {\n"
"background-color: rgb(135, 135, 135);\n"
"    }")
        self.button3.setObjectName("button3")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(16, 2, 261, 51))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(24)
        self.label.setFont(font)
        self.label.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.label.setStyleSheet("color: rgb(255, 255, 255);")
        self.label.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label.setObjectName("label")
        Calculator.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(Calculator)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 289, 21))
        self.menubar.setObjectName("menubar")
        Calculator.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(Calculator)
        self.statusbar.setObjectName("statusbar")
        Calculator.setStatusBar(self.statusbar)

        self.retranslateUi(Calculator)
        QtCore.QMetaObject.connectSlotsByName(Calculator)

    def retranslateUi(self, Calculator):
        _translate = QtCore.QCoreApplication.translate
        Calculator.setWindowTitle(_translate("Calculator", "Calculator"))
        self.buttonyuzde.setText(_translate("Calculator", "%"))
        self.buttonae.setText(_translate("Calculator", "+/-"))
        self.buttonbol.setText(_translate("Calculator", "÷"))
        self.buttonclear.setText(_translate("Calculator", "C"))
        self.button4.setText(_translate("Calculator", "4"))
        self.button9.setText(_translate("Calculator", "9"))
        self.button5.setText(_translate("Calculator", "5"))
        self.button8.setText(_translate("Calculator", "8"))
        self.buttoncarp.setText(_translate("Calculator", "x"))
        self.buttoncikar.setText(_translate("Calculator", "-"))
        self.button7.setText(_translate("Calculator", "7"))
        self.button6.setText(_translate("Calculator", "6"))
        self.buttonvirgul.setText(_translate("Calculator", "."))
        self.button0.setText(_translate("Calculator", "0"))
        self.buttonesittir.setText(_translate("Calculator", "="))
        self.buttonarti.setText(_translate("Calculator", "+"))
        self.button2.setText(_translate("Calculator", "2"))
        self.button1.setText(_translate("Calculator", "1"))
        self.button3.setText(_translate("Calculator", "3"))
        self.label.setText(_translate("Calculator", "0"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Calculator = QtWidgets.QMainWindow()
    ui = Ui_Calculator()
    ui.setupUi(Calculator)
    Calculator.show()
    sys.exit(app.exec_())
