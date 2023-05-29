# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Down_Sampling_Image_Screen.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5 import QtCore, QtGui, QtWidgets, uic
from PyQt5.QtGui import *
from PyQt5.QtWidgets import QMenuBar, QMenu
from PyQt5.QtCore import *
from PyQt5.uic import loadUi
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QDialog, QApplication, QWidget, QStackedWidget, QComboBox, QPushButton, QVBoxLayout, QLabel
from PyQt5.QtWidgets import QApplication, QLabel, QSizePolicy, QScrollArea, QMessageBox, QMainWindow, QMenu, QAction, qApp, QFileDialog, QToolBar, QMenuBar  
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QFileDialog, QHBoxLayout
import cv2



class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(1366, 800)
        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(690, 20, 571, 561))
        self.label_2.setText("")
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.label_4 = QtWidgets.QLabel(Dialog)
        self.label_4.setGeometry(QtCore.QRect(870, 640, 281, 41))
        self.label_4.setStyleSheet("font: 16pt \"MS Shell Dlg 2\";")
        self.label_4.setAlignment(QtCore.Qt.AlignCenter)
        self.label_4.setObjectName("label_4")
        self.Open_Image_Button = QtWidgets.QPushButton(Dialog)
        self.Open_Image_Button.setGeometry(QtCore.QRect(70, 620, 401, 81))
        self.Open_Image_Button.setObjectName("Open_Image_Button")

        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(10, 20, 571, 561))
        self.label.setText("")
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.label.setBackgroundRole(QPalette.Base)
        self.label.setSizePolicy(QSizePolicy.Ignored, QSizePolicy.Ignored)
        self.label.setScaledContents(True)



        self.label_3 = QtWidgets.QLabel(Dialog)
        self.label_3.setGeometry(QtCore.QRect(590, 260, 61, 31))
        self.label_3.setStyleSheet("font: 22pt \"MS Shell Dlg 2\";")
        self.label_3.setAlignment(QtCore.Qt.AlignCenter)
        self.label_3.setObjectName("label_3")
        self.lineEdit = QtWidgets.QLineEdit(Dialog)
        self.lineEdit.setGeometry(QtCore.QRect(530, 620, 301, 81))
        self.lineEdit.setStyleSheet("border: 12px  solid rgb(0, 0, 0);\n"
"border-width: 2px;\n"
"font: 11.5pt \"MS Shell Dlg 2\";\n"
"border-radius: 15px;\n"
"padding-left:20px;\n"
"padding-right:20px;")
        self.lineEdit.setText("")
        self.lineEdit.setObjectName("lineEdit")
        self.label_5 = QtWidgets.QLabel(Dialog)
        self.label_5.setGeometry(QtCore.QRect(410, 730, 581, 41))
        self.label_5.setStyleSheet("color: rgb(255, 0, 0);")
        self.label_5.setText("")
        self.label_5.setObjectName("label_5")        

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label_4.setText(_translate("Dialog", "Output Image"))
        self.Open_Image_Button.setText(_translate("Dialog", "Open Image"))
        self.label_3.setText(_translate("Dialog", "=>"))
        self.lineEdit.setPlaceholderText(_translate("Dialog", "Enter Downsampling Value..."))

        self.Open_Image_Button.clicked.connect(self.File_Select)
        




    def File_Select(self):
        Down_Sampling_Value = self.lineEdit.text() # Accessing the value entered by the user.
        
        if not (int(Down_Sampling_Value.isdigit())):
            self.label_5.setText("Please enter an integer value!")
        else:
            self.label_5.setText("")
            # fname = QFileDialog.getOpenFileName(self, "Open File", "All_Project_Files\Final_Project_Files\Cam_Media", "Images (*.png *.xpm *.jpg)")
            # # Opening the Image
            # self.pixmap = QPixmap(fname[0]) # This returns a tuple and hence we mention [0].
            # # Adding the picture to the Label.
            # self.label.setPixmap(self.pixmap)
            Down_Sampling_Value = int(self.lineEdit.text())
            file_name, _ = QFileDialog.getOpenFileName(None, 'Open Image File', r"<Default dir>", "Image files (*.jpg *.jpeg *.gif *.png)")
            self.label.setPixmap(QPixmap(file_name))

            img = cv2.imread(file_name)
            m, n, c = img.shape
            print("The original size of the image is ", m, " x ", n)
            image_downsize = img[::Down_Sampling_Value, ::Down_Sampling_Value]
            m, n, c = image_downsize.shape
            print("The new size of the image is ", m, " x ", n)

            
            cv2.imwrite(r"All_Project_Files\Final_Project_Files\Cam_Media\Down_Sized_Img\Down_Sized_Image.png", image_downsize)
            Downsized_File_Name = r"All_Project_Files\Final_Project_Files\Cam_Media\Down_Sized_Img\Down_Sized_Image.png"
            # self.label_2.setPixmap(QPixmap(Downsized_File_Name))


            # If you want these to display these in separate windows other than GUI.
            # cv2.imshow("Negative Image", negative_img)


            # cv2.imshow("Image", img)
            # cv2.waitKey(0)
    
            # # closing all open windows
            # cv2.destroyAllWindows()


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())
