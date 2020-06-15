from PySide2 import QtCore
from lib import operacjeMongoDB


class Zarzadzanie(QtCore.QAbstractTableModel):
    def __init__(self, data):
        QtCore.QAbstractTableModel.__init__(self)
        self.user_data = data
        self.columns = list(self.user_data[0].keys())


    def headerData(self, section, orientation, role=QtCore.Qt.DisplayRole):
        if orientation == QtCore.Qt.Horizontal and role == QtCore.Qt.DisplayRole:
            return self.columns[section].title()


    def rowCount(self, *args, **kwargs):
        return len(self.user_data)


    def columnCount(self, *args, **kwargs):
        return len(self.columns)


    def data(self, index, role):
        row = self.user_data[index.row()]
        column = self.columns[index.column()]

        if role == QtCore.Qt.DisplayRole:
            return str(row[column])




    def refresh_klient(self):
        self.user_data = operacjeMongoDB.get_multiple_data1()
        self.model = Zarzadzanie(self.user_data)
        self.tableView.setModel(self.model)

    def refresh_pracownik(self):
        self.user_data = operacjeMongoDB.get_multiple_data()
        self.model = Zarzadzanie(self.user_data)
        self.tableView.setModel(self.model)

    def refresh_produkt(self):
        self.user_data = operacjeMongoDB.get_multiple_data2()
        self.model = Zarzadzanie(self.user_data)
        self.tableView.setModel(self.model)

