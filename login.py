#Importarea librariilor necesare
from PySide6.QtCore import Qt, Signal
import sys
from PySide6.QtWidgets import *
from PySide6.QtGui import QIcon, QFont
from config import *
import pyodbc as odbc

password = ""
username = "" #Variabile care vor fi necesare la conexiunea bazei de date

class LoginWindow(QDialog):

    authentication_successful = Signal()

    def __init__(self):
        super().__init__()

        self.user = ""
        self.passw = ""
        self.setWindowTitle("Aplicație pentru gestiunea unei companii care produce avioane")
        self.setWindowIcon(QIcon('airplane.png'))
        self.setFixedSize(300, 200)

        font = QFont()
        font.setPointSize(24)

        self.text = QLabel()
        self.text.setAlignment(Qt.AlignCenter)
        self.text.setText("Bine ați venit!")
        self.text.setStyleSheet("color: darkblue;")
        self.text.setFont(font)

        self.username = QLineEdit()
        self.username.setAlignment(Qt.AlignCenter)
        self.username.setPlaceholderText("Introduceți username-ul...")

        self.password = QLineEdit()
        self.password.setEchoMode(QLineEdit.Password)
        self.password.setAlignment(Qt.AlignCenter)
        self.password.setPlaceholderText("Introduceți parola...")

        self.connButton = QPushButton("Connect")

        self.avertisment = QLabel()
        self.avertisment.setText("Aveți 3 încercări!")
        self.avertisment.setStyleSheet("color: red;")
        self.avertisment.setAlignment(Qt.AlignCenter)

        layout = QVBoxLayout()
        layout.addWidget(self.text)
        layout.addWidget(self.username)
        layout.addWidget(self.password)
        layout.addWidget(self.avertisment)
        layout.addWidget(self.connButton)
        self.connButton.clicked.connect(self.getLog)

        self.setLayout(layout)
        #Se realizează layout-ul ferestrei de login

    def getLog(self):
            #Funcție cu care se încearcă realizarea conexiunii la baza de date
            global counter
            self.user = self.username.text()
            self.passw = self.password.text()
            username = self.user
            password = self.passw
            #Se preiau credențialele din interfață
            #După 3 încercări fereastra se închide
            if counter < 3:
                cnxn_str = (
                    "Driver=" + driver + ";" #Conexiunea la baza de date se face cu ajutorul driver-ului și server-ului
                    "Server=" + server + ";"
                    "Database=" + db + ";" #Se precizează baza de date la care vrem să ne conectăm
                    "Trusted_Connection=no;" #Flag care nu perimite conectarea fără credențiale
                    "UID=" + self.user + ";" #Credențialele folosite pentru conectare, date ca input din inferfață
                    "PWD=" + self.passw + ";"#Pot fi valide sau nu
                    )

                #Se încearcă conexiunea la baza de date
                try:
                    conn = odbc.connect(cnxn_str)
                except odbc.Error as ex:
                    sqlstate = ex.args[1]
                    print("Autentificare eșuată!")
                    counter += 1
                    self.avertisment.setText("Mai aveți " + str((3 - counter)) + " încercări!")
                    if counter == 3:
                        print("Nu mai aveți încercări disponibile. Aplicația se va închide.")
                        self.close()

            if conn:
                print("Autentificare cu succes!")
                self.authentication_successful.emit()
                self.accept()
                conn.close()
                #Dacă este reușită se transmite un semnal spre fereastra principală


    def getUsername(self):
            return self.user
    
    def getPassword(self):
            return self.passw
    #Gettere care vor fi folosite pentru a putea reutiliza parola și username-ul date ca input în fereastra principală
    


