# -*- coding: utf-8 -*-
from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Product(object):

    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(1240, 802)
        self.widget = QtWidgets.QWidget(Form)
        self.widget.setGeometry(QtCore.QRect(0, 0, 361, 831))
        self.widget.setStyleSheet("background-color: rgb(121, 0, 182);")
        self.widget.setObjectName("widget")
        self.label_3 = QtWidgets.QLabel(self.widget)
        self.label_3.setGeometry(QtCore.QRect(100, 50, 121, 121))
        self.label_3.setStyleSheet("font: 11pt \"MS Shell Dlg 2\";")
        self.label_3.setText("")
        self.label_3.setPixmap(QtGui.QPixmap("img/cart.png"))
        self.label_3.setScaledContents(True)
        self.label_3.setObjectName("label_3")
        self.label = QtWidgets.QLabel(self.widget)
        self.label.setGeometry(QtCore.QRect(50, 170, 271, 61))
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setPointSize(14)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(10)
        self.label.setFont(font)
        self.label.setStyleSheet("color: rgb(255, 255, 255);\n"
"font: 87 14pt \"Arial Black\";")
        self.label.setObjectName("label")
        self.widget_3 = QtWidgets.QWidget(self.widget)
        self.widget_3.setGeometry(QtCore.QRect(0, 739, 361, 61))
        self.widget_3.setStyleSheet("background-color:rgb(91, 1, 147)")
        self.widget_3.setObjectName("widget_3")
        self.label_5 = QtWidgets.QLabel(self.widget_3)
        self.label_5.setGeometry(QtCore.QRect(150, 10, 81, 41))
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setPointSize(12)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(10)
        self.label_5.setFont(font)
        self.label_5.setStyleSheet("color: rgb(255, 255, 255);\n"
"font: 87 12pt \"Arial Black\";")
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(self.widget_3)
        self.label_6.setGeometry(QtCore.QRect(90, 10, 51, 41))
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setPointSize(12)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(10)
        self.label_6.setFont(font)
        self.label_6.setStyleSheet("color: rgb(255, 255, 255);\n"
"font: 87 12pt \"Arial Black\";")
        self.label_6.setText("")
        self.label_6.setPixmap(QtGui.QPixmap("img/logout.png"))
        self.label_6.setScaledContents(True)
        self.label_6.setObjectName("label_6")
        self.label_2 = QtWidgets.QLabel(self.widget)
        self.label_2.setGeometry(QtCore.QRect(50, 670, 271, 61))
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setPointSize(12)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(10)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet("color: rgb(255, 255, 255);\n"
"font: 87 12pt \"Arial Black\";")
        self.label_2.setObjectName("label_2")
        self.label_7 = QtWidgets.QLabel(self.widget)
        self.label_7.setGeometry(QtCore.QRect(160, 310, 111, 71))
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setPointSize(12)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(10)
        self.label_7.setFont(font)
        self.label_7.setStyleSheet("color: rgb(255, 255, 255);\n"
"font: 87 12pt \"Arial Black\";")
        self.label_7.setObjectName("label_7")
        self.label_14 = QtWidgets.QLabel(self.widget)
        self.label_14.setGeometry(QtCore.QRect(90, 320, 61, 51))
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setPointSize(12)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(10)
        self.label_14.setFont(font)
        self.label_14.setStyleSheet("color: rgb(255, 255, 255);\n"
"font: 87 12pt \"Arial Black\";")
        self.label_14.setText("")
        self.label_14.setPixmap(QtGui.QPixmap("img/products.png"))
        self.label_14.setScaledContents(True)
        self.label_14.setObjectName("label_14")
        self.label_15 = QtWidgets.QLabel(self.widget)
        self.label_15.setGeometry(QtCore.QRect(160, 400, 141, 71))
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setPointSize(12)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(10)
        self.label_15.setFont(font)
        self.label_15.setStyleSheet("color: rgb(255, 255, 255);\n"
"font: 87 12pt \"Arial Black\";")
        self.label_15.setObjectName("label_15")
        self.label_16 = QtWidgets.QLabel(self.widget)
        self.label_16.setGeometry(QtCore.QRect(90, 410, 61, 51))
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setPointSize(12)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(10)
        self.label_16.setFont(font)
        self.label_16.setStyleSheet("color: rgb(255, 255, 255);\n"
"font: 87 12pt \"Arial Black\";")
        self.label_16.setText("")
        self.label_16.setPixmap(QtGui.QPixmap("img/worker.png"))
        self.label_16.setScaledContents(True)
        self.label_16.setObjectName("label_16")
        self.widget_2 = QtWidgets.QWidget(Form)
        self.widget_2.setGeometry(QtCore.QRect(360, 0, 881, 811))
        self.widget_2.setStyleSheet("background-color:rgb(107, 107, 107)")
        self.widget_2.setObjectName("widget_2")
        self.label_4 = QtWidgets.QLabel(self.widget_2)
        self.label_4.setGeometry(QtCore.QRect(250, 20, 321, 31))
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setPointSize(12)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(10)
        self.label_4.setFont(font)
        self.label_4.setStyleSheet("font: 87 12pt \"Arial Black\";\n"
"color: rgb(255, 255, 255);")
        self.label_4.setObjectName("label_4")
        self.label_17 = QtWidgets.QLabel(self.widget_2)
        self.label_17.setGeometry(QtCore.QRect(50, 120, 31, 31))
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setPointSize(12)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(10)
        self.label_17.setFont(font)
        self.label_17.setStyleSheet("font: 87 12pt \"Arial Black\";\n"
"color: rgb(255, 255, 255);")
        self.label_17.setObjectName("label_17")
        self.lineEdit_2 = QtWidgets.QLineEdit(self.widget_2)
        self.lineEdit_2.setGeometry(QtCore.QRect(50, 160, 211, 31))
        self.lineEdit_2.setStyleSheet("background-color: rgb(225, 225, 225);\n"
"\n"
"\n"
"\n"
"\n"
"")
        self.lineEdit_2.setEchoMode(QtWidgets.QLineEdit.Normal)
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.label_18 = QtWidgets.QLabel(self.widget_2)
        self.label_18.setGeometry(QtCore.QRect(50, 230, 171, 31))
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setPointSize(12)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(10)
        self.label_18.setFont(font)
        self.label_18.setStyleSheet("font: 87 12pt \"Arial Black\";\n"
"color: rgb(255, 255, 255);")
        self.label_18.setObjectName("label_18")
        self.lineEdit_3 = QtWidgets.QLineEdit(self.widget_2)
        self.lineEdit_3.setGeometry(QtCore.QRect(50, 270, 211, 31))
        self.lineEdit_3.setStyleSheet("background-color: rgb(225, 225, 225);\n"
"\n"
"\n"
"\n"
"\n"
"")
        self.lineEdit_3.setEchoMode(QtWidgets.QLineEdit.Normal)
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.label_19 = QtWidgets.QLabel(self.widget_2)
        self.label_19.setGeometry(QtCore.QRect(50, 330, 31, 31))
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setPointSize(12)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(10)
        self.label_19.setFont(font)
        self.label_19.setStyleSheet("font: 87 12pt \"Arial Black\";\n"
"color: rgb(255, 255, 255);")
        self.label_19.setObjectName("label_19")
        self.lineEdit_4 = QtWidgets.QLineEdit(self.widget_2)
        self.lineEdit_4.setGeometry(QtCore.QRect(50, 370, 211, 31))
        self.lineEdit_4.setStyleSheet("background-color: rgb(225, 225, 225);\n"
"\n"
"\n"
"\n"
"\n"
"")
        self.lineEdit_4.setEchoMode(QtWidgets.QLineEdit.Normal)
        self.lineEdit_4.setObjectName("lineEdit_4")
        self.widget_4 = QtWidgets.QWidget(self.widget_2)
        self.widget_4.setGeometry(QtCore.QRect(0, 10, 881, 811))
        self.widget_4.setStyleSheet("background-color:rgb(107, 107, 107)")
        self.widget_4.setObjectName("widget_4")
        self.label_20 = QtWidgets.QLabel(self.widget_4)
        self.label_20.setGeometry(QtCore.QRect(250, 20, 321, 31))
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setPointSize(12)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(10)
        self.label_20.setFont(font)
        self.label_20.setStyleSheet("font: 87 12pt \"Arial Black\";\n"
"color: rgb(255, 255, 255);")
        self.label_20.setObjectName("label_20")
        self.label_21 = QtWidgets.QLabel(self.widget_4)
        self.label_21.setGeometry(QtCore.QRect(50, 120, 31, 31))
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setPointSize(12)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(10)
        self.label_21.setFont(font)
        self.label_21.setStyleSheet("font: 87 12pt \"Arial Black\";\n"
"color: rgb(255, 255, 255);")
        self.label_21.setObjectName("label_21")
        self.lineEdit_5 = QtWidgets.QLineEdit(self.widget_4)
        self.lineEdit_5.setGeometry(QtCore.QRect(50, 160, 211, 31))
        self.lineEdit_5.setStyleSheet("background-color: rgb(225, 225, 225);\n"
"border-radius: 10px;\n"
"\n"
"\n"
"\n"
"\n"
"")
        self.lineEdit_5.setEchoMode(QtWidgets.QLineEdit.Normal)
        self.lineEdit_5.setObjectName("lineEdit_5")
        self.label_22 = QtWidgets.QLabel(self.widget_4)
        self.label_22.setGeometry(QtCore.QRect(50, 230, 171, 31))
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setPointSize(12)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(10)
        self.label_22.setFont(font)
        self.label_22.setStyleSheet("font: 87 12pt \"Arial Black\";\n"
"color: rgb(255, 255, 255);")
        self.label_22.setObjectName("label_22")
        self.lineEdit_6 = QtWidgets.QLineEdit(self.widget_4)
        self.lineEdit_6.setGeometry(QtCore.QRect(50, 270, 211, 31))
        self.lineEdit_6.setStyleSheet("background-color: rgb(225, 225, 225);\n"
"border-radius: 10px;\n"
"\n"
"\n"
"\n"
"\n"
"")
        self.lineEdit_6.setEchoMode(QtWidgets.QLineEdit.Normal)
        self.lineEdit_6.setObjectName("lineEdit_6")
        self.label_23 = QtWidgets.QLabel(self.widget_4)
        self.label_23.setGeometry(QtCore.QRect(50, 340, 91, 31))
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setPointSize(12)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(10)
        self.label_23.setFont(font)
        self.label_23.setStyleSheet("font: 87 12pt \"Arial Black\";\n"
"color: rgb(255, 255, 255);")
        self.label_23.setObjectName("label_23")
        self.lineEdit_7 = QtWidgets.QLineEdit(self.widget_4)
        self.lineEdit_7.setGeometry(QtCore.QRect(50, 380, 211, 31))
        self.lineEdit_7.setStyleSheet("background-color: rgb(225, 225, 225);\n"
"border-radius: 10px;\n"
"\n"
"\n"
"\n"
"\n"
"\n"
"\n"
"")
        self.lineEdit_7.setEchoMode(QtWidgets.QLineEdit.Normal)
        self.lineEdit_7.setObjectName("lineEdit_7")
        self.lineEdit_8 = QtWidgets.QLineEdit(self.widget_4)
        self.lineEdit_8.setGeometry(QtCore.QRect(50, 490, 211, 31))
        self.lineEdit_8.setStyleSheet("background-color: rgb(225, 225, 225);\n"
"border-radius: 10px;\n"
"\n"
"\n"
"\n"
"\n"
"")
        self.lineEdit_8.setEchoMode(QtWidgets.QLineEdit.Normal)
        self.lineEdit_8.setObjectName("lineEdit_8")
        self.label_24 = QtWidgets.QLabel(self.widget_4)
        self.label_24.setGeometry(QtCore.QRect(50, 450, 161, 31))
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setPointSize(12)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(10)
        self.label_24.setFont(font)
        self.label_24.setStyleSheet("font: 87 12pt \"Arial Black\";\n"
"color: rgb(255, 255, 255);")
        self.label_24.setObjectName("label_24")
        self.pushButton = QtWidgets.QPushButton(self.widget_4)
        self.pushButton.setGeometry(QtCore.QRect(20, 590, 141, 51))
        self.pushButton.setStyleSheet("background-color: rgb(225, 225, 225);\n"
"color: rgb(79, 79, 79);\n"
"font: 75 12pt \"MS Shell Dlg 2\";\n"
"border-radius: 20px;")
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(self.widget_4)
        self.pushButton_2.setGeometry(QtCore.QRect(100, 660, 141, 51))
        self.pushButton_2.setStyleSheet("background-color: rgb(225, 225, 225);\n"
"color: rgb(79, 79, 79);\n"
"font: 75 12pt \"MS Shell Dlg 2\";\n"
"border-radius: 20px;")
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_3 = QtWidgets.QPushButton(self.widget_4)
        self.pushButton_3.setGeometry(QtCore.QRect(170, 590, 141, 51))
        self.pushButton_3.setStyleSheet("background-color: rgb(225, 225, 225);\n"
"color: rgb(79, 79, 79);\n"
"font: 75 12pt \"MS Shell Dlg 2\";\n"
"border-radius: 20px;")
        self.pushButton_3.setObjectName("pushButton_3")
        self.tableWidget = QtWidgets.QTableWidget(self.widget_4)
        self.tableWidget.setGeometry(QtCore.QRect(330, 90, 541, 681))
        self.tableWidget.setStyleSheet("border: 3px solid white;\n"
"background-color: rgb(209, 209, 209);")
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(4)
        self.tableWidget.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(3, item)
        self.tableWidget.horizontalHeader().setVisible(True)
        self.tableWidget.horizontalHeader().setCascadingSectionResizes(False)
        self.tableWidget.horizontalHeader().setDefaultSectionSize(120)
        self.tableWidget.horizontalHeader().setHighlightSections(True)
        self.tableWidget.horizontalHeader().setStretchLastSection(True)
        self.tableWidget.verticalHeader().setDefaultSectionSize(37)
        self.tableWidget.verticalHeader().setHighlightSections(True)
        self.tableWidget.verticalHeader().setMinimumSectionSize(40)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.label.setText(_translate("Form", "Prime Supermarket"))
        self.label_5.setText(_translate("Form", "Logout"))
        self.label_2.setText(_translate("Form", "Low Price High Quality..."))
        self.label_7.setText(_translate("Form", "Products"))
        self.label_15.setText(_translate("Form", "Employees"))
        self.label_4.setText(_translate("Form", "Product Management System"))
        self.label_17.setText(_translate("Form", "Id:"))
        self.label_18.setText(_translate("Form", "Product Name:"))
        self.label_19.setText(_translate("Form", "Id:"))
        self.label_20.setText(_translate("Form", "Product Management System"))
        self.label_21.setText(_translate("Form", "Id:"))
        self.label_22.setText(_translate("Form", "Product Name:"))
        self.label_23.setText(_translate("Form", "Stock:"))
        self.label_24.setText(_translate("Form", "Product Price:"))
        self.pushButton.setText(_translate("Form", "Add"))
        self.pushButton_2.setText(_translate("Form", "Update"))
        self.pushButton_3.setText(_translate("Form", "Delete"))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("Form", "id"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("Form", "productName"))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("Form", "stock"))
        item = self.tableWidget.horizontalHeaderItem(3)
        item.setText(_translate("Form", "productPrice"))