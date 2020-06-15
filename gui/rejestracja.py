# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'rejestracja.ui'
##
## Created by: Qt User Interface Compiler version 5.14.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import (QCoreApplication, QDate, QDateTime, QMetaObject,
    QObject, QPoint, QRect, QSize, QTime, QUrl, Qt)
from PySide2.QtGui import (QBrush, QColor, QConicalGradient, QCursor, QFont,
    QFontDatabase, QIcon, QKeySequence, QLinearGradient, QPalette, QPainter,
    QPixmap, QRadialGradient)
from PySide2.QtWidgets import *


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(333, 243)
        self.lineEdit = QLineEdit(Dialog)
        self.lineEdit.setObjectName(u"lineEdit")
        self.lineEdit.setGeometry(QRect(10, 15, 141, 20))
        self.lineEdit_2 = QLineEdit(Dialog)
        self.lineEdit_2.setObjectName(u"lineEdit_2")
        self.lineEdit_2.setGeometry(QRect(10, 55, 141, 20))
        self.lineEdit_4 = QLineEdit(Dialog)
        self.lineEdit_4.setObjectName(u"lineEdit_4")
        self.lineEdit_4.setGeometry(QRect(180, 15, 141, 20))
        self.lineEdit_5 = QLineEdit(Dialog)
        self.lineEdit_5.setObjectName(u"lineEdit_5")
        self.lineEdit_5.setGeometry(QRect(180, 55, 141, 20))
        self.lineEdit_7 = QLineEdit(Dialog)
        self.lineEdit_7.setObjectName(u"lineEdit_7")
        self.lineEdit_7.setGeometry(QRect(10, 155, 141, 20))
        self.lineEdit_8 = QLineEdit(Dialog)
        self.lineEdit_8.setObjectName(u"lineEdit_8")
        self.lineEdit_8.setGeometry(QRect(180, 155, 141, 20))
        self.lineEdit_8.setEchoMode(QLineEdit.Password)
        self.label = QLabel(Dialog)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(10, 0, 141, 16))
        font = QFont()
        font.setPointSize(8)
        self.label.setFont(font)
        self.label_4 = QLabel(Dialog)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(180, 40, 141, 16))
        self.label_4.setFont(font)
        self.label_7 = QLabel(Dialog)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setGeometry(QRect(10, 140, 141, 16))
        self.label_7.setFont(font)
        self.label_8 = QLabel(Dialog)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setGeometry(QRect(180, 140, 141, 16))
        self.label_8.setFont(font)
        self.pushButton = QPushButton(Dialog)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setGeometry(QRect(9, 210, 101, 23))
        self.label_2 = QLabel(Dialog)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(180, 0, 141, 16))
        self.label_2.setFont(font)
        self.label_5 = QLabel(Dialog)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setGeometry(QRect(10, 40, 141, 16))
        self.label_5.setFont(font)
        self.lineEdit_3 = QLineEdit(Dialog)
        self.lineEdit_3.setObjectName(u"lineEdit_3")
        self.lineEdit_3.setGeometry(QRect(10, 95, 141, 20))
        self.lineEdit_6 = QLineEdit(Dialog)
        self.lineEdit_6.setObjectName(u"lineEdit_6")
        self.lineEdit_6.setGeometry(QRect(180, 95, 141, 20))
        self.label_3 = QLabel(Dialog)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(10, 80, 141, 16))
        self.label_3.setFont(font)
        self.label_10 = QLabel(Dialog)
        self.label_10.setObjectName(u"label_10")
        self.label_10.setGeometry(QRect(180, 80, 141, 16))
        self.label_10.setFont(font)

        self.retranslateUi(Dialog)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Rejestracja", None))
        self.label.setText(QCoreApplication.translate("Dialog", u"Imi\u0119", None))
        self.label_4.setText(QCoreApplication.translate("Dialog", u"Miejscowo\u015b\u0107", None))
        self.label_7.setText(QCoreApplication.translate("Dialog", u"E-mail", None))
        self.label_8.setText(QCoreApplication.translate("Dialog", u"Has\u0142o", None))
        self.pushButton.setText(QCoreApplication.translate("Dialog", u"Utw\u00f3rz konto", None))
        self.label_2.setText(QCoreApplication.translate("Dialog", u"Nazwisko", None))
        self.label_5.setText(QCoreApplication.translate("Dialog", u"Numer telefonu", None))
        self.label_3.setText(QCoreApplication.translate("Dialog", u"Ulica", None))
        self.label_10.setText(QCoreApplication.translate("Dialog", u"Kod pocztowy", None))
    # retranslateUi

