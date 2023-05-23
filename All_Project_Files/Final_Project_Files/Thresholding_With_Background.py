# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Thresholding_With_Background.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5 import QtCore, QtGui, QtWidgets, uic
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.uic import loadUi
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QDialog, QApplication, QWidget, QStackedWidget, QComboBox, QPushButton, QVBoxLayout, QLabel
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QFileDialog
import cv2
import numpy as np


class Ui_Dialog_3(object):
    def setupUi(self, Dialog_3):
        Dialog_3.setObjectName("Dialog_3")
        Dialog_3.resize(1366, 800)
        self.lineEdit = QtWidgets.QLineEdit(Dialog_3)
        self.lineEdit.setGeometry(QtCore.QRect(530, 620, 301, 41))
        self.lineEdit.setStyleSheet("border: 12px  solid rgb(0, 0, 0);\n"
"border-width: 2px;\n"
"font: 11.5pt \"MS Shell Dlg 2\";\n"
"border-radius: 15px;\n"
"padding-left:20px;\n"
"padding-right:20px;")
        self.lineEdit.setText("")
        self.lineEdit.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit.setObjectName("lineEdit")
        self.lineEdit_2 = QtWidgets.QLineEdit(Dialog_3)
        self.lineEdit_2.setGeometry(QtCore.QRect(530, 670, 301, 41))
        self.lineEdit_2.setStyleSheet("border: 12px  solid rgb(0, 0, 0);\n"
"border-width: 2px;\n"
"font: 11.5pt \"MS Shell Dlg 2\";\n"
"border-radius: 15px;\n"
"padding-left:20px;\n"
"padding-right:20px;")
        self.lineEdit_2.setText("")
        self.lineEdit_2.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.label_4 = QtWidgets.QLabel(Dialog_3)
        self.label_4.setGeometry(QtCore.QRect(870, 640, 281, 41))
        self.label_4.setStyleSheet("font: 16pt \"MS Shell Dlg 2\";")
        self.label_4.setAlignment(QtCore.Qt.AlignCenter)
        self.label_4.setObjectName("label_4")
        self.label_2 = QtWidgets.QLabel(Dialog_3)
        self.label_2.setGeometry(QtCore.QRect(690, 20, 571, 561))
        self.label_2.setText("")
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.label = QtWidgets.QLabel(Dialog_3)
        self.label.setGeometry(QtCore.QRect(10, 20, 571, 561))
        self.label.setText("")
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.Open_Image_Button = QtWidgets.QPushButton(Dialog_3)
        self.Open_Image_Button.setGeometry(QtCore.QRect(70, 620, 401, 81))
        self.Open_Image_Button.setObjectName("Open_Image_Button")
        self.label_3 = QtWidgets.QLabel(Dialog_3)
        self.label_3.setGeometry(QtCore.QRect(590, 260, 61, 31))
        self.label_3.setStyleSheet("font: 22pt \"MS Shell Dlg 2\";")
        self.label_3.setAlignment(QtCore.Qt.AlignCenter)
        self.label_3.setObjectName("label_3")
        self.label_5 = QtWidgets.QLabel(Dialog_3)
        self.label_5.setGeometry(QtCore.QRect(410, 730, 581, 41))
        self.label_5.setStyleSheet("color: rgb(255, 0, 0);")
        self.label_5.setText("")
        self.label_5.setObjectName("label_5")

        self.retranslateUi(Dialog_3)
        QtCore.QMetaObject.connectSlotsByName(Dialog_3)

    def retranslateUi(self, Dialog_3):
        _translate = QtCore.QCoreApplication.translate
        Dialog_3.setWindowTitle(_translate("Dialog_3", "Dialog"))
        self.lineEdit.setPlaceholderText(_translate("Dialog_3", "Enter Lower Limit..."))
        self.lineEdit_2.setPlaceholderText(_translate("Dialog_3", "Enter Upper Limit..."))
        self.label_4.setText(_translate("Dialog_3", "Output Image"))
        self.Open_Image_Button.setText(_translate("Dialog_3", "Open Image"))
        self.label_3.setText(_translate("Dialog_3", "=>"))


        self.Open_Image_Button.clicked.connect(self.File_Select)


    def File_Select(self):
        Lower_Limit = self.lineEdit.text() # Accessing the lower limit value entered by the user.
        Upper_Limit = self.lineEdit_2.text() # Accessing the upper limit value entered by the user.
        
        if not (int(Lower_Limit.isdigit() and Upper_Limit.isdigit())):
            self.label_5.setText("Please enter an integer value!")
        else:
            self.label_5.setText("")
            # fname = QFileDialog.getOpenFileName(self, "Open File", "All_Project_Files\Final_Project_Files\Cam_Media", "Images (*.png *.xpm *.jpg)")
            # # Opening the Image
            # self.pixmap = QPixmap(fname[0]) # This returns a tuple and hence we mention [0].
            # # Adding the picture to the Label.
            # self.label.setPixmap(self.pixmap)
            Lower_Limit = int(self.lineEdit.text())
            Upper_Limit = int(self.lineEdit_2.text())
            file_name, _ = QFileDialog.getOpenFileName(None, 'Open Image File', r"<Default dir>", "Image files (*.jpg *.jpeg *.gif *.png)")
            self.label.setPixmap(QPixmap(file_name))
            img = cv2.imread(file_name, 0)
            m, n = img.shape
            print("The original size of the image is ", m, " x ", n)


            threshold_image = []
            a = Lower_Limit
            b = Upper_Limit
            for i in range(len(img)):
                temp = []
                for j in range(len(img)):
                    if img[i][j] > a and img[i][j] < b:
                        temp.append(255)
                    else:
                        temp.append(img[i][j])
                threshold_image.append(temp)

            threshold_image = np.array(threshold_image)

            m, n= threshold_image.shape
            print("The new size of the image is ", m, " x ", n)

            cv2.imwrite(r"All_Project_Files\Final_Project_Files\Cam_Media\Thresholding_With\Threshold_With_Image.png", threshold_image)
            Thresholding_With_File_Name = r"All_Project_Files\Final_Project_Files\Cam_Media\Thresholding_With\Threshold_With_Image.png"
            self.label_2.setPixmap(QPixmap(Thresholding_With_File_Name))


            # If you want these to display these in separate windows other than GUI.
            # cv2.imshow("Negative Image", negative_img)


            # cv2.imshow("Image", img)
            # cv2.waitKey(0)
    
            # # closing all open windows
            # cv2.destroyAllWindows()


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog_3 = QtWidgets.QDialog()
    ui = Ui_Dialog_3()
    ui.setupUi(Dialog_3)
    Dialog_3.show()
    sys.exit(app.exec_())
