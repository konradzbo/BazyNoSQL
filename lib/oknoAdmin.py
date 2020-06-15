from PySide2 import QtWidgets
from PySide2.QtWidgets import QApplication

from gui import main, pracownik, klient, logi, produkt, historia_zakupow
from lib import oknoKlient, oknoPracownik, oknoLogi, oknoProdukt, oknoHistoria


class App(main.Ui_MainWindow, QtWidgets.QMainWindow):
    def __init__(self):
        super(App, self).__init__()
        self.setupUi(self)
        self.pushButton_2.clicked.connect(self.openPracownik)
        self.pushButton_3.clicked.connect(self.openKlient)
        self.pushButton_4.clicked.connect(self.openLogi)
        self.pushButton_5.clicked.connect(self.openProdukt)
        self.pushButton_6.clicked.connect(self.openHistoria)


    def openHistoria(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = historia_zakupow.Ui_MainWindow()
        self.ui.setupUi(self.window)
        QApplication.closeAllWindows()
        self.qt1_app = oknoHistoria.WidokHistoria()
        self.qt1_app.show()


    def openPracownik(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = pracownik.Ui_MainWindow()
        self.ui.setupUi(self.window)
        QApplication.closeAllWindows()
        self.qt1_app = oknoPracownik.WidokPracownik()
        self.qt1_app.show()


    def openKlient(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = klient.Ui_MainWindow()
        self.ui.setupUi(self.window)
        QApplication.closeAllWindows()
        self.qt1_app = oknoKlient.WidokKlient()
        self.qt1_app.show()

    def openLogi(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = logi.Ui_MainWindow()
        self.ui.setupUi(self.window)
        QApplication.closeAllWindows()
        self.qt1_app = oknoLogi.WidokLogi()
        self.qt1_app.show()

    def openProdukt(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = produkt.Ui_MainWindow()
        self.ui.setupUi(self.window)
        QApplication.closeAllWindows()
        self.qt1_app = oknoProdukt.WidokProdukt()
        self.qt1_app.show()


if __name__ == '__main__':
    app = QtWidgets.QApplication()
    qt_app = App()
    qt_app.show()
    app.exec_()