import operator
from PySide2.QtCore import SIGNAL, QAbstractTableModel
from PySide2.QtGui import Qt, QFont
from PySide2.QtWidgets import QApplication, QVBoxLayout, QTableView, QWidget

from lib.operacjeMongoDB import session


class MyWindow(QWidget):
    def __init__(self, data_list, header, *args):
        QWidget.__init__(self, *args)
        # setGeometry(x_pos, y_pos, width, height)
        self.setGeometry(300, 200, 570, 450)
        self.setWindowTitle("Click on column title to sort")
        table_model = MyTableModel(self, data_list, header)
        table_view = QTableView()
        table_view.setModel(table_model)
        # set font
        font = QFont("Courier New", 14)
        table_view.setFont(font)
        # set column width to fit contents (set font first!)
        table_view.resizeColumnsToContents()
        # enable sorting
        table_view.setSortingEnabled(True)
        layout = QVBoxLayout(self)
        layout.addWidget(table_view)
        self.setLayout(layout)
class MyTableModel(QAbstractTableModel):
    def __init__(self, parent, mylist, header, *args):
        QAbstractTableModel.__init__(self, parent, *args)
        self.mylist = mylist
        self.header = header
    def rowCount(self, parent):
        return len(self.mylist)
    def columnCount(self, parent):
        return len(self.mylist[0])
    def data(self, index, role):
        if not index.isValid():
            return None
        elif role != Qt.DisplayRole:
            return None
        return self.mylist[index.row()][index.column()]
    def headerData(self, col, orientation, role):
        if orientation == Qt.Horizontal and role == Qt.DisplayRole:
            return self.header[col]
        return None
    def sort(self, col, order):
        """sort table by given column number col"""
        self.emit(SIGNAL("layoutAboutToBeChanged()"))
        self.mylist = sorted(self.mylist,
            key=operator.itemgetter(col))
        if order == Qt.DescendingOrder:
            self.mylist.reverse()
        self.emit(SIGNAL("layoutChanged()"))
# the solvent data ...
header = [' Klient', ' Numer zakupu', ' Produkt', ' Cena', ' Ilość', ' Data zakupu']
# use numbers for numeric data to sort properly

rows = session.execute("select numer_zakupu, klient, produkt, cena, ilosc, data_zakupu from zakupy")

a=5
str(a)

for rowz in rows:
    #item = str("Numer zakupu: " + row.numer_zakupu + " Klient: " + row.klient + " Produkt: " + row.produkt + " Cena: " + row.cena + " Ilość: " + row.ilosc + " Data zakupu: " + row.data_zakupu)
    data_list = [(rowz.klient, rowz.numer_zakupu, rowz.produkt, rowz.cena, rowz.ilosc, rowz.data_zakupu)]


app = QApplication([])
win = MyWindow(data_list, header)
win.show()
app.exec_()