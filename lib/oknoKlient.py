from PySide2 import QtWidgets
from PySide2.QtWidgets import QApplication
from bson import ObjectId

from gui import klient, main
from lib import oknoAdmin
from lib.operacjeMongoDB import collection1
from lib.tabela import Zarzadzanie


class WidokKlient(klient.Ui_MainWindow, QtWidgets.QMainWindow):
    def __init__(self):
        super(WidokKlient, self).__init__()
        self.setupUi(self)
        Zarzadzanie.refresh_klient(self)
        self.pushButton_2.clicked.connect(self.powrot)
        self.pushButton_4.clicked.connect(self.dodaj)
        self.pushButton_3.clicked.connect(self.remove_data)
        self.pushButton_5.clicked.connect(self.update_existing)


    def powrot(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = main.Ui_MainWindow()
        self.ui.setupUi(self.window)
        QApplication.closeAllWindows()
        self.qt2_app = oknoAdmin.App()
        self.qt2_app.show()

    def dodaj(self):
        text2 = str(self.lineEdit_2.text())
        text3 = str(self.lineEdit_3.text())
        text4 = str(self.lineEdit_4.text())
        text5 = int(self.lineEdit_5.text())
        text6 = str(self.lineEdit_6.text())
        text7 = str(self.lineEdit_7.text())
        text8 = str(self.lineEdit_8.text())
        text9 = str(self.lineEdit_9.text())

        collection1.insert_one({
            "Imię": text2,
            "Nazwisko": text3,
            "E-mail": text4,
            "Numer telefonu": text5,
            "Miejscowość": text6,
            "Ulica": text7,
            "Kod pocztowy": text8,
            "Hasło": text9})
        Zarzadzanie.refresh_klient(self)

    def remove_data(self):
        collection1.delete_one({'_id': ObjectId(self.lineEdit.text())})
        Zarzadzanie.refresh_klient(self)

    def update_existing(self, data):
        text = ObjectId(self.lineEdit.text())
        text2 = str(self.lineEdit_2.text())
        text3 = str(self.lineEdit_3.text())
        text4 = str(self.lineEdit_4.text())
        text5 = int(self.lineEdit_5.text())
        text6 = str(self.lineEdit_6.text())
        text7 = str(self.lineEdit_7.text())
        text8 = str(self.lineEdit_8.text())
        text9 = str(self.lineEdit_9.text())

        data = ({"Imię": text2,"Nazwisko": text3,"E-mail": text4,"Numer telefonu": text5,"Miejscowość": text6,"Ulica": text7,"Kod pocztowy": text8, "Hasło": text9})
        collection1.update_one({'_id': text}, {"$set": data})
        Zarzadzanie.refresh_klient(self)


if __name__ == '__main__':
    app = QtWidgets.QApplication()
    qt_app = WidokKlient()
    qt_app.show()
    app.exec_()
