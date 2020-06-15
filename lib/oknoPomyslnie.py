import time

from PySide2 import QtWidgets

from gui import pomyslnie


class Pomyslnie(pomyslnie.Ui_Dialog, QtWidgets.QDialog):
    def __init__(self):
        super(Pomyslnie, self).__init__()
        self.setupUi(self)

if __name__ == '__main__':
    app = QtWidgets.QApplication()
    qt_app = Pomyslnie()
    qt_app.show()
    app.exec_()