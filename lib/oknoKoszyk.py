from PySide2 import QtWidgets
from PySide2.QtWidgets import QApplication
from pip._vendor.colorama import Fore

from gui import logi, main, koszyk
from lib import oknoAdmin
from lib.operacjeMongoDB import es


class WidokKoszyk(koszyk.Ui_MainWindow, QtWidgets.QMainWindow):
    def __init__(self):
        super(WidokKoszyk, self).__init__()
        self.setupUi(self)



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
    qt_app = WidokKoszyk()
    qt_app.show()
    app.exec_()