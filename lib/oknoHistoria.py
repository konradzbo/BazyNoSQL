from PySide2 import QtWidgets
from PySide2.QtGui import QStandardItemModel, QStandardItem
from PySide2.QtWidgets import QApplication

from gui import historia_zakupow, main
from lib import oknoAdmin
from lib.operacjeMongoDB import session


class WidokHistoria(historia_zakupow.Ui_MainWindow, QtWidgets.QMainWindow):
    def __init__(self):
        super(WidokHistoria, self).__init__()
        self.setupUi(self)
        self.pushButton_2.clicked.connect(self.powrot)

        rows = session.execute("select numer_zakupu, klient, produkt, cena, ilosc, data_zakupu from zakupy")

        for row in rows:
            item = str("Numer zakupu: "+ row.numer_zakupu +" Klient: "+ row.klient +" Produkt: "+ row.produkt +" Cena: "+ row.cena +" Ilość: "+ row.ilosc +" Data zakupu: "+ row.data_zakupu)
            self.listWidget.addItem(item)


    def powrot(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = main.Ui_MainWindow()
        self.ui.setupUi(self.window)
        QApplication.closeAllWindows()
        self.qt2_app = oknoAdmin.App()
        self.qt2_app.show()



if __name__ == '__main__':
    app = QtWidgets.QApplication()
    qt_app = WidokHistoria()
    qt_app.show()
    app.exec_()