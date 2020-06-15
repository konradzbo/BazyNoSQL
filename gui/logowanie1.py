# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'logowanie1.ui'
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
        Dialog.resize(233, 154)
        self.label_3 = QLabel(Dialog)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(-50, -40, 351, 241))
        self.label_3.setPixmap(QPixmap(u"../../../Desktop/gradient-colors-blur-background.jpg"))
        self.label_2 = QLabel(Dialog)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(10, 40, 47, 13))
        self.exit_btn = QPushButton(Dialog)
        self.exit_btn.setObjectName(u"exit_btn")
        self.exit_btn.setGeometry(QRect(140, 120, 81, 23))
        self.lineEdit_2 = QLineEdit(Dialog)
        self.lineEdit_2.setObjectName(u"lineEdit_2")
        self.lineEdit_2.setGeometry(QRect(10, 52, 211, 20))
        self.lineEdit_2.setContextMenuPolicy(Qt.NoContextMenu)
        self.lineEdit_2.setEchoMode(QLineEdit.Password)
        self.login_btn1 = QPushButton(Dialog)
        self.login_btn1.setObjectName(u"login_btn1")
        self.login_btn1.setGeometry(QRect(10, 90, 81, 23))
        self.newUser_btn = QPushButton(Dialog)
        self.newUser_btn.setObjectName(u"newUser_btn")
        self.newUser_btn.setGeometry(QRect(10, 120, 81, 23))
        self.lineEdit = QLineEdit(Dialog)
        self.lineEdit.setObjectName(u"lineEdit")
        self.lineEdit.setGeometry(QRect(10, 12, 211, 20))
        self.label = QLabel(Dialog)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(10, 0, 47, 13))

        self.retranslateUi(Dialog)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Logowanie", None))
        self.label_3.setText("")
        self.label_2.setText(QCoreApplication.translate("Dialog", u"Has\u0142o", None))
        self.exit_btn.setText(QCoreApplication.translate("Dialog", u"Wyjd\u017a", None))
        self.login_btn1.setText(QCoreApplication.translate("Dialog", u"Zaloguj", None))
        self.newUser_btn.setText(QCoreApplication.translate("Dialog", u"Nowe konto", None))
        self.label.setText(QCoreApplication.translate("Dialog", u"E-mail", None))
    # retranslateUi

