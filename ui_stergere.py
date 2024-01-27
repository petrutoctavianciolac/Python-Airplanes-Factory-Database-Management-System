# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ui_stergere.ui'
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
from PySide6.QtWidgets import (QApplication, QFrame, QLabel, QLineEdit,
    QPushButton, QSizePolicy, QWidget)

class Ui_WidgetS(object):
    def setupUi(self, Widget):
        if not Widget.objectName():
            Widget.setObjectName(u"Widget")
        Widget.resize(300, 400)
        Widget.setStyleSheet(u"background-color: rgb(192,192,192);")
        self.frame = QFrame(Widget)
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
        self.stergereAvion = QPushButton(Widget)
        self.stergereAvion.setObjectName(u"stergereAvion")
        self.stergereAvion.setGeometry(QRect(110, 320, 80, 24))
        self.stergereAvion.setStyleSheet(u"QPushButton{background-color:  rgb(255, 255, 255);\n"
"border-radius: 0px;\n"
"font: 12pt \"Segoe UI\";\n"
"color: rgb(0, 0, 0);}\n"
"\n"
"QPushButton:hover{\n"
"border: 1px solid rgb(255,0,0);\n"
"}")
        self.sterge_operator = QLabel(Widget)
        self.sterge_operator.setObjectName(u"sterge_operator")
        self.sterge_operator.setGeometry(QRect(50, 130, 200, 31))
        self.sterge_operator.setStyleSheet(u"font: 16pt \"Segoe UI\";\n"
"color: rgb(255, 255, 255);")
        self.iCod = QLineEdit(Widget)
        self.iCod.setObjectName(u"iCod")
        self.iCod.setGeometry(QRect(50, 190, 200, 24))
        self.iCod.setStyleSheet(u"QLineEdit{\n"
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

        self.iCod.setAlignment(Qt.AlignCenter)
        self.retranslateUi(Widget)

        QMetaObject.connectSlotsByName(Widget)
    # setupUi

    def retranslateUi(self, Widget):
        Widget.setWindowTitle(QCoreApplication.translate("Widget", u"Widget", None))
        self.label.setText(QCoreApplication.translate("Widget", u"\u0218tergere Avion", None))
        self.stergereAvion.setText(QCoreApplication.translate("Widget", u"\u0218tergere", None))
        self.sterge_operator.setText(QCoreApplication.translate("Widget", u"Cod:", None))
    # retranslateUi

