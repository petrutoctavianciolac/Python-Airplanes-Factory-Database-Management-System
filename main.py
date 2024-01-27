#Importarea librariilor necesare
import sys
import pyodbc as odbc
from PySide6.QtWidgets import QApplication, QWidget, QTableWidgetItem, QDialog
from PySide6.QtCore import QTimer
from config import db, server, driver
from login import LoginWindow
from plane_config import AddPlane, DelPlane, ModPlane
from ui_form import Ui_Widget

#Clasa care defineste fereastra principală
class MainWindow(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        
        self.ui = Ui_Widget()
        self.ui.setupUi(self) #Importarea partii de front end

        #Evenimentele puse pe butoane pentru a adauga, modifica sau șterge înregistrări din tabel OperatoriAerieni
        self.ui.introduOperator.clicked.connect(self.addOperator)
        self.ui.introduOperatorStergere.clicked.connect(self.delOperator)
        self.ui.introduNumeleNou.clicked.connect(self.modNumeOperator)
        self.ui.introduNouaRegiune.clicked.connect(self.modRegiuneOperator)

        #Evenimentele puse pe butoane pentru a afișa cererile fară parametrii variabili
        self.ui.query1.clicked.connect(self.afisareJoinPiese)
        self.ui.query2.clicked.connect(self.afisareJoinVenit)
        self.ui.query3.clicked.connect(self.afisareJoinCantitate)
        self.ui.query4.clicked.connect(self.afisareJoinLocuri)
        self.ui.query5.clicked.connect(self.afisareJoinCostMediu)
        self.ui.query6.clicked.connect(self.afisareDupaViteza)
        self.ui.query7.clicked.connect(self.afisareDupaProfit)
        self.ui.query8.clicked.connect(self.afisareOperatoriZgarciti)

        #Eveniment care se declanseaza odata la 3 secunde pentru a actualiza tabelul Operatori Aerieni 
        #cu datele care eventual au fost modificate
        self.timer_operatori = QTimer(self)
        self.timer_operatori.start(3000)
        self.timer_operatori.timeout.connect(self.actualizareOperatori)

        #Evenimentele puse pe butoane pentru a adăuga, modifica sau șterge înregistrări din tabel Avioane
        self.ui.adaugareAvion.clicked.connect(self.addAvion)
        self.ui.stergereAvion.clicked.connect(self.delAvion)
        self.ui.modificareAvion.clicked.connect(self.modAvion)

        #Eveniment care se declanseaza odata la 3 secunde pentru a actualiza tabelul Avioane 
        #cu datele care eventual au fost modificate
        self.timer_avioane = QTimer(self)
        self.timer_avioane.start(3000)
        self.timer_avioane.timeout.connect(self.actulizareAvioane)

        #Eveniment care se declanseaza odata la 3 secunde pentru a actualiza tabelul în care se afisează
        #rezultatele cererii JOIN cu parametru variabil în funcție de ce regiune a fost aleasă in drop-down list
        self.timer_avioaneRegiune = QTimer(self)
        self.timer_avioaneRegiune.start(3000)
        self.timer_avioaneRegiune.timeout.connect(self.afisareAvioaneRegiune)

        #Popularea drop-down list-ului cu regiunile care sunt prezenta în baza de date
        q_operatori = "SELECT DISTINCT Regiune FROM dbo.OperatoriAerieni;"
        cursor.execute(q_operatori)
        operatori = cursor.fetchall()
        self.ui.alegereRegiune.addItem("")
        for operator in operatori:
            self.ui.alegereRegiune.addItem(operator[0])

        #Eveniment care se declanseaza odata la 3 secunde pentru a actualiza tabelul în care se afisează
        #rezultatele subquery cu parametru variabil în funcție de ce avion a fost ales in drop-down list
        self.timer_avioanePiese = QTimer(self)
        self.timer_avioanePiese.start(3000)
        self.timer_avioanePiese.timeout.connect(self.afisareAvioaneDupaPiese)

        #Popularea drop-down list-ului cu avioanele care sunt prezente în baza de date
        q_avioane = "SELECT NumeAvion FROM dbo.Avioane;"
        cursor.execute(q_avioane)
        avioane = cursor.fetchall()

        self.ui.alegereAvion.addItem("")
        for avion in avioane:
            self.ui.alegereAvion.addItem(avion[0])

        #Setare layout tabel pentru a se vedea output-ul cât mai bine
        self.ui.avioaneRegiuni.setColumnWidth(0, self.ui.avioaneRegiuni.width()/3.3)
        self.ui.avioaneRegiuni.setColumnWidth(1, self.ui.avioaneRegiuni.width()/5)
        self.ui.avioaneRegiuni.setColumnWidth(2, self.ui.avioaneRegiuni.width()/7.5)
        self.ui.avioaneRegiuni.setColumnWidth(3, self.ui.avioaneRegiuni.width()/3)

        #Setare layout tabel pentru a se vedea output-ul cât mai bine
        self.ui.avioanePiese.setColumnWidth(0, self.ui.avioanePiese.width() / 2.3)
        self.ui.avioanePiese.setColumnWidth(1, self.ui.avioanePiese.width() / 3.54)
        self.ui.avioanePiese.setColumnWidth(2, self.ui.avioanePiese.width() / 4)
        
        #Afișarea inițială a tabelei OperatoriAerieni atunci când e deschisă aplicația
        q_operatori = "SELECT * FROM dbo.OperatoriAerieni;"
        cursor.execute(q_operatori)
        operatori = cursor.fetchall()

        #Setare layout tabel pentru a se vedea output-ul cât mai bine
        self.ui.avioaneRegiuni.setColumnWidth(0, self.ui.avioaneRegiuni.width() / 2.8)
        self.ui.avioaneRegiuni.setColumnWidth(1, self.ui.avioaneRegiuni.width() / 5.4)
        self.ui.avioaneRegiuni.setColumnWidth(2, self.ui.avioaneRegiuni.width() / 7)
        self.ui.avioaneRegiuni.setColumnWidth(3, self.ui.avioaneRegiuni.width() / 3.3)

        #Setare layout tabel pentru a se vedea output-ul cât mai bine
        self.ui.afisareOperatori.setRowCount(len(operatori))
        self.ui.afisareOperatori.setColumnWidth(0, self.ui.afisareOperatori.width()/2.8)
        self.ui.afisareOperatori.setColumnWidth(1, self.ui.afisareOperatori.width()/3.17)
        self.ui.afisareOperatori.setColumnWidth(2, self.ui.afisareOperatori.width()/4.3)
        
        #Popularea tabelului din interfață cu valorile din tabel OperatoriAerieni
        counter = 0
        for operator in operatori:
            self.ui.afisareOperatori.setItem(counter, 0, QTableWidgetItem(operator[1]))
            self.ui.afisareOperatori.setItem(counter, 1, QTableWidgetItem(operator[2]))
            self.ui.afisareOperatori.setItem(counter, 2, QTableWidgetItem(operator[3]))
            counter = counter + 1
        
        #Afișarea inițială a tabelei Avioane atunci când e deschisă aplicația
        q_avioane = "SELECT DepartamentID, NumeAvion, CodAvion, CostProductie, Pret, VitezaMaxima, NumarLocuri FROM dbo.Avioane;"
        cursor.execute(q_avioane)
        avioane = cursor.fetchall()

        #Setare layout tabel pentru a se vedea output-ul cât mai bine
        self.ui.tabelAvioane.setRowCount(len(avioane))
        self.ui.tabelAvioane.setColumnWidth(0, self.ui.tabelAvioane.width() / 4.1)
        self.ui.tabelAvioane.setColumnWidth(1, self.ui.tabelAvioane.width() / 6.7)
        self.ui.tabelAvioane.setColumnWidth(2, self.ui.tabelAvioane.width() / 7.4)
        self.ui.tabelAvioane.setColumnWidth(3, self.ui.tabelAvioane.width() / 7.2)
        self.ui.tabelAvioane.setColumnWidth(4, self.ui.tabelAvioane.width() / 7)
        self.ui.tabelAvioane.setColumnWidth(5, self.ui.tabelAvioane.width() / 15)
        self.ui.tabelAvioane.setColumnWidth(6, self.ui.tabelAvioane.width() / 15)

        counter = 0

        #Popularea tabelului din interfață cu valorile din tabelul Avioane 
        for avion in avioane:
            
            #Se face o cererea pentru a se obține numele departamentului având cheia externă
            q_departamenete = "SELECT NumeDepartament FROM dbo.Departamente WHERE DepartamentID = " + str(avion[0]) + ";"
            cursor.execute(q_departamenete)
            departament = cursor.fetchall()

            self.ui.tabelAvioane.setItem(counter, 1, QTableWidgetItem(departament[0][0]))
            self.ui.tabelAvioane.setItem(counter, 0, QTableWidgetItem(avion[1]))
            self.ui.tabelAvioane.setItem(counter, 2, QTableWidgetItem(avion[2]))
            self.ui.tabelAvioane.setItem(counter, 3, QTableWidgetItem(str(avion[3])))
            self.ui.tabelAvioane.setItem(counter, 4, QTableWidgetItem(str(avion[4])))
            self.ui.tabelAvioane.setItem(counter, 5, QTableWidgetItem(str(avion[5])))
            self.ui.tabelAvioane.setItem(counter, 6, QTableWidgetItem(str(avion[6])))
            counter = counter + 1 

    def afisareJoinPiese(self):

        q_piese = """SELECT P.NumePiesa, PA.NumarPieseNecesare FROM dbo.Piese P
                    INNER JOIN dbo.PieseAvioane PA
                    ON P.PiesaID = PA.PiesaID
                    INNER JOIN Avioane A
                    ON PA.AvionID = A.AvionID
                    WHERE A.NumeAvion = 'Airbus A320';"""
        #Cerere care se realizează cu ajutorul JOIN. Afișează toate piesele necesare și cantitatea lor
        #care sunt folosite pentru Airbus A320 

        cursor.execute(q_piese)
        piese = cursor.fetchall()
        
        #Setare layout tabel pentru a se vedea output-ul cât mai bine
        self.ui.tabelCautare.setColumnCount(2)
        self.ui.tabelCautare.setHorizontalHeaderLabels(["Nume Piesă", "Număr"])
        self.ui.tabelCautare.setRowCount(len(piese))
        self.ui.tabelCautare.setColumnWidth(0, self.ui.tabelCautare.width() / 2)
        self.ui.tabelCautare.setColumnWidth(1, self.ui.tabelCautare.width() / 2.15)

        counter = 0

        #Popularea tabelului din interfață cu valorile obținute din query
        for piesa in piese:
            self.ui.tabelCautare.setItem(counter, 0, QTableWidgetItem(piesa[0]))
            self.ui.tabelCautare.setItem(counter, 1, QTableWidgetItem(str(piesa[1])))

            counter = counter + 1


    def afisareJoinVenit(self):

        q_venit = """SELECT A.NumeAvion, SUM(AC.Cantitate * A.Pret) AS 'Venit' FROM dbo.Avioane A
                     INNER JOIN dbo.AvioaneCumparate AC
                     ON A.AvionID = AC.AvionID
                     GROUP BY A.NumeAvion
                     ORDER BY Venit DESC;"""
        #Cerere care se realizează cu ajutorul JOIN. Afișează toate modele de avion vândute alături de venitul
        #încasat din toate vânzările sortate descendent după banii încasați

        cursor.execute(q_venit)
        venit = cursor.fetchall()

        #Setare layout tabel pentru a se vedea output-ul cât mai bine
        self.ui.tabelCautare.setColumnCount(2)
        self.ui.tabelCautare.setHorizontalHeaderLabels(["Nume Avion", "Venit"])
        self.ui.tabelCautare.setRowCount(len(venit))
        self.ui.tabelCautare.setColumnWidth(0, self.ui.tabelCautare.width() / 2)
        self.ui.tabelCautare.setColumnWidth(1, self.ui.tabelCautare.width() / 2.15)

        counter = 0

        #Popularea tabelului din interfață cu valorile obținute din query
        for ven in venit:
            self.ui.tabelCautare.setItem(counter, 0, QTableWidgetItem(ven[0]))
            self.ui.tabelCautare.setItem(counter, 1, QTableWidgetItem(str(ven[1])))

            counter = counter + 1


    def afisareJoinCantitate(self):
        
        q_cantitate = """SELECT DISTINCT A.NumeAvion, A.Pret, SUM(AC.Cantitate) AS 'CantiateTotala' FROM dbo.Avioane A
                         INNER JOIN dbo.AvioaneCumparate AC
                         ON A.AvionID = AC.AvionID
                         WHERE YEAR(AC.DataCumpararii) = 2023
                         GROUP BY A.NumeAvion, A.Pret
                         ORDER BY CantiateTotala DESC;"""
        #Cerere care se realizează cu ajutorul JOIN. Afișează modelele de avion, prețul și cantitatea totală vândute
        #în 2023 ordonate crescător după cantitate.
        cursor.execute(q_cantitate)
        cantitate = cursor.fetchall()

        #Setare layout tabel pentru a se vedea output-ul cât mai bine
        self.ui.tabelCautare.setColumnCount(3)
        self.ui.tabelCautare.setHorizontalHeaderLabels(["Nume Avion", "Preț", "Cantitate Totală"])
        self.ui.tabelCautare.setRowCount(len(cantitate))
        self.ui.tabelCautare.setColumnWidth(0, self.ui.tabelCautare.width() / 3)
        self.ui.tabelCautare.setColumnWidth(1, self.ui.tabelCautare.width() / 3)
        self.ui.tabelCautare.setColumnWidth(2, self.ui.tabelCautare.width() / 3.3)

        counter = 0

        #Popularea tabelului din interfață cu valorile obținute din query
        for cant in cantitate:
            self.ui.tabelCautare.setItem(counter, 0, QTableWidgetItem(cant[0]))
            self.ui.tabelCautare.setItem(counter, 1, QTableWidgetItem(str(cant[1])))
            self.ui.tabelCautare.setItem(counter, 2, QTableWidgetItem(str(cant[2])))

            counter = counter + 1

    def afisareJoinLocuri(self):
        
        q_locuri = """SELECT D.NumeDepartament, COUNT(A.AvionID) AS 'NumarAvioane' FROM dbo.Departamente D
                     INNER JOIN dbo.Avioane A
                     ON D.DepartamentID = A.DepartamentID
                     WHERE A.NumarLocuri > 200
                     GROUP BY D.NumeDepartament;"""
        #Cerere care se realizează cu ajutorul JOIN. Afișează departamentele care produc avioane cu mai mult de
        #200 de locuri. Alături de departament și numărul de astfel de avioane din fiecare departament

        cursor.execute(q_locuri)
        locuri = cursor.fetchall()

        #Setare layout tabel pentru a se vedea output-ul cât mai bine
        self.ui.tabelCautare.setColumnCount(2)
        self.ui.tabelCautare.setHorizontalHeaderLabels(["Nume Departament", "Număr Avioane"])
        self.ui.tabelCautare.setRowCount(len(locuri))
        self.ui.tabelCautare.setColumnWidth(0, self.ui.tabelCautare.width() / 2)
        self.ui.tabelCautare.setColumnWidth(1, self.ui.tabelCautare.width() / 2.15)

        counter = 0

        #Popularea tabelului din interfață cu valorile obținute din query
        for loc in locuri:
            self.ui.tabelCautare.setItem(counter, 0, QTableWidgetItem(loc[0]))
            self.ui.tabelCautare.setItem(counter, 1, QTableWidgetItem(str(loc[1])))

            counter = counter + 1


    def afisareJoinCostMediu(self):

        q_cost = """SELECT D.NumeDepartament, AVG(A.CostProductie) AS 'CostMediu' FROM dbo.Departamente D
                    INNER JOIN dbo.Avioane A
                    ON D.DepartamentID = A.DepartamentID
                    GROUP BY D.NumeDepartament
                    HAVING AVG(A.CostProductie) >= 20000000
                    ORDER BY CostMediu;"""
        #Cerere care se realizează cu ajutorul JOIN. Se afișează departamentele care au cost mediu de producție
        #a modelelor de avioane > 20.000.000. Se afișează alături și costul mediu.

        cursor.execute(q_cost)
        cost = cursor.fetchall()

        #Setare layout tabel pentru a se vedea output-ul cât mai bine
        self.ui.tabelCautare.setColumnCount(2)
        self.ui.tabelCautare.setHorizontalHeaderLabels(["Nume Departament", "Cost Mediu"])
        self.ui.tabelCautare.setRowCount(len(cost))
        self.ui.tabelCautare.setColumnWidth(0, self.ui.tabelCautare.width() / 2)
        self.ui.tabelCautare.setColumnWidth(1, self.ui.tabelCautare.width() / 2.15)

        counter = 0

        #Popularea tabelului din interfață cu valorile obținute din query
        for cos in cost:
            self.ui.tabelCautare.setItem(counter, 0, QTableWidgetItem(cos[0]))
            self.ui.tabelCautare.setItem(counter, 1, QTableWidgetItem(str(cos[1])))

            counter = counter + 1

    
    def afisareDupaViteza(self):
        
        q_viteza = """SELECT A.NumeAvion, A.CodAvion, A.VitezaMaxima, D.NumeDepartament FROM dbo.Avioane A
                      INNER JOIN dbo.Departamente D
                      ON A.DepartamentID = D.DepartamentID
                      WHERE A.VitezaMaxima IN ( SELECT MAX(A1.VitezaMaxima) FROM dbo.Avioane A1
                      WHERE A1.DepartamentID = A.DepartamentID)
                      ORDER BY A.VitezaMaxima DESC;"""
        #Cerere care se realizează cu SUBQUERY. Se afișează avionul cu cea mai mare viteză din fiecare departament
        #alături de departament se afișează și viteza maximă și departamentul.

        cursor.execute(q_viteza)
        viteze = cursor.fetchall()

        #Setare layout tabel pentru a se vedea output-ul cât mai bine
        self.ui.tabelCautare.setColumnCount(4)
        self.ui.tabelCautare.setHorizontalHeaderLabels(["Nume Avion", "Cod Avion", "Viteză", "Departament"])
        self.ui.tabelCautare.setRowCount(len(viteze))
        self.ui.tabelCautare.setColumnWidth(0, self.ui.tabelCautare.width() / 2.65)
        self.ui.tabelCautare.setColumnWidth(1, self.ui.tabelCautare.width() / 5)
        self.ui.tabelCautare.setColumnWidth(2, self.ui.tabelCautare.width() / 7)
        self.ui.tabelCautare.setColumnWidth(3, self.ui.tabelCautare.width() / 4.1)

        counter = 0

        #Popularea tabelului din interfață cu valorile obținute din query
        for viteza in viteze:
            self.ui.tabelCautare.setItem(counter, 0, QTableWidgetItem(viteza[0]))
            self.ui.tabelCautare.setItem(counter, 1, QTableWidgetItem(viteza[1]))
            self.ui.tabelCautare.setItem(counter, 2, QTableWidgetItem(str(viteza[2])))
            self.ui.tabelCautare.setItem(counter, 3, QTableWidgetItem(viteza[3]))

            counter = counter + 1


    def afisareDupaProfit(self):

        q_profit = """SELECT A.NumeAvion, D.NumeDepartament, A.Pret - A.CostProductie AS 'Profit' FROM dbo.Avioane A
                      INNER JOIN dbo.Departamente D
                      ON A.DepartamentID = D.DepartamentID
                      INNER JOIN dbo.AvioaneCumparate AC
                      ON A.AvionID = AC.AvionID
                      WHERE YEAR(AC.DataCumpararii) = 2023 AND A.Pret - A.CostProductie IN 
                      (SELECT MAX(A1.Pret - A1.CostProductie) FROM dbo.Avioane A1
                      WHERE A1.DepartamentID = D.DepartamentID);"""
        #Cerere care se realizează cu SUBQUERY. Se afișează avionul care produce cel mai mare profit(Pret - CostProductie)
        #din fiecare departament ce a fost vândut in 2023.

        cursor.execute(q_profit)
        profituri = cursor.fetchall()

        #Setare layout tabel pentru a se vedea output-ul cât mai bine
        self.ui.tabelCautare.setColumnCount(3)
        self.ui.tabelCautare.setHorizontalHeaderLabels(["Nume Avion", "Nume Departament", "Profit"])
        self.ui.tabelCautare.setRowCount(len(profituri))
        self.ui.tabelCautare.setColumnWidth(0, self.ui.tabelCautare.width() / 2.3)
        self.ui.tabelCautare.setColumnWidth(1, self.ui.tabelCautare.width() / 3.54)
        self.ui.tabelCautare.setColumnWidth(2, self.ui.tabelCautare.width() / 4)

        counter = 0

        #Popularea tabelului din interfață cu valorile obținute din query
        for profit in profituri:
            self.ui.tabelCautare.setItem(counter, 0, QTableWidgetItem(profit[0]))
            self.ui.tabelCautare.setItem(counter, 1, QTableWidgetItem(profit[1]))
            self.ui.tabelCautare.setItem(counter, 2, QTableWidgetItem(str(profit[2])))

            counter = counter + 1

    def afisareOperatoriZgarciti(self):

        q_operatori = """SELECT NumeOperatorAerian, Regiune
                         FROM dbo.OperatoriAerieni
                         WHERE OperatorAerianID NOT IN (
                         SELECT DISTINCT OperatorAerianID
                         FROM dbo.AvioaneCumparate);"""
        #Cerere care se realizează cu SUBQUERY. Afișează toți operatorii aerieni care nu au cumpărat
        #niciun avion până acum.

        cursor.execute(q_operatori)
        operatori = cursor.fetchall()

        #Setare layout tabel pentru a se vedea output-ul cât mai bine
        self.ui.tabelCautare.setColumnCount(2)
        self.ui.tabelCautare.setHorizontalHeaderLabels(["Nume Operator", "Regiune"])
        self.ui.tabelCautare.setRowCount(len(operatori))
        self.ui.tabelCautare.setColumnWidth(0, self.ui.tabelCautare.width() / 2)
        self.ui.tabelCautare.setColumnWidth(1, self.ui.tabelCautare.width() / 2.15)

        counter = 0

        #Popularea tabelului din interfață cu valorile obținute din query
        for operator in operatori:
            self.ui.tabelCautare.setItem(counter, 0, QTableWidgetItem(operator[0]))
            self.ui.tabelCautare.setItem(counter, 1, QTableWidgetItem(operator[1]))

            counter = counter + 1



    def afisareAvioaneRegiune(self):

        regiune = self.ui.alegereRegiune.currentText()
        q_avioaneRegiuni = """SELECT A.NumeAvion, A.CodAvion, OA.Regiune, AC.DataCumpararii FROM dbo.Avioane A
                              INNER JOIN dbo.AvioaneCumparate AC
                              ON A.AvionID = AC.AvionID
                              INNER JOIN dbo.OperatoriAerieni OA
                              ON AC.OperatorAerianID = OA.OperatorAerianID
                              WHERE OA.Regiune = '{}';""".format(regiune)
        #Cerere care se realizează cu ajutorul JOIN cu parametrii. Afișează numele și codul avioanelor care au fost
        #vândute către un operator aerian dintr-o regiune dată ca input(Am defnit drop-down list-ul cu regiunile
        #existente în baza de date la început). Afișarea se va face alături de regiune și data vânzării.
        
        cursor.execute(q_avioaneRegiuni)
        resultsAvioaneRegiuni = cursor.fetchall()

        self.ui.avioaneRegiuni.setRowCount(len(resultsAvioaneRegiuni))

        counter = 0

        #Popularea tabelului din interfață cu valorile obținute din query
        for avion in resultsAvioaneRegiuni:
            self.ui.avioaneRegiuni.setItem(counter, 0, QTableWidgetItem(str(avion[0])))
            self.ui.avioaneRegiuni.setItem(counter, 1, QTableWidgetItem(str(avion[1])))
            self.ui.avioaneRegiuni.setItem(counter, 2, QTableWidgetItem(str(avion[2])))
            self.ui.avioaneRegiuni.setItem(counter, 3, QTableWidgetItem(str(avion[3])))

            counter = counter + 1
    
    def afisareAvioaneDupaPiese(self):
        
        avion = self.ui.alegereAvion.currentText()
        q_avion = """SELECT A.NumeAvion, A.CodAvion, SUM(PA.NumarPieseNecesare) AS 'Total Piese' FROM dbo.Avioane A
                     INNER JOIN dbo.PieseAvioane PA
                     ON A.AvionID = PA.AvionID
                     GROUP BY A.AvionID, A.NumeAvion, A.CodAvion
                     HAVING SUM(PA.NumarPieseNecesare) > 
                     (SELECT COALESCE(SUM(PA1.NumarPieseNecesare), 0) FROM dbo.PieseAvioane PA1
                     INNER JOIN dbo.Avioane A1
                     ON PA1.AvionID = A1.AvionID
                     WHERE A1.NumeAvion = '{}');""".format(avion)
        
        #Cerere care se realizează cu SUBQUERY cu parametru variabil. Afișează toate avioanele care folosesc mai multe
        #piese decât avionul dat ca input din drop-down list alături de numărul de piese necesare pentru fiecare avion
        
        cursor.execute(q_avion)
        avioane = cursor.fetchall()

        self.ui.avioanePiese.setRowCount(len(avioane))

        counter = 0

        #Popularea tabelului din interfață cu valorile obținute din query
        for avion in avioane:
            self.ui.avioanePiese.setItem(counter, 0, QTableWidgetItem(avion[0]))
            self.ui.avioanePiese.setItem(counter, 1, QTableWidgetItem(avion[1]))
            self.ui.avioanePiese.setItem(counter, 2, QTableWidgetItem(str(avion[2])))

            counter = counter + 1


    def addAvion(self):

        #Funcție pentru adăugarea unei noi înregistrări în tabela Avioane
        add_plane = AddPlane()
        add_plane.show()
        #Se deschide o nouă fereastră definită în plane_config.py

        q_departamente = "SELECT NumeDepartament FROM dbo.Departamente;"
        cursor.execute(q_departamente)
        departamenete = cursor.fetchall()
        add_plane.setDepartamente(departamenete)
        #Se completează drop-down list-ul din care se alege departamentul noului avion cu numele tuturor 
        #departamentelor existent în baza de date

        if add_plane.exec() == AddPlane.Accepted:
            nume = add_plane.getNume()
            cod = add_plane.getCod()
            cost = add_plane.getCost()
            cost = str(cost)
            pret = add_plane.getPret()
            pret = str(pret)
            viteza = add_plane.getViteza()
            viteza = str(viteza)
            capacitate = add_plane.getLocuri()
            capacitate = str(capacitate)
            departament = add_plane.getDepartament()
            #Se citesc valorile date ca input.

            #Având departamentul ales din drop-down list se face o cerere pentru a obține cheia
            #aferentă departamentului ales pentru a fi introdusă drept cheie externă în noua înregistrare
            q_departamente = "SELECT DepartamentID FROM dbo.Departamente WHERE NumeDepartament = '" + str(departament) +"';"
            cursor.execute(q_departamente)
            departament = cursor.fetchall()
            
            #Se inserează noua înregistrare în tabela avioane
            q_departamente = """INSERT INTO dbo.Avioane (DepartamentID, NumeAvion, CodAvion, CostProductie, Pret, VitezaMaxima, NumarLocuri)
            VALUES ("""+str(departament[0][0])+""",'""" + str(nume) +"""', '"""+ str(cod) + """',""" + cost + """,""" +pret+ """,""" +viteza+ """,""" +capacitate+ """);"""
            cursor.execute(q_departamente)
            conn.commit()

    def delAvion(self):
        del_plane = DelPlane()
        del_plane.show()
        #Se deschide o nouă fereastră definită în plane_config.py

        if del_plane.exec() == DelPlane.Accepted:
            cod_delete = del_plane.getCod()
            #Ștergerea se va face după cod
            #Se șterge din baza de date înregistrarea din Avioane cu codul introdus
            if cod_delete != "":
                q_departamente = "DELETE FROM dbo.Avioane WHERE CodAvion = '" + cod_delete + "';"
                cursor.execute(q_departamente)
                conn.commit()
    
    def modAvion(self):
        mod_plane = ModPlane()
        mod_plane.show()
        #Se deschide o nouă fereastră definită în plane_config.py

        #Se completează drop-down list-ul din care se alege departamentul cel nou cu numele tuturor 
        #departamentelor existent în baza de date
        q_departamente = "SELECT NumeDepartament FROM Departamente;"
        cursor.execute(q_departamente)
        departamente = cursor.fetchall()
        mod_plane.setDepartamente(departamente)

        if mod_plane.exec() == ModPlane.Accepted:
            nume = mod_plane.getNume()
            cod = mod_plane.getCod()
            cost = mod_plane.getCost()
            pret = mod_plane.getPret()
            pret = str(pret)
            viteza = mod_plane.getViteza()
            viteza = str(viteza)
            capacitate = mod_plane.getLocuri()
            capacitate = str(capacitate)
            departament = mod_plane.getDepartament()
            #Se iau valorile introduse
            
            #Codul trebuie să existe, deoarece modificare se va face după cod, acesta fiind unic
            if cod != "":
                if nume != "":
                
            #Pentru a putea fi modificate doar anumite câmpuri din înregistare se face operația de UPDATE pe rând
                    q_modificare = "UPDATE dbo.Avioane SET NumeAvion = '" + nume + "' WHERE CodAvion = '" + cod + "';"
                    cursor.execute(q_modificare)
                    cursor.commit()

                if cost != "":
                    cost = str(cost)
                    q_modificare = "UPDATE dbo.Avioane SET CostProductie = " + cost + " WHERE CodAvion = '" + cod + "';"
                    cursor.execute(q_modificare)
                    cursor.commit()
                
                if pret != "":
                    pret = str(pret)
                    q_modificare = "UPDATE dbo.Avioane SET Pret = " + pret + " WHERE CodAvion = '" + cod + "';"
                    cursor.execute(q_modificare)
                    cursor.commit()
                
                if viteza != "":
                    viteza = str(viteza)
                    q_modificare = "UPDATE dbo.Avioane SET VitezaMaxima = " + viteza + " WHERE CodAvion = '" + cod + "';"
                    cursor.execute(q_modificare)
                    cursor.commit()
                
                if capacitate != "":
                    capacitate = str(capacitate)
                    q_modificare = "UPDATE dbo.Avioane SET NumarLocuri = " + capacitate + " WHERE CodAvion = '" + cod + "';"
                    cursor.execute(q_modificare)
                    cursor.commit()
                
                if departament != "":
                    q_departamente = "SELECT DepartamentID FROM dbo.Departamente WHERE NumeDepartament = '" + str(departament) +"';"
                    cursor.execute(q_departamente)
                    departament = cursor.fetchall()
                    departament = departament[0][0]

                    q_modificare = "UPDATE dbo.Avioane SET DepartamentID = " + str(departament) + " WHERE CodAvion = '" + cod + "';"
                    cursor.execute(q_modificare)
                    cursor.commit()
    
    def actulizareAvioane(self):

        #Aceasta este funcția care actualizează odată la 3 secunde datele case află în tabelul cu Avioane din interfață
        q_avioane = "SELECT DepartamentID, NumeAvion, CodAvion, CostProductie, Pret, VitezaMaxima, NumarLocuri FROM dbo.Avioane;"
        #Se execută cererea care preia toate datele necesare

        cursor.execute(q_avioane)
        avioane = cursor.fetchall()
        self.ui.tabelAvioane.setRowCount(len(avioane))

        counter = 0

        #Se introduc datele actualizate în tabelul din interfață
        for avion in avioane:
            #În cazul departamentului cu ajutorul cheii externe se afișează numele departamentului
            q_departamenete = "SELECT NumeDepartament FROM dbo.Departamente WHERE DepartamentID = " + str(avion[0]) + ";"
            cursor.execute(q_departamenete)
            departament = cursor.fetchall()

            self.ui.tabelAvioane.setItem(counter, 1, QTableWidgetItem(departament[0][0]))
            self.ui.tabelAvioane.setItem(counter, 0, QTableWidgetItem(avion[1]))
            self.ui.tabelAvioane.setItem(counter, 2, QTableWidgetItem(avion[2]))
            self.ui.tabelAvioane.setItem(counter, 3, QTableWidgetItem(str(avion[3])))
            self.ui.tabelAvioane.setItem(counter, 4, QTableWidgetItem(str(avion[4])))
            self.ui.tabelAvioane.setItem(counter, 5, QTableWidgetItem(str(avion[5])))
            self.ui.tabelAvioane.setItem(counter, 6, QTableWidgetItem(str(avion[6])))
            counter = counter + 1 
    
    def actualizareOperatori(self):
        
            #Aceasta este funcția care actualizează odată la 3 secunde datele case află în tabelul cu Avioane din interfață
            q_operatori = "SELECT * FROM dbo.OperatoriAerieni;"

            #Se execută care preia toate datele necesare
            cursor.execute(q_operatori)
            operatori = cursor.fetchall()
            self.ui.afisareOperatori.setRowCount(len(operatori))
            self.ui.afisareOperatori.clearContents()

            #Se actualizează valorile din interfață
            counter = 0
            for operator in operatori:
                self.ui.afisareOperatori.setItem(counter, 0, QTableWidgetItem(operator[1]))
                self.ui.afisareOperatori.setItem(counter, 1, QTableWidgetItem(operator[2]))
                self.ui.afisareOperatori.setItem(counter, 2, QTableWidgetItem(operator[3]))
                counter = counter + 1

    def modNumeOperator(self):
        #Funcție care modifică Numele Operatorului din tabela OperatoriAerieni
        #Actualizarea se face după cod deoarece este unic
        cod = self.ui.inputCodOperatorModificareNume.text()
        newName = self.ui.inputNumeNouOperator.text()
        mod = "UPDATE dbo.OperatoriAerieni SET NumeOperatorAerian = '" + newName + "' WHERE CodOperatorAerian = '" + cod + "';"
        cursor.execute(mod)
        conn.commit()

        self.ui.inputCodOperatorModificareNume.setText("")
        self.ui.inputNumeNouOperator.setText("")
    
    def modRegiuneOperator(self):
        #Funcție care modifică Regiunea din Tabela OperatoriAerieni
        #Actualizarea se face după cod deoarece este unic
        cod = self.ui.inputCodOperatorModificareRegiune.text()
        newRegion = self.ui.inputRegiuneNouaOperator.text()
        mod = "UPDATE dbo.OperatoriAerieni SET Regiune = '" + newRegion + "' WHERE CodOperatorAerian = '" + cod + "';"
        cursor.execute(mod)
        conn.commit()

        self.ui.inputCodOperatorModificareRegiune.setText("")
        self.ui.inputRegiuneNouaOperator.setText("")


    def delOperator(self):

        #Funcție care șterge o înregistrarea din tabela OperatoriAerieni după cod
        cod = self.ui.inputCodOperatorStergere.text()
        dell = "DELETE FROM dbo.OperatoriAerieni WHERE CodOperatorAerian = '" + cod + "';"
        cursor.execute(dell)
        conn.commit()

        self.ui.inputCodOperatorStergere.setText("")


    def addOperator(self):
        #Funcție care introduce o nouă înregistrare în tabela OperatoriAerieni
        nume = self.ui.inputNumeOperator.text()
        cod = self.ui.inputCodOperator.text()
        regiune = self.ui.inputRegiuneOperator.text()

        add = "INSERT INTO dbo.OperatoriAerieni (NumeOperatorAerian, CodOperatorAerian, Regiune) VALUES ('"+ nume +"', '"+ cod + "', '"+ regiune +"');"
        cursor.execute(add)
        conn.commit()

        self.ui.inputRegiuneOperator.setText("")
        self.ui.inputCodOperator.setText("")
        self.ui.inputNumeOperator.setText("")

username = ""
password = ""
cnxn_str = "" #Variabile ce sunt folosite la realizarea conexiunii la baza de date

if __name__ == "__main__":
    app = QApplication(sys.argv)
    login = LoginWindow()
    #Dacă s-a trecut de fereastra de login(Conexiunea la baza de date a fost realizată)
    #se deschide fereastra principală și se realizează din nou conexiunea la baza de date cu aceleași credențiale
    if login.exec() == QDialog.Accepted:
        password = login.getPassword()
        username = login.getUsername()
        cnxn_str = (
            "Driver=" + driver + ";"
            "Server=" + server + ";"
            "Database=" + db + ";"
            "Trusted_Connection=no;"
            "UID=" + username + ";"
            "PWD=" + password + ";"
        )

        conn = odbc.connect(cnxn_str)
        cursor = conn.cursor()
        widget = MainWindow()
        widget.show()
        sys.exit(app.exec())

cursor.close()
conn.close()
#Se închide conexiunea la baza de date