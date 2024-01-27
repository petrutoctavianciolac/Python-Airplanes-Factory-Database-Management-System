# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'form.ui'
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
from PySide6.QtWidgets import (QApplication, QComboBox, QHeaderView, QLabel,
    QLineEdit, QPushButton, QSizePolicy, QTabWidget,
    QTableWidget, QTableWidgetItem, QWidget)

class Ui_Widget(object):
    def setupUi(self, Widget):
        if not Widget.objectName():
            Widget.setObjectName(u"Widget")
        Widget.setEnabled(True)
        Widget.resize(800, 600)
        Widget.setMaximumSize(QSize(1000, 800))
        icon = QIcon()
        icon.addFile(u"airplane.png", QSize(), QIcon.Normal, QIcon.Off)
        Widget.setWindowIcon(icon)
        Widget.setStyleSheet(u"background-color:  rgb(138,43,226);\n"
"")
        self.bunVenit = QLabel(Widget)
        self.bunVenit.setObjectName(u"bunVenit")
        self.bunVenit.setGeometry(QRect(290, 0, 171, 61))
        self.bunVenit.setStyleSheet(u"font: 22pt \"Segoe UI\";\n"
"color: rgb(255, 255, 255);")
        self.menu = QTabWidget(Widget)
        self.menu.setObjectName(u"menu")
        self.menu.setGeometry(QRect(0, 50, 810, 551))
        self.menu.setStyleSheet(u"font: 14pt \"Segoe UI\";\n"
"color:  rgb(138,43,226);;\n"
"background-color: rgb(192,192,192);\n"
"border-color: rgb(138,43,226);\n"
"border-radius: 5px;\n"
"")
        self.menu.setTabBarAutoHide(False)
        self.operatori = QWidget()
        self.operatori.setObjectName(u"operatori")
        self.introducere_operator = QLabel(self.operatori)
        self.introducere_operator.setObjectName(u"introducere_operator")
        self.introducere_operator.setGeometry(QRect(10, 10, 201, 31))
        self.introducere_operator.setStyleSheet(u"font: 16pt \"Segoe UI\";\n"
"color: rgb(255, 255, 255);")
        self.numeOperator = QLabel(self.operatori)
        self.numeOperator.setObjectName(u"numeOperator")
        self.numeOperator.setGeometry(QRect(10, 80, 49, 16))
        self.numeOperator.setStyleSheet(u"font: 12pt \"Segoe UI\";\n"
"color: rgb(255, 255, 255);")
        self.inputNumeOperator = QLineEdit(self.operatori)
        self.inputNumeOperator.setObjectName(u"inputNumeOperator")
        self.inputNumeOperator.setGeometry(QRect(10, 110, 201, 24))
        self.inputNumeOperator.setStyleSheet(u"QLineEdit{\n"
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
        self.codOperator = QLabel(self.operatori)
        self.codOperator.setObjectName(u"codOperator")
        self.codOperator.setGeometry(QRect(10, 140, 49, 16))
        self.codOperator.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"font: 12pt \"Segoe UI\";")
        self.inputCodOperator = QLineEdit(self.operatori)
        self.inputCodOperator.setObjectName(u"inputCodOperator")
        self.inputCodOperator.setGeometry(QRect(10, 170, 201, 24))
        self.inputCodOperator.setStyleSheet(u"QLineEdit{\n"
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
        self.regiuneOperator = QLabel(self.operatori)
        self.regiuneOperator.setObjectName(u"regiuneOperator")
        self.regiuneOperator.setGeometry(QRect(10, 210, 71, 21))
        self.regiuneOperator.setStyleSheet(u"font: 12pt \"Segoe UI\";\n"
"color: rgb(255, 255, 255);")
        self.inputRegiuneOperator = QLineEdit(self.operatori)
        self.inputRegiuneOperator.setObjectName(u"inputRegiuneOperator")
        self.inputRegiuneOperator.setGeometry(QRect(10, 240, 201, 24))
        self.inputRegiuneOperator.setStyleSheet(u"QLineEdit{\n"
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
        self.introduOperator = QPushButton(self.operatori)
        self.introduOperator.setObjectName(u"introduOperator")
        self.introduOperator.setGeometry(QRect(10, 280, 91, 24))
        self.introduOperator.setStyleSheet(u"QPushButton{background-color:  rgb(255, 255, 255);\n"
"border-radius: 0px;\n"
"font: 12pt \"Segoe UI\";\n"
"color: rgb(0, 0, 0);}\n"
"\n"
"QPushButton:hover{\n"
"border: 1px solid rgb(30,144,255);\n"
"}\n"
"")
        self.sterge_operator = QLabel(self.operatori)
        self.sterge_operator.setObjectName(u"sterge_operator")
        self.sterge_operator.setGeometry(QRect(10, 340, 201, 31))
        self.sterge_operator.setStyleSheet(u"font: 16pt \"Segoe UI\";\n"
"color: rgb(255, 255, 255);")
        self.numeOperatorStergere = QLabel(self.operatori)
        self.numeOperatorStergere.setObjectName(u"numeOperatorStergere")
        self.numeOperatorStergere.setGeometry(QRect(10, 390, 49, 16))
        self.numeOperatorStergere.setStyleSheet(u"font: 12pt \"Segoe UI\";\n"
"color: rgb(255, 255, 255);")
        self.inputCodOperatorStergere = QLineEdit(self.operatori)
        self.inputCodOperatorStergere.setObjectName(u"inputCodOperatorStergere")
        self.inputCodOperatorStergere.setGeometry(QRect(10, 420, 201, 24))
        self.inputCodOperatorStergere.setStyleSheet(u"QLineEdit{\n"
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
        self.introduOperatorStergere = QPushButton(self.operatori)
        self.introduOperatorStergere.setObjectName(u"introduOperatorStergere")
        self.introduOperatorStergere.setGeometry(QRect(10, 470, 91, 24))
        self.introduOperatorStergere.setStyleSheet(u"QPushButton{background-color:  rgb(255, 255, 255);\n"
"border-radius: 0px;\n"
"font: 12pt \"Segoe UI\";\n"
"color: rgb(0, 0, 0);}\n"
"\n"
"QPushButton:hover{\n"
"border: 1px solid rgb(255,0,0);\n"
"}")
        self.modificareOperator = QLabel(self.operatori)
        self.modificareOperator.setObjectName(u"modificareOperator")
        self.modificareOperator.setGeometry(QRect(240, 10, 201, 31))
        self.modificareOperator.setStyleSheet(u"font: 16pt \"Segoe UI\";\n"
"color: rgb(255, 255, 255);")
        self.modificareRegiuneOperator = QLabel(self.operatori)
        self.modificareRegiuneOperator.setObjectName(u"modificareRegiuneOperator")
        self.modificareRegiuneOperator.setGeometry(QRect(240, 50, 171, 31))
        self.modificareRegiuneOperator.setStyleSheet(u"font: 14pt \"Segoe UI\";\n"
"color: rgb(255, 255, 255);")
        self.codOperatorModificareRegiune = QLabel(self.operatori)
        self.codOperatorModificareRegiune.setObjectName(u"codOperatorModificareRegiune")
        self.codOperatorModificareRegiune.setGeometry(QRect(240, 80, 49, 16))
        self.codOperatorModificareRegiune.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"font: 12pt \"Segoe UI\";")
        self.inputCodOperatorModificareRegiune = QLineEdit(self.operatori)
        self.inputCodOperatorModificareRegiune.setObjectName(u"inputCodOperatorModificareRegiune")
        self.inputCodOperatorModificareRegiune.setGeometry(QRect(240, 110, 201, 24))
        self.inputCodOperatorModificareRegiune.setStyleSheet(u"QLineEdit{\n"
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
        self.regiuneNouaOperator = QLabel(self.operatori)
        self.regiuneNouaOperator.setObjectName(u"regiuneNouaOperator")
        self.regiuneNouaOperator.setGeometry(QRect(240, 140, 101, 21))
        self.regiuneNouaOperator.setStyleSheet(u"font: 12pt \"Segoe UI\";\n"
"color: rgb(255, 255, 255);")
        self.inputRegiuneNouaOperator = QLineEdit(self.operatori)
        self.inputRegiuneNouaOperator.setObjectName(u"inputRegiuneNouaOperator")
        self.inputRegiuneNouaOperator.setGeometry(QRect(240, 170, 201, 24))
        self.inputRegiuneNouaOperator.setStyleSheet(u"QLineEdit{\n"
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
        self.introduNouaRegiune = QPushButton(self.operatori)
        self.introduNouaRegiune.setObjectName(u"introduNouaRegiune")
        self.introduNouaRegiune.setGeometry(QRect(240, 210, 91, 24))
        self.introduNouaRegiune.setStyleSheet(u"QPushButton{background-color:  rgb(255, 255, 255);\n"
"border-radius: 0px;\n"
"font: 12pt \"Segoe UI\";\n"
"color: rgb(0, 0, 0);}\n"
"\n"
"QPushButton:hover{\n"
"border: 1px solid rgb(255,140,0);\n"
"}")
        self.modificareNumeOperator = QLabel(self.operatori)
        self.modificareNumeOperator.setObjectName(u"modificareNumeOperator")
        self.modificareNumeOperator.setGeometry(QRect(460, 50, 171, 31))
        self.modificareNumeOperator.setStyleSheet(u"font: 14pt \"Segoe UI\";\n"
"color: rgb(255, 255, 255);")
        self.codOperatorModificareNume = QLabel(self.operatori)
        self.codOperatorModificareNume.setObjectName(u"codOperatorModificareNume")
        self.codOperatorModificareNume.setGeometry(QRect(460, 80, 49, 16))
        self.codOperatorModificareNume.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"font: 12pt \"Segoe UI\";")
        self.inputCodOperatorModificareNume = QLineEdit(self.operatori)
        self.inputCodOperatorModificareNume.setObjectName(u"inputCodOperatorModificareNume")
        self.inputCodOperatorModificareNume.setGeometry(QRect(460, 110, 201, 24))
        self.inputCodOperatorModificareNume.setStyleSheet(u"QLineEdit{\n"
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
        self.numrNouOperator = QLabel(self.operatori)
        self.numrNouOperator.setObjectName(u"numrNouOperator")
        self.numrNouOperator.setGeometry(QRect(460, 140, 101, 21))
        self.numrNouOperator.setStyleSheet(u"font: 12pt \"Segoe UI\";\n"
"color: rgb(255, 255, 255);")
        self.inputNumeNouOperator = QLineEdit(self.operatori)
        self.inputNumeNouOperator.setObjectName(u"inputNumeNouOperator")
        self.inputNumeNouOperator.setGeometry(QRect(460, 170, 201, 24))
        self.inputNumeNouOperator.setStyleSheet(u"QLineEdit{\n"
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
        self.introduNumeleNou = QPushButton(self.operatori)
        self.introduNumeleNou.setObjectName(u"introduNumeleNou")
        self.introduNumeleNou.setGeometry(QRect(460, 210, 91, 24))
        self.introduNumeleNou.setStyleSheet(u"QPushButton{background-color:  rgb(255, 255, 255);\n"
"border-radius: 0px;\n"
"font: 12pt \"Segoe UI\";\n"
"color: rgb(0, 0, 0);}\n"
"\n"
"QPushButton:hover{\n"
"border: 1px solid rgb(255,140,0);\n"
"}")
        self.afisareOperatori = QTableWidget(self.operatori)
        if (self.afisareOperatori.columnCount() < 3):
            self.afisareOperatori.setColumnCount(3)
        icon1 = QIcon(QIcon.fromTheme(u"applications-multimedia"))
        __qtablewidgetitem = QTableWidgetItem()
        __qtablewidgetitem.setIcon(icon1);
        self.afisareOperatori.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.afisareOperatori.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.afisareOperatori.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        self.afisareOperatori.setObjectName(u"afisareOperatori")
        self.afisareOperatori.setGeometry(QRect(310, 260, 491, 251))
        self.afisareOperatori.setMinimumSize(QSize(0, 0))
        self.afisareOperatori.viewport().setProperty("cursor", QCursor(Qt.OpenHandCursor))
        self.afisareOperatori.setStyleSheet(u"color: rgb(0, 0, 0);\n"
"border-color: rgb(0, 0, 0);\n"
"background-color: rgb(255, 255, 255);\n"
"")
        self.afisareOperatori.setRowCount(0)
        self.afisareOperatori.setColumnCount(3)
        self.afisareOperatori.horizontalHeader().setMinimumSectionSize(60)
        self.afisareOperatori.horizontalHeader().setHighlightSections(True)
        self.afisareOperatori.verticalHeader().setMinimumSectionSize(30)
        self.afisareOperatori.verticalHeader().setDefaultSectionSize(30)
        self.menu.addTab(self.operatori, "")
        self.avioane = QWidget()
        self.avioane.setObjectName(u"avioane")
        self.avioane.setStyleSheet(u"")
        self.adaugareAvion = QPushButton(self.avioane)
        self.adaugareAvion.setObjectName(u"adaugareAvion")
        self.adaugareAvion.setGeometry(QRect(365, 370, 80, 25))
        self.adaugareAvion.setStyleSheet(u"QPushButton{background-color:  rgb(255, 255, 255);\n"
"border-radius: 0px;\n"
"font: 12pt \"Segoe UI\";\n"
"color: rgb(0, 0, 0);}\n"
"\n"
"QPushButton:hover{\n"
"border: 1px solid rgb(30,144,255);\n"
"}\n"
"")
        self.stergereAvion = QPushButton(self.avioane)
        self.stergereAvion.setObjectName(u"stergereAvion")
        self.stergereAvion.setGeometry(QRect(365, 400, 80, 25))
        self.stergereAvion.setStyleSheet(u"QPushButton{background-color:  rgb(255, 255, 255);\n"
"border-radius: 0px;\n"
"font: 12pt \"Segoe UI\";\n"
"color: rgb(0, 0, 0);}\n"
"\n"
"QPushButton:hover{\n"
"border: 1px solid rgb(255,0,0);\n"
"}")
        self.tabelAvioane = QTableWidget(self.avioane)
        if (self.tabelAvioane.columnCount() < 7):
            self.tabelAvioane.setColumnCount(7)
        brush = QBrush(QColor(0, 0, 0, 255))
        brush.setStyle(Qt.NoBrush)
        __qtablewidgetitem3 = QTableWidgetItem()
        __qtablewidgetitem3.setForeground(brush);
        self.tabelAvioane.setHorizontalHeaderItem(0, __qtablewidgetitem3)
        __qtablewidgetitem4 = QTableWidgetItem()
        self.tabelAvioane.setHorizontalHeaderItem(1, __qtablewidgetitem4)
        brush1 = QBrush(QColor(0, 0, 0, 255))
        brush1.setStyle(Qt.NoBrush)
        __qtablewidgetitem5 = QTableWidgetItem()
        __qtablewidgetitem5.setBackground(QColor(255, 255, 255));
        __qtablewidgetitem5.setForeground(brush1);
        self.tabelAvioane.setHorizontalHeaderItem(2, __qtablewidgetitem5)
        brush2 = QBrush(QColor(0, 0, 0, 255))
        brush2.setStyle(Qt.NoBrush)
        __qtablewidgetitem6 = QTableWidgetItem()
        __qtablewidgetitem6.setBackground(QColor(138, 43, 226));
        __qtablewidgetitem6.setForeground(brush2);
        self.tabelAvioane.setHorizontalHeaderItem(3, __qtablewidgetitem6)
        __qtablewidgetitem7 = QTableWidgetItem()
        self.tabelAvioane.setHorizontalHeaderItem(4, __qtablewidgetitem7)
        __qtablewidgetitem8 = QTableWidgetItem()
        self.tabelAvioane.setHorizontalHeaderItem(5, __qtablewidgetitem8)
        __qtablewidgetitem9 = QTableWidgetItem()
        self.tabelAvioane.setHorizontalHeaderItem(6, __qtablewidgetitem9)
        self.tabelAvioane.setObjectName(u"tabelAvioane")
        self.tabelAvioane.setGeometry(QRect(0, 20, 801, 341))
        self.tabelAvioane.viewport().setProperty("cursor", QCursor(Qt.OpenHandCursor))
        self.tabelAvioane.setStyleSheet(u"background-color:  rgb(255, 255, 255);\n"
"border-radius: 0px;\n"
"font: 12pt \"Segoe UI\";\n"
"color: rgb(0, 0, 0);\n"
"")
        self.modificareAvion = QPushButton(self.avioane)
        self.modificareAvion.setObjectName(u"modificareAvion")
        self.modificareAvion.setGeometry(QRect(365, 430, 80, 25))
        self.modificareAvion.setStyleSheet(u"QPushButton{background-color:  rgb(255, 255, 255);\n"
"border-radius: 0px;\n"
"font: 12pt \"Segoe UI\";\n"
"color: rgb(0, 0, 0);}\n"
"\n"
"QPushButton:hover{\n"
"border: 1px solid rgb(255,0,0);\n"
"}")
        self.menu.addTab(self.avioane, "")
        self.cautare = QWidget()
        self.cautare.setObjectName(u"cautare")
        self.tabelCautare = QTableWidget(self.cautare)
        self.tabelCautare.setObjectName(u"tabelCautare")
        self.tabelCautare.setGeometry(QRect(120, 230, 521, 192))
        self.tabelCautare.setStyleSheet(u"background-color:  rgb(255, 255, 255);\n"
"border-radius: 0px;\n"
"font: 12pt \"Segoe UI\";\n"
"color: rgb(0, 0, 0);\n"
"alignment: center;\n"
"")
        self.query1 = QPushButton(self.cautare)
        self.query1.setObjectName(u"query1")
        self.query1.setGeometry(QRect(30, 30, 150, 25))
        self.query1.setStyleSheet(u"QPushButton{background-color:  rgb(255, 255, 255);\n"
"border-radius: 0px;\n"
"font: 12pt \"Segoe UI\";\n"
"color: rgb(0, 0, 0);}\n"
"\n"
"QPushButton:hover{\n"
"border: 1px solid rgb(30,144,255);\n"
"}\n"
"")
        self.query2 = QPushButton(self.cautare)
        self.query2.setObjectName(u"query2")
        self.query2.setGeometry(QRect(230, 30, 150, 25))
        self.query2.setStyleSheet(u"QPushButton{background-color:  rgb(255, 255, 255);\n"
"border-radius: 0px;\n"
"font: 12pt \"Segoe UI\";\n"
"color: rgb(0, 0, 0);}\n"
"\n"
"QPushButton:hover{\n"
"border: 1px solid rgb(30,144,255);\n"
"}\n"
"")
        self.query3 = QPushButton(self.cautare)
        self.query3.setObjectName(u"query3")
        self.query3.setGeometry(QRect(430, 30, 150, 25))
        self.query3.setStyleSheet(u"QPushButton{background-color:  rgb(255, 255, 255);\n"
"border-radius: 0px;\n"
"font: 12pt \"Segoe UI\";\n"
"color: rgb(0, 0, 0);}\n"
"\n"
"QPushButton:hover{\n"
"border: 1px solid rgb(30,144,255);\n"
"}\n"
"")
        self.query4 = QPushButton(self.cautare)
        self.query4.setObjectName(u"query4")
        self.query4.setGeometry(QRect(630, 30, 150, 25))
        self.query4.setStyleSheet(u"QPushButton{background-color:  rgb(255, 255, 255);\n"
"border-radius: 0px;\n"
"font: 12pt \"Segoe UI\";\n"
"color: rgb(0, 0, 0);}\n"
"\n"
"QPushButton:hover{\n"
"border: 1px solid rgb(30,144,255);\n"
"}\n"
"")
        self.query5 = QPushButton(self.cautare)
        self.query5.setObjectName(u"query5")
        self.query5.setGeometry(QRect(30, 160, 150, 25))
        self.query5.setStyleSheet(u"QPushButton{background-color:  rgb(255, 255, 255);\n"
"border-radius: 0px;\n"
"font: 12pt \"Segoe UI\";\n"
"color: rgb(0, 0, 0);}\n"
"\n"
"QPushButton:hover{\n"
"border: 1px solid rgb(30,144,255);\n"
"}\n"
"")
        self.query6 = QPushButton(self.cautare)
        self.query6.setObjectName(u"query6")
        self.query6.setGeometry(QRect(230, 160, 150, 25))
        self.query6.setStyleSheet(u"QPushButton{background-color:  rgb(255, 255, 255);\n"
"border-radius: 0px;\n"
"font: 12pt \"Segoe UI\";\n"
"color: rgb(0, 0, 0);}\n"
"\n"
"QPushButton:hover{\n"
"border: 1px solid rgb(30,144,255);\n"
"}\n"
"")
        self.query7 = QPushButton(self.cautare)
        self.query7.setObjectName(u"query7")
        self.query7.setGeometry(QRect(430, 160, 150, 25))
        self.query7.setStyleSheet(u"QPushButton{background-color:  rgb(255, 255, 255);\n"
"border-radius: 0px;\n"
"font: 12pt \"Segoe UI\";\n"
"color: rgb(0, 0, 0);}\n"
"\n"
"QPushButton:hover{\n"
"border: 1px solid rgb(30,144,255);\n"
"}\n"
"")
        self.query8 = QPushButton(self.cautare)
        self.query8.setObjectName(u"query8")
        self.query8.setGeometry(QRect(630, 160, 150, 25))
        self.query8.setStyleSheet(u"QPushButton{background-color:  rgb(255, 255, 255);\n"
"border-radius: 0px;\n"
"font: 12pt \"Segoe UI\";\n"
"color: rgb(0, 0, 0);}\n"
"\n"
"QPushButton:hover{\n"
"border: 1px solid rgb(30,144,255);\n"
"}\n"
"")
        self.menu.addTab(self.cautare, "")
        self.cautare_avansata = QWidget()
        self.cautare_avansata.setObjectName(u"cautare_avansata")
        self.avioaneRegiuni = QTableWidget(self.cautare_avansata)
        if (self.avioaneRegiuni.columnCount() < 4):
            self.avioaneRegiuni.setColumnCount(4)
        __qtablewidgetitem10 = QTableWidgetItem()
        self.avioaneRegiuni.setHorizontalHeaderItem(0, __qtablewidgetitem10)
        __qtablewidgetitem11 = QTableWidgetItem()
        self.avioaneRegiuni.setHorizontalHeaderItem(1, __qtablewidgetitem11)
        __qtablewidgetitem12 = QTableWidgetItem()
        self.avioaneRegiuni.setHorizontalHeaderItem(2, __qtablewidgetitem12)
        __qtablewidgetitem13 = QTableWidgetItem()
        self.avioaneRegiuni.setHorizontalHeaderItem(3, __qtablewidgetitem13)
        self.avioaneRegiuni.setObjectName(u"avioaneRegiuni")
        self.avioaneRegiuni.setGeometry(QRect(10, 30, 551, 192))
        self.avioaneRegiuni.setStyleSheet(u"background-color:  rgb(255, 255, 255);\n"
"border-radius: 0px;\n"
"font: 12pt \"Segoe UI\";\n"
"color: rgb(0, 0, 0);\n"
"")
        self.alegereRegiune = QComboBox(self.cautare_avansata)
        self.alegereRegiune.setObjectName(u"alegereRegiune")
        self.alegereRegiune.setGeometry(QRect(630, 30, 82, 28))
        self.alegereRegiune.setStyleSheet(u"background-color:  rgb(255, 255, 255);\n"
"border-radius: 0px;\n"
"font: 12pt \"Segoe UI\";\n"
"color: rgb(0, 0, 0);\n"
"")
        self.avioanePiese = QTableWidget(self.cautare_avansata)
        if (self.avioanePiese.columnCount() < 3):
            self.avioanePiese.setColumnCount(3)
        __qtablewidgetitem14 = QTableWidgetItem()
        self.avioanePiese.setHorizontalHeaderItem(0, __qtablewidgetitem14)
        __qtablewidgetitem15 = QTableWidgetItem()
        self.avioanePiese.setHorizontalHeaderItem(1, __qtablewidgetitem15)
        __qtablewidgetitem16 = QTableWidgetItem()
        self.avioanePiese.setHorizontalHeaderItem(2, __qtablewidgetitem16)
        self.avioanePiese.setObjectName(u"avioanePiese")
        self.avioanePiese.setGeometry(QRect(10, 290, 551, 192))
        self.avioanePiese.setStyleSheet(u"background-color:  rgb(255, 255, 255);\n"
"border-radius: 0px;\n"
"font: 12pt \"Segoe UI\";\n"
"color: rgb(0, 0, 0);\n"
"")
        self.alegereAvion = QComboBox(self.cautare_avansata)
        self.alegereAvion.setObjectName(u"alegereAvion")
        self.alegereAvion.setGeometry(QRect(630, 290, 161, 28))
        self.alegereAvion.setStyleSheet(u"background-color:  rgb(255, 255, 255);\n"
"border-radius: 0px;\n"
"font: 12pt \"Segoe UI\";\n"
"color: rgb(0, 0, 0);\n"
"")
        self.menu.addTab(self.cautare_avansata, "")
        self.poza_avion = QLabel(Widget)
        self.poza_avion.setObjectName(u"poza_avion")
        self.poza_avion.setGeometry(QRect(730, 10, 61, 61))
        self.poza_avion.setPixmap(QPixmap(u"airplane.png"))

        self.retranslateUi(Widget)

        self.menu.setCurrentIndex(3)


        QMetaObject.connectSlotsByName(Widget)
    # setupUi

    def retranslateUi(self, Widget):
        Widget.setWindowTitle(QCoreApplication.translate("Widget", u"Aplica\u021bie pentru gestiunea unei companii care produce avioane", None))
        self.bunVenit.setText(QCoreApplication.translate("Widget", u"Bine a\u021bi venit!", None))
        self.introducere_operator.setText(QCoreApplication.translate("Widget", u"Introducere Operator", None))
        self.numeOperator.setText(QCoreApplication.translate("Widget", u"Nume:", None))
        self.codOperator.setText(QCoreApplication.translate("Widget", u"Cod:", None))
        self.regiuneOperator.setText(QCoreApplication.translate("Widget", u"Regiune:", None))
        self.introduOperator.setText(QCoreApplication.translate("Widget", u"Introducere", None))
        self.sterge_operator.setText(QCoreApplication.translate("Widget", u"Stergere Operator", None))
        self.numeOperatorStergere.setText(QCoreApplication.translate("Widget", u"Cod:", None))
        self.introduOperatorStergere.setText(QCoreApplication.translate("Widget", u"\u0218tergere", None))
        self.modificareOperator.setText(QCoreApplication.translate("Widget", u"Modificare Operator", None))
        self.modificareRegiuneOperator.setText(QCoreApplication.translate("Widget", u"Modificare Regiune", None))
        self.codOperatorModificareRegiune.setText(QCoreApplication.translate("Widget", u"Cod:", None))
        self.regiuneNouaOperator.setText(QCoreApplication.translate("Widget", u"Regiune nou\u0103:", None))
        self.introduNouaRegiune.setText(QCoreApplication.translate("Widget", u"Modificare", None))
        self.modificareNumeOperator.setText(QCoreApplication.translate("Widget", u"Modificare Nume", None))
        self.codOperatorModificareNume.setText(QCoreApplication.translate("Widget", u"Cod:", None))
        self.numrNouOperator.setText(QCoreApplication.translate("Widget", u"Nume nou:", None))
        self.introduNumeleNou.setText(QCoreApplication.translate("Widget", u"Modificare", None))
        ___qtablewidgetitem = self.afisareOperatori.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("Widget", u"Nume", None));
        ___qtablewidgetitem1 = self.afisareOperatori.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("Widget", u"Cod", None));
        ___qtablewidgetitem2 = self.afisareOperatori.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("Widget", u"Regiune", None));
        self.menu.setTabText(self.menu.indexOf(self.operatori), QCoreApplication.translate("Widget", u"Operatori Aerieni", None))
        self.adaugareAvion.setText(QCoreApplication.translate("Widget", u"Ad\u0103ugare", None))
        self.stergereAvion.setText(QCoreApplication.translate("Widget", u"\u0218tergere", None))
        ___qtablewidgetitem3 = self.tabelAvioane.horizontalHeaderItem(0)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("Widget", u"Nume", None));
        ___qtablewidgetitem4 = self.tabelAvioane.horizontalHeaderItem(1)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("Widget", u"Departament", None));
        ___qtablewidgetitem5 = self.tabelAvioane.horizontalHeaderItem(2)
        ___qtablewidgetitem5.setText(QCoreApplication.translate("Widget", u"Cod", None));
        ___qtablewidgetitem6 = self.tabelAvioane.horizontalHeaderItem(3)
        ___qtablewidgetitem6.setText(QCoreApplication.translate("Widget", u"Cost Produc\u021bie", None));
        ___qtablewidgetitem7 = self.tabelAvioane.horizontalHeaderItem(4)
        ___qtablewidgetitem7.setText(QCoreApplication.translate("Widget", u"Pre\u021b", None));
        ___qtablewidgetitem8 = self.tabelAvioane.horizontalHeaderItem(5)
        ___qtablewidgetitem8.setText(QCoreApplication.translate("Widget", u"Vitez\u0103", None));
        ___qtablewidgetitem9 = self.tabelAvioane.horizontalHeaderItem(6)
        ___qtablewidgetitem9.setText(QCoreApplication.translate("Widget", u"Locuri", None));
        self.modificareAvion.setText(QCoreApplication.translate("Widget", u"Modificare", None))
        self.menu.setTabText(self.menu.indexOf(self.avioane), QCoreApplication.translate("Widget", u"Avioane", None))
        self.query1.setText(QCoreApplication.translate("Widget", u"Piese Avion A320", None))
        self.query2.setText(QCoreApplication.translate("Widget", u"Avioane V\u00e2ndute", None))
        self.query3.setText(QCoreApplication.translate("Widget", u"Cump\u0103rate 2023", None))
        self.query4.setText(QCoreApplication.translate("Widget", u"Peste 200 Locuri", None))
        self.query5.setText(QCoreApplication.translate("Widget", u"Cost Mediu", None))
        self.query6.setText(QCoreApplication.translate("Widget", u"Cel Mai Rapid", None))
        self.query7.setText(QCoreApplication.translate("Widget", u"Profit 2023", None))
        self.query8.setText(QCoreApplication.translate("Widget", u"F\u0103r\u0103 Achizitii", None))
        self.menu.setTabText(self.menu.indexOf(self.cautare), QCoreApplication.translate("Widget", u"C\u0103utare", None))
        ___qtablewidgetitem10 = self.avioaneRegiuni.horizontalHeaderItem(0)
        ___qtablewidgetitem10.setText(QCoreApplication.translate("Widget", u"Nume Avion", None));
        ___qtablewidgetitem11 = self.avioaneRegiuni.horizontalHeaderItem(1)
        ___qtablewidgetitem11.setText(QCoreApplication.translate("Widget", u"Cod Avion", None));
        ___qtablewidgetitem12 = self.avioaneRegiuni.horizontalHeaderItem(2)
        ___qtablewidgetitem12.setText(QCoreApplication.translate("Widget", u"Regiune", None));
        ___qtablewidgetitem13 = self.avioaneRegiuni.horizontalHeaderItem(3)
        ___qtablewidgetitem13.setText(QCoreApplication.translate("Widget", u"Data V\u00e2nzare", None));
        ___qtablewidgetitem14 = self.avioanePiese.horizontalHeaderItem(0)
        ___qtablewidgetitem14.setText(QCoreApplication.translate("Widget", u"Nume Avion", None));
        ___qtablewidgetitem15 = self.avioanePiese.horizontalHeaderItem(1)
        ___qtablewidgetitem15.setText(QCoreApplication.translate("Widget", u"Cod Avion", None));
        ___qtablewidgetitem16 = self.avioanePiese.horizontalHeaderItem(2)
        ___qtablewidgetitem16.setText(QCoreApplication.translate("Widget", u"Total Piese", None));
        self.menu.setTabText(self.menu.indexOf(self.cautare_avansata), QCoreApplication.translate("Widget", u"C\u0103utare Avansat\u0103", None))
        self.poza_avion.setText("")
    # retranslateUi

