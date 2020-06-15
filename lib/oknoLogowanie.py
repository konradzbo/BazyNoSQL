import sys
from PySide2.QtWidgets import QMessageBox, QApplication
from gui import logowanie, main, rejestracja, userProdukt
from PySide2 import QtWidgets
from lib import oknoAdmin, oknoRejestracja
import datetime
from lib.operacjeMongoDB import es, collection1, collection2, r, session
from lib.tabela import Zarzadzanie
from random import seed, random
from random import randint


class Zaloguj(logowanie.Ui_Dialog, QtWidgets.QDialog):
    def __init__(self):
        super(Zaloguj, self).__init__()
        self.setupUi(self)
        self.newUser_btn.clicked.connect(self.nowyUzytkownik)
        self.login_btn1.clicked.connect(self.logowanie)
        self.exit_btn.clicked.connect(self.wyjdz)


    def logowanie(self):
        login = self.lineEdit.text()
        pwd = self.lineEdit_2.text()
        now = datetime.datetime.now()

        regex = {"E-mail": {"$regex": login}}
        u = collection1.find(regex)

        if login == 'admin':
            if pwd == 'admin':
                res = es.index(
                    index='sklep',
                    doc_type='logg',
                    body={
                        "user": (login),
                        "data": (now),
                        "operation": "logging"
                    })
                self.admin()
            else:
                self.zlyLogin()

        for doc in u:
            x = doc["E-mail"]
            y = doc["Hasło"]
            if login == x:
                Zaloguj.username = x
                if pwd == y:
                    res = es.index(
                        index='sklep',
                        doc_type='logg',
                        body={
                            "user": (login),
                            "data": (now),
                            "operation": "logging"
                        })
                    self.user()
                else:
                    self.zlyLogin()
            else:
                self.zlyLogin()



    def zlyLogin(self):
        msg = QMessageBox()
        msg.setIcon(QMessageBox.Information)
        msg.setText("Wprowadzono błędne dane logowania")
        msg.setWindowTitle("Błąd logowania")
        msg.setStandardButtons(QMessageBox.Ok)
        retval = msg.exec_()


    def nowyUzytkownik(self):
        self.window = QtWidgets.QDialog()
        self.ui = rejestracja.Ui_Dialog()
        self.ui.setupUi(self.window)
        #app.closeAllWindows()
        self.qt1_app = oknoRejestracja.Zarejestruj()
        self.qt1_app.show()

    def wyjdz(self):
        sys.exit()

    def admin(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = main.Ui_MainWindow()
        self.ui.setupUi(self.window)
        #app.closeAllWindows()
        self.qt1_app = oknoAdmin.App()
        self.qt1_app.show()

    def user(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = userProdukt.Ui_MainWindow()
        self.ui.setupUi(self.window)
        #app.closeAllWindows()
        self.qt1_app = WidokUserProdukt()
        self.qt1_app.show()


class WidokUserProdukt(userProdukt.Ui_MainWindow, QtWidgets.QMainWindow):
    def __init__(self):
        super(WidokUserProdukt, self).__init__()
        self.setupUi(self)
        Zarzadzanie.refresh_produkt(self)
        login = Zaloguj.username
        self.textEdit_2.setText("" + login)
        self.pushButton.clicked.connect(self.dodaj)
        self.pushButton_2.clicked.connect(self.wyloguj)
        self.pushButton_3.clicked.connect(self.clear)
        self.pushButton_4.clicked.connect(self.kup)


    def wyloguj(self):
        self.clear()
        self.window = QtWidgets.QDialog()
        self.ui = logowanie.Ui_Dialog()
        self.ui.setupUi(self.window)
        QApplication.closeAllWindows()
        self.qt2_app = Zaloguj()
        self.qt2_app.show()

    def kup(self):
        login = Zaloguj.username
        y = r.llen('ile')
        value = randint(999, 10000)
        suma1 = 0
        for i in range(y):
            x = str(r.lindex(i, 0)) #id
            z = str(r.lindex(i, 4)) #ilosc

            regex = {"_id": {"$regex": x}}
            u = collection2.find(regex)
            for doc in u:
                p = doc["Ilość"]
                pr = doc["Nazwa"]
                mo = doc["Model"]
                ma = doc["Marka"]
                ce = doc["Cena"]
                myquery = {"_id": x}
                newvalues = {"$set": {"Ilość": p-int(z)}}
                collection2.update_one(myquery, newvalues)

        self.textEdit.setText("")
        self.message()

        ilosc = int(self.lineEdit_2.text())
        cena = ilosc*ce
        print(cena)
        x = datetime.datetime.now()
        date = str(x.strftime("%Y" + "-" + "%m" + "-" + "%d"))

        for j in range(y):
            nazwa1 = str(r.lindex(j, 1))
            model1 = str(r.lindex(j, 2))
            marka1 = str(r.lindex(j, 3))
            ilosc1 = str(r.lindex(j, 4))
            suma1 += (int(r.lindex(j, 4) or 0) * int((r.lindex(j, 5) or 0)))
            l = suma1

            session.execute(
                "insert into zakupy (id_zakupu, numer_zakupu, klient, produkt, cena, ilosc, data_zakupu) values(uuid(),'"+ str(value) +"','" + str(login) + "','"+ nazwa1 +" "+ model1 +" "+ marka1 +"','"+ str(suma1) +"','"+ str(ilosc1) +"','"+ date +"');")
            suma1 = 0


        Zarzadzanie.refresh_produkt(self)
        self.clear()

        res = es.index(
            index='sklep',
            doc_type='logg',
            body={
                "user": (login),
                "data": (x),
                "operation": "order"
            })



    def message(self):
        msg = QMessageBox()
        msg.setIcon(QMessageBox.Information)
        msg.setText("Przedmioty zostały zakupione!\nDziękujemy :)")
        msg.setWindowTitle("Informacje o zakupie")
        msg.setStandardButtons(QMessageBox.Ok)
        msg.exec_()

    def clear(self):
        for i in range(r.llen('ile')):
            r.delete(i)
            r.delete('ile')
            self.listWidget.clear()

    def suma_koszyk(self):

        suma = 0
        for i in range(r.llen('ile') + 1):
            suma + (int(r.lindex(i, 4) or 0) * int((r.lindex(i, 5) or 0)))


    def dodaj(self):
        noSQLList = "NoSQLStores"
        id = self.lineEdit.text()
        ilosc = int(self.lineEdit_2.text())


        regex = {"_id": {"$regex": id}}
        u = collection2.find(regex)
        for doc in u:
            p = doc["_id"]
            x = doc["Nazwa"]
            o = doc["Model"]
            z = doc["Marka"]
            a = doc["Cena"]


        suma=0
        y=r.llen('ile')
        r.rpush(y, p, x, o, z, ilosc, a)
        r.rpush("ile", p)

        self.listWidget.clear()
        for i in range(y+1):
            x = ((str(i+1)) + ". Produkt " + str(r.lindex(i,0))+"  "+str(r.lindex(i,1))+" "+str(r.lindex(i,2))+" "+str(r.lindex(i,3))+"  Ilość: "+str(r.lindex(i,4))+"  Cena: "+str(r.lindex(i,5))+"zł")
            self.listWidget.addItem(x)
            suma += (int(r.lindex(i, 4) or 0) * int((r.lindex(i, 5) or 0)))
            l = str(suma)
            self.textEdit.setText("Suma: "+l)





if __name__ == '__main__':
    app = QtWidgets.QApplication()
    qt_app = Zaloguj()
    qt_app.show()
    app.exec_()