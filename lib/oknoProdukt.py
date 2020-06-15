from PySide2 import QtWidgets
from PySide2.QtWidgets import QApplication
from bson import ObjectId

from gui import main, produkt
from lib import oknoAdmin
from lib.operacjeMongoDB import collection, collection2
from lib.tabela import Zarzadzanie


class WidokProdukt(produkt.Ui_MainWindow, QtWidgets.QMainWindow):
    def __init__(self):
        super(WidokProdukt, self).__init__()
        self.setupUi(self)
        Zarzadzanie.refresh_produkt(self)
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
        text = str(self.lineEdit.text())
        text2 = str(self.lineEdit_2.text())
        text3 = str(self.lineEdit_3.text())
        text4 = str(self.lineEdit_4.text())
        text5 = int(self.lineEdit_5.text())
        text6 = int(self.lineEdit_6.text())


        collection2.insert_one({
            "_id":text,
            "Nazwa": text2,
            "Model": text3,
            "Marka": text4,
            "Cena": text5,
            "Ilość": text6})
        Zarzadzanie.refresh_produkt(self)

    def remove_data(self):
        collection2.delete_one({'_id': ObjectId(self.lineEdit.text())})
        Zarzadzanie.refresh_produkt(self)

    def update_existing(self, data):
        text = ObjectId(self.lineEdit.text())
        text2 = str(self.lineEdit_2.text())
        text3 = str(self.lineEdit_3.text())
        text4 = str(self.lineEdit_4.text())
        text5 = int(self.lineEdit_5.text())
        text6 = int(self.lineEdit_6.text())

        data = ({"Nazwa": text2,"Model": text3,"Marka": text4,"Cena": text5,"Ilość": text6})
        collection2.update_one({'_id': text}, {"$set": data})
        Zarzadzanie.refresh_produkt(self)

if __name__ == '__main__':
    app = QtWidgets.QApplication()
    qt_app = WidokProdukt()
    qt_app.show()
    app.exec_()