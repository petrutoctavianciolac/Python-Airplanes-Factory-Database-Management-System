#Importarea librariilor necesare
from PySide6.QtCore import Qt, Signal
import sys
from PySide6.QtWidgets import *
from PySide6.QtGui import QIcon, QFont
from ui_adaugare import Ui_Widget
from ui_stergere import Ui_WidgetS
from ui_modificare import Ui_WidgetM

#Freastra folosită pentru adăugare
class AddPlane(QDialog):
    def __init__(self):
        super().__init__()
        
        self.ui = Ui_Widget()
        self.ui.setupUi(self)
        self.setWindowTitle("Adăugare Avion")
        self.setWindowIcon(QIcon("airplane.png"))

        #Funcția care face posibilă folosirea getterelor
        self.ui.adaugareAvion.clicked.connect(self.on_add_clicked)
        
    
    def on_add_clicked(self):
        self.accept()
    
    def getNume(self):
        return self.ui.iNumeAvion.text()
    
    def getCod(self):
        return self.ui.iCodAvion.text()
    
    def getCost(self):
        return self.ui.iCost.text()
    
    def getPret(self):
        return self.ui.iPret.text()
    
    def getViteza(self):
        return self.ui.iViteza.text()
    
    def getLocuri(self):
        return self.ui.iLocuri.text()
    
    def getDepartament(self):
        return self.ui.iDepartament.currentText()
    
    #Gettere folosite pentru a luat din inferfață inputurile
    
    def setDepartamente(self, departamenete):
        for departament in departamenete:
            self.ui.iDepartament.addItem(departament[0])
    #Setter folosit pentru a popula drop-down list-ul cu departamentele existente
    
#Fereastră folosită pentru ștergere
class DelPlane(QDialog):
    def __init__(self):
        super().__init__()

        self.ui = Ui_WidgetS()
        self.ui.setupUi(self)
        self.setWindowTitle("Ștergere Avion")
        self.setWindowIcon(QIcon("airplane.png"))

        #Funcția care face posibilă folosirea getCod
        self.ui.stergereAvion.clicked.connect(self.on_dell_clicked)
    
    def getCod(self):
        return self.ui.iCod.text()
        #Getter care ia codul din interfața grafică
    
    def on_dell_clicked(self):
        self.accept()

#Fereastră folosită pentru modificare
class ModPlane(QDialog):
    def __init__(self):
        super().__init__()

        self.ui = Ui_WidgetM()
        self.ui.setupUi(self)
        self.setWindowTitle("Modificare Avion")
        self.setWindowIcon(QIcon("airplane.png"))

        #Funcția care face posibilă folosirea getterelor
        self.ui.modificareAvion.clicked.connect(self.on_mod_clicked)

    def on_mod_clicked(self):
        self.accept()
    
    def setDepartamente(self, departamente):
        self.ui.iDepartament.addItem("")
        for departament in departamente:
            self.ui.iDepartament.addItem(departament[0])
    
    #Setter folosit pentru a popula drop-down list-ul cu departamentele existente
    
    def getNume(self):
        return self.ui.iNumeAvion.text()
    
    def getCod(self):
        return self.ui.iCodAvion.text()
    
    def getCost(self):
        return self.ui.iCost.text()
    
    def getPret(self):
        return self.ui.iPret.text()
    
    def getViteza(self):
        return self.ui.iViteza.text()
    
    def getLocuri(self):
        return self.ui.iLocuri.text()
    
    def getDepartament(self):
        return self.ui.iDepartament.currentText()
    #Gettere folosite pentru a luat din inferfață inputurile