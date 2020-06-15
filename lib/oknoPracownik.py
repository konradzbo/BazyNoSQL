from PySide2 import QtWidgets
from PySide2.QtWidgets import QApplication
from bson import ObjectId

from gui import pracownik, main
from lib import oknoAdmin
from lib.operacjeMongoDB import collection
from lib.tabela import Zarzadzanie


class WidokPracownik(pracownik.Ui_MainWindow, QtWidgets.QMainWindow):
    def __init__(self):
        super(WidokPracownik, self).__init__()
        self.setupUi(self)
        Zarzadzanie.refresh_pracownik(self)
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

        collection.insert_one({
            "Imię": text2,
            "Nazwisko": text3,
            "E-mail": text4,
            "Numer telefonu": text5,
            "Stanowisko": text6})
        Zarzadzanie.refresh_pracownik(self)

    def remove_data(self):
        collection.delete_one({'_id': ObjectId(self.lineEdit.text())})
        Zarzadzanie.refresh_pracownik(self)

    def update_existing(self, data):
        text = ObjectId(self.lineEdit.text())
        text2 = str(self.lineEdit_2.text())
        text3 = str(self.lineEdit_3.text())
        text4 = str(self.lineEdit_4.text())
        text5 = int(self.lineEdit_5.text())
        text6 = str(self.lineEdit_6.text())
        data = ({"Imię": text2,"Nazwisko": text3,"E-mail": text4,"Numer telefonu": text5,"Stanowisko": text6})
        collection.update_one({'_id': text}, {"$set": data})
        Zarzadzanie.refresh_pracownik(self)

if __name__ == '__main__':
    app = QtWidgets.QApplication()
    qt_app = WidokPracownik()
    qt_app.show()
    app.exec_()