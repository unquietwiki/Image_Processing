# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Laplace_Screen.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_Dialog_8(object):
    def setupUi(self, Dialog_8):
        if not Dialog_8.objectName():
            Dialog_8.setObjectName(u"Dialog_8")
        Dialog_8.resize(1366, 800)
        self.Open_Image_Button = QPushButton(Dialog_8)
        self.Open_Image_Button.setObjectName(u"Open_Image_Button")
        self.Open_Image_Button.setGeometry(QRect(70, 620, 401, 81))
        self.label_2 = QLabel(Dialog_8)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(690, 20, 571, 561))
        self.label_3 = QLabel(Dialog_8)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(610, 330, 61, 31))
        self.label_3.setStyleSheet(u"font: 22pt \"MS Shell Dlg 2\";")
        self.label_3.setAlignment(Qt.AlignCenter)
        self.label_4 = QLabel(Dialog_8)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(870, 640, 281, 41))
        self.label_4.setStyleSheet(u"font: 16pt \"MS Shell Dlg 2\";")
        self.label_4.setAlignment(Qt.AlignCenter)
        self.label = QLabel(Dialog_8)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(10, 20, 571, 561))
        self.label_5 = QLabel(Dialog_8)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setGeometry(QRect(410, 730, 581, 41))
        self.label_5.setStyleSheet(u"color: rgb(255, 0, 0);")

        self.retranslateUi(Dialog_8)

        QMetaObject.connectSlotsByName(Dialog_8)
    # setupUi

    def retranslateUi(self, Dialog_8):
        Dialog_8.setWindowTitle(QCoreApplication.translate("Dialog_8", u"Dialog", None))
        self.Open_Image_Button.setText(QCoreApplication.translate("Dialog_8", u"Open Image", None))
        self.label_2.setText("")
        self.label_3.setText(QCoreApplication.translate("Dialog_8", u"=>", None))
        self.label_4.setText(QCoreApplication.translate("Dialog_8", u"Output Image", None))
        self.label.setText("")
        self.label_5.setText("")
    # retranslateUi

