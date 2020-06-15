import sys
from datetime import datetime

from PySide2 import QtWidgets
from PySide2.QtWidgets import QApplication, QMessageBox

from gui import rejestracja, logowanie
from lib import oknoLogowanie, oknoPomyslnie
from lib.operacjeMongoDB import collection1, es


class Zarejestruj(rejestracja.Ui_Dialog, QtWidgets.QDialog):
    def __init__(self):
        super(Zarejestruj, self).__init__()
        self.setupUi(self)
        self.pushButton.clicked.connect(self.dodaj)


    def dodaj(self):
        now = datetime.now()
        text4 = str(self.lineEdit_7.text())
        res = es.index(
            index='sklep',
            doc_type='logg',
            body={
                "user": (text4),
                "data": (now),
                "operation": "registration"
            })

        text2 = str(self.lineEdit.text())
        text3 = str(self.lineEdit_4.text())

        text5 = int(self.lineEdit_2.text())
        text6 = str(self.lineEdit_5.text())
        text7 = str(self.lineEdit_3.text())
        text8 = str(self.lineEdit_6.text())
        text9 = str(self.lineEdit_8.text())

        collection1.insert_one({
            "Imię": text2,
            "Nazwisko": text3,
            "E-mail": text4,
            "Numer telefonu": text5,
            "Miejscowość": text6,
            "Ulica": text7,
            "Kod pocztowy": text8,
            "Hasło": text9})

        self.message()

    def message(self):
        msg = QMessageBox()
        msg.setIcon(QMessageBox.Information)
        msg.setText("Konto zostało utworzone pomyślnie!\nMożna się zalogować :)")
        msg.setWindowTitle("Informacje o rejestracji")
        msg.setStandardButtons(QMessageBox.Ok)
        msg.exec_()

if __name__ == '__main__':
    app = QtWidgets.QApplication()
    qt_app = Zarejestruj()
    qt_app.show()
    app.exec_()