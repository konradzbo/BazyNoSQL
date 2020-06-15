from PySide2 import QtWidgets
from PySide2.QtWidgets import QApplication
from pip._vendor.colorama import Fore

from gui import logi, main
from lib import oknoAdmin
from lib.operacjeMongoDB import es


class WidokLogi(logi.Ui_MainWindow, QtWidgets.QMainWindow):
    def __init__(self):
        super(WidokLogi, self).__init__()
        self.setupUi(self)
        self.pushButton.clicked.connect(self.szukaj)
        self.pushButton_2.clicked.connect(self.wszystkie)
        self.pushButton_3.clicked.connect(self.powrot)


    def powrot(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = main.Ui_MainWindow()
        self.ui.setupUi(self.window)
        QApplication.closeAllWindows()
        self.qt2_app = oknoAdmin.App()
        self.qt2_app.show()

    def szukaj(self):
        self.listWidget.clear()
        text = str(self.lineEdit.text())
        res= es.search(index='sklep',doc_type='logg',size=1000,body={
                'query':{
                    'fuzzy':{
                        "user": text
                    }
                }
            })

        for hit in res['hits']['hits']:
            item = (str(hit['_source']['user']) + "  |  " + (str(hit['_source']['data'])) + "  |  " +
                     (str(hit['_source']['operation'])))
            self.listWidget.addItem(item)

    def wszystkie(self):
        self.listWidget.clear()
        text = str(self.lineEdit.text())
        res = es.search(index='sklep', doc_type='logg', size=1000, body={
            'query': {
                "match_all": {}
                }
        })

        for hit in res['hits']['hits']:
            item = (str(hit['_source']['user']) + "  |  " + (
                str(hit['_source']['data'])) + "  |  " +
                                     (str(hit['_source']['operation'])))
            self.listWidget.addItem(item)




if __name__ == '__main__':
    app = QtWidgets.QApplication()
    qt_app = WidokLogi()
    qt_app.show()
    app.exec_()