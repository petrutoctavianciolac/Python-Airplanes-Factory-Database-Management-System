# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ui_adaugare.ui'
##
## Created by: Qt User Interface Compiler version 6.6.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QComboBox, QFrame, QLabel,
    QLineEdit, QPushButton, QSizePolicy, QWidget)

class Ui_Widget(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(300, 600)
        Form.setStyleSheet(u"background-color: rgb(192,192,192);")
        self.frame = QFrame(Form)
        self.frame.setObjectName(u"frame")
        self.frame.setGeometry(QRect(0, 0, 301, 121))
        self.frame.setStyleSheet(u"background-color:  rgb(138,43,226);")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.label = QLabel(self.frame)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(65, 40, 170, 31))
        self.label.setStyleSheet(u"font: 18pt \"Arial\";\n"
"color: rgb(255, 255, 255);")
        self.adaugareAvion = QPushButton(Form)
        self.adaugareAvion.setObjectName(u"adaugareAvion")
        self.adaugareAvion.setGeometry(QRect(120, 570, 80, 25))
        self.adaugareAvion.setStyleSheet(u"QPushButton{background-color:  rgb(255, 255, 255);\n"
"border-radius: 0px;\n"
"font: 12pt \"Segoe UI\";\n"
"color: rgb(0, 0, 0);}\n"
"\n"
"QPushButton:hover{\n"
"border: 1px solid rgb(30,144,255);\n"
"}\n"
"")
        self.iNumeAvion = QLineEdit(Form)
        self.iNumeAvion.setObjectName(u"iNumeAvion")
        self.iNumeAvion.setGeometry(QRect(60, 170, 200, 24))
        self.iNumeAvion.setStyleSheet(u"QLineEdit{\n"
"color: rgb(0, 0, 0);\n"
"background-color: rgb(255, 255, 255);\n"
"border: 2px solid;\n"
"border-color: rgb(138,43,226);\n"
"border-radius: 5px;\n"
"font: 10pt \"Arial\";\n"
"}\n"
"\n"
"QLineEdit:focus{\n"
"border-color: rgb(34,139,34);\n"
"}")
        self.iCodAvion = QLineEdit(Form)
        self.iCodAvion.setObjectName(u"iCodAvion")
        self.iCodAvion.setGeometry(QRect(60, 230, 200, 24))
        self.iCodAvion.setStyleSheet(u"QLineEdit{\n"
"color: rgb(0, 0, 0);\n"
"background-color: rgb(255, 255, 255);\n"
"border: 2px solid;\n"
"border-color: rgb(138,43,226);\n"
"border-radius: 5px;\n"
"font: 10pt \"Arial\";\n"
"}\n"
"\n"
"QLineEdit:focus{\n"
"border-color: rgb(34,139,34);\n"
"}")
        self.iCost = QLineEdit(Form)
        self.iCost.setObjectName(u"iCost")
        self.iCost.setGeometry(QRect(60, 290, 200, 24))
        self.iCost.setStyleSheet(u"QLineEdit{\n"
"color: rgb(0, 0, 0);\n"
"background-color: rgb(255, 255, 255);\n"
"border: 2px solid;\n"
"border-color: rgb(138,43,226);\n"
"border-radius: 5px;\n"
"font: 10pt \"Arial\";\n"
"}\n"
"\n"
"QLineEdit:focus{\n"
"border-color: rgb(34,139,34);\n"
"}")
        self.iPret = QLineEdit(Form)
        self.iPret.setObjectName(u"iPret")
        self.iPret.setGeometry(QRect(60, 350, 200, 24))
        self.iPret.setStyleSheet(u"QLineEdit{\n"
"color: rgb(0, 0, 0);\n"
"background-color: rgb(255, 255, 255);\n"
"border: 2px solid;\n"
"border-color: rgb(138,43,226);\n"
"border-radius: 5px;\n"
"font: 10pt \"Arial\";\n"
"}\n"
"\n"
"QLineEdit:focus{\n"
"border-color: rgb(34,139,34);\n"
"}")
        self.iViteza = QLineEdit(Form)
        self.iViteza.setObjectName(u"iViteza")
        self.iViteza.setGeometry(QRect(60, 410, 200, 24))
        self.iViteza.setStyleSheet(u"QLineEdit{\n"
"color: rgb(0, 0, 0);\n"
"background-color: rgb(255, 255, 255);\n"
"border: 2px solid;\n"
"border-color: rgb(138,43,226);\n"
"border-radius: 5px;\n"
"font: 10pt \"Arial\";\n"
"}\n"
"\n"
"QLineEdit:focus{\n"
"border-color: rgb(34,139,34);\n"
"}")
        self.iLocuri = QLineEdit(Form)
        self.iLocuri.setObjectName(u"iLocuri")
        self.iLocuri.setGeometry(QRect(60, 470, 201, 24))
        self.iLocuri.setStyleSheet(u"QLineEdit{\n"
"color: rgb(0, 0, 0);\n"
"background-color: rgb(255, 255, 255);\n"
"border: 2px solid;\n"
"border-color: rgb(138,43,226);\n"
"border-radius: 5px;\n"
"font: 10pt \"Arial\";\n"
"}\n"
"\n"
"QLineEdit:focus{\n"
"border-color: rgb(34,139,34);\n"
"}")
        self.iLocuri.setAlignment(Qt.AlignCenter)
        self.aLabel = QLabel(Form)
        self.aLabel.setObjectName(u"aLabel")
        self.aLabel.setGeometry(QRect(120, 140, 60, 16))
        self.aLabel.setStyleSheet(u"font: 14pt \"Arial\";\n"
"color: rgb(255, 255, 255);")
        self.aLabel_2 = QLabel(Form)
        self.aLabel_2.setObjectName(u"aLabel_2")
        self.aLabel_2.setGeometry(QRect(130, 210, 60, 16))
        self.aLabel_2.setStyleSheet(u"font: 14pt \"Arial\";\n"
"color: rgb(255, 255, 255);")
        self.aLabel_3 = QLabel(Form)
        self.aLabel_3.setObjectName(u"aLabel_3")
        self.aLabel_3.setGeometry(QRect(130, 260, 60, 16))
        self.aLabel_3.setStyleSheet(u"font: 14pt \"Arial\";\n"
"color: rgb(255, 255, 255);")
        self.aLabel_4 = QLabel(Form)
        self.aLabel_4.setObjectName(u"aLabel_4")
        self.aLabel_4.setGeometry(QRect(130, 320, 60, 21))
        self.aLabel_4.setStyleSheet(u"font: 14pt \"Arial\";\n"
"color: rgb(255, 255, 255);")
        self.aLabel_5 = QLabel(Form)
        self.aLabel_5.setObjectName(u"aLabel_5")
        self.aLabel_5.setGeometry(QRect(130, 380, 60, 16))
        self.aLabel_5.setStyleSheet(u"font: 14pt \"Arial\";\n"
"color: rgb(255, 255, 255);")
        self.aLabel_6 = QLabel(Form)
        self.aLabel_6.setObjectName(u"aLabel_6")
        self.aLabel_6.setGeometry(QRect(130, 440, 60, 16))
        self.aLabel_6.setStyleSheet(u"font: 14pt \"Arial\";\n"
"color: rgb(255, 255, 255);")
        self.iDepartament = QComboBox(Form)
        self.iDepartament.setObjectName(u"iDepartament")
        self.iDepartament.setGeometry(QRect(60, 530, 200, 24))
        self.iDepartament.setStyleSheet(u"QComboBox{\n"
"color: rgb(0, 0, 0);\n"
"background-color: rgb(255, 255, 255);\n"
"border: 2px solid;\n"
"border-color: rgb(138,43,226);\n"
"border-radius: 5px;\n"
"font: 10pt \"Arial\";\n"
"}\n"
"\n"
"QComboBox:focus{\n"
"border-color: rgb(34,139,34);\n"
"}")
        self.aLabel_7 = QLabel(Form)
        self.aLabel_7.setObjectName(u"aLabel_7")
        self.aLabel_7.setGeometry(QRect(100, 500, 120, 16))
        self.aLabel_7.setStyleSheet(u"font: 14pt \"Arial\";\n"
"color: rgb(255, 255, 255);")

        self.iCodAvion.setAlignment(Qt.AlignCenter)
        self.iNumeAvion.setAlignment(Qt.AlignCenter)
        self.iCost.setAlignment(Qt.AlignCenter)
        self.iPret.setAlignment(Qt.AlignCenter)
        self.iViteza.setAlignment(Qt.AlignCenter)
        self.iLocuri.setAlignment(Qt.AlignCenter)

        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.label.setText(QCoreApplication.translate("Form", u"Ad\u0103ugare Avion", None))
        self.adaugareAvion.setText(QCoreApplication.translate("Form", u"Ad\u0103ugare", None))
        self.aLabel.setText(QCoreApplication.translate("Form", u"Nume:", None))
        self.aLabel_2.setText(QCoreApplication.translate("Form", u"Cod:", None))
        self.aLabel_3.setText(QCoreApplication.translate("Form", u"Cost:", None))
        self.aLabel_4.setText(QCoreApplication.translate("Form", u"Pre\u021b:", None))
        self.aLabel_5.setText(QCoreApplication.translate("Form", u"Vitez\u0103:", None))
        self.aLabel_6.setText(QCoreApplication.translate("Form", u"Locuri:", None))
        self.aLabel_7.setText(QCoreApplication.translate("Form", u"Departament:", None))
    # retranslateUi

