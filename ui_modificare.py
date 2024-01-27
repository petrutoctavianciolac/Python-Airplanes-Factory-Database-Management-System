# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ui_modificare.ui'
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

class Ui_WidgetM(object):
    def setupUi(self, Widget):
        if not Widget.objectName():
            Widget.setObjectName(u"Widget")
        Widget.resize(300, 600)
        Widget.setStyleSheet(u"background-color: rgb(192,192,192);")
        self.frame = QFrame(Widget)
        self.frame.setObjectName(u"frame")
        self.frame.setGeometry(QRect(0, 0, 301, 121))
        self.frame.setStyleSheet(u"background-color:  rgb(138,43,226);")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.label = QLabel(self.frame)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(60, 40, 180, 31))
        self.label.setStyleSheet(u"font: 18pt \"Arial\";\n"
"color: rgb(255, 255, 255);")
        self.label_2 = QLabel(self.frame)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(60, 80, 180, 16))
        self.label_2.setStyleSheet(u"font: 18\n"
"10pt \"Arial\";\n"
"color: rgb(255, 255, 255);")
        self.aLabel_3 = QLabel(Widget)
        self.aLabel_3.setObjectName(u"aLabel_3")
        self.aLabel_3.setGeometry(QRect(110, 250, 80, 16))
        self.aLabel_3.setStyleSheet(u"font: 14pt \"Arial\";\n"
"color: rgb(255, 255, 255);")
        self.aLabel = QLabel(Widget)
        self.aLabel.setObjectName(u"aLabel")
        self.aLabel.setGeometry(QRect(100, 130, 100, 16))
        self.aLabel.setStyleSheet(u"font: 14pt \"Arial\";\n"
"color: rgb(255, 255, 255);")
        self.aLabel_4 = QLabel(Widget)
        self.aLabel_4.setObjectName(u"aLabel_4")
        self.aLabel_4.setGeometry(QRect(110, 300, 80, 21))
        self.aLabel_4.setStyleSheet(u"font: 14pt \"Arial\";\n"
"color: rgb(255, 255, 255);")
        self.iDepartament = QComboBox(Widget)
        self.iDepartament.setObjectName(u"iDepartament")
        self.iDepartament.setGeometry(QRect(50, 520, 200, 24))
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
        self.aLabel_2 = QLabel(Widget)
        self.aLabel_2.setObjectName(u"aLabel_2")
        self.aLabel_2.setGeometry(QRect(130, 190, 60, 16))
        self.aLabel_2.setStyleSheet(u"font: 14pt \"Arial\";\n"
"color: rgb(255, 255, 255);")
        self.iLocuri = QLineEdit(Widget)
        self.iLocuri.setObjectName(u"iLocuri")
        self.iLocuri.setGeometry(QRect(50, 450, 200, 24))
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
        self.aLabel_7 = QLabel(Widget)
        self.aLabel_7.setObjectName(u"aLabel_7")
        self.aLabel_7.setGeometry(QRect(75, 490, 150, 16))
        self.aLabel_7.setStyleSheet(u"font: 14pt \"Arial\";\n"
"color: rgb(255, 255, 255);")
        self.iCost = QLineEdit(Widget)
        self.iCost.setObjectName(u"iCost")
        self.iCost.setGeometry(QRect(50, 270, 200, 24))
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
        self.iPret = QLineEdit(Widget)
        self.iPret.setObjectName(u"iPret")
        self.iPret.setGeometry(QRect(50, 330, 200, 24))
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
        self.aLabel_5 = QLabel(Widget)
        self.aLabel_5.setObjectName(u"aLabel_5")
        self.aLabel_5.setGeometry(QRect(95, 365, 110, 16))
        self.aLabel_5.setStyleSheet(u"font: 14pt \"Arial\";\n"
"color: rgb(255, 255, 255);")
        self.aLabel_6 = QLabel(Widget)
        self.aLabel_6.setObjectName(u"aLabel_6")
        self.aLabel_6.setGeometry(QRect(75, 420, 150, 16))
        self.aLabel_6.setStyleSheet(u"font: 14pt \"Arial\";\n"
"color: rgb(255, 255, 255);")
        self.iViteza = QLineEdit(Widget)
        self.iViteza.setObjectName(u"iViteza")
        self.iViteza.setGeometry(QRect(50, 390, 200, 24))
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
        self.modificareAvion = QPushButton(Widget)
        self.modificareAvion.setObjectName(u"modificareAvion")
        self.modificareAvion.setGeometry(QRect(110, 560, 80, 25))
        self.modificareAvion.setStyleSheet(u"QPushButton{background-color:  rgb(255, 255, 255);\n"
"border-radius: 0px;\n"
"font: 12pt \"Segoe UI\";\n"
"color: rgb(0, 0, 0);}\n"
"\n"
"QPushButton:hover{\n"
"border: 1px solid rgb(255,165,0);\n"
"}\n"
"")
        self.iCodAvion = QLineEdit(Widget)
        self.iCodAvion.setObjectName(u"iCodAvion")
        self.iCodAvion.setGeometry(QRect(50, 210, 200, 24))
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
        self.iNumeAvion = QLineEdit(Widget)
        self.iNumeAvion.setObjectName(u"iNumeAvion")
        self.iNumeAvion.setGeometry(QRect(50, 150, 200, 24))
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

        self.retranslateUi(Widget)

        self.iCodAvion.setAlignment(Qt.AlignCenter)
        self.iNumeAvion.setAlignment(Qt.AlignCenter)
        self.iCost.setAlignment(Qt.AlignCenter)
        self.iPret.setAlignment(Qt.AlignCenter)
        self.iViteza.setAlignment(Qt.AlignCenter)
        self.iLocuri.setAlignment(Qt.AlignCenter)

        QMetaObject.connectSlotsByName(Widget)
    # setupUi

    def retranslateUi(self, Widget):
        Widget.setWindowTitle(QCoreApplication.translate("Widget", u"Widget", None))
        self.label.setText(QCoreApplication.translate("Widget", u"Modificare Avion", None))
        self.label_2.setText(QCoreApplication.translate("Widget", u"Modificarea se face dup\u0103 cod!", None))
        self.aLabel_3.setText(QCoreApplication.translate("Widget", u"Cost nou:", None))
        self.aLabel.setText(QCoreApplication.translate("Widget", u"Nume nou:", None))
        self.aLabel_4.setText(QCoreApplication.translate("Widget", u"Pre\u021b nou:", None))
        self.aLabel_2.setText(QCoreApplication.translate("Widget", u"Cod:", None))
        self.aLabel_7.setText(QCoreApplication.translate("Widget", u"Departament nou:", None))
        self.aLabel_5.setText(QCoreApplication.translate("Widget", u"Vitez\u0103 nou\u0103:", None))
        self.aLabel_6.setText(QCoreApplication.translate("Widget", u"Num\u0103r locuri nou:", None))
        self.modificareAvion.setText(QCoreApplication.translate("Widget", u"Modificare", None))
    # retranslateUi

