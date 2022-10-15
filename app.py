from telnetlib import RCP
from typing import Literal
from PIL import Image, ImageFile
import os
import sys
import shutil
ImageFile.LOAD_TRUNCATED_IMAGES = True
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QDialog, QApplication, QFileDialog
from PyQt5.QtGui import QPixmap

VERSION="V0.21"
APP_NAME=f"Image Converter - {VERSION}"

def conversion(folder, finput, foutput):
    files_list = []
    number_converted_files = 0
    if ("." + foutput) in finput:
        finput.remove("." + foutput)
        if finput is None:
            exit()

    for file in os.listdir(folder):
        extension=os.path.splitext(file)
        if extension[1] in finput:
            files_list.append(file)

    for file in files_list:
        extension=os.path.splitext(file)
        new_file = file.replace(extension[1],("." + foutput))
        im = Image.open(folder + file).convert("RGB")
        foutput= foutput.replace(".", "")
        im.save(folder + new_file, foutput)
        os.remove(folder + file)
        number_converted_files += 1

class Ui_Confirmation(object):
    def setupUi(self, Form):
        Form.setObjectName("Statut")
        Form.resize(327, 188)
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(130, 60, 55, 16))
        self.label.setObjectName("label")
        self.progressBar = QtWidgets.QProgressBar(Form)
        self.progressBar.setGeometry(QtCore.QRect(37, 110, 251, 23))
        self.progressBar.setProperty("value", 0)
        self.progressBar.setObjectName("progressBar")
        self.label_2 = QtWidgets.QLabel(Form)
        self.label_2.setGeometry(QtCore.QRect(130, 150, 55, 16))
        self.label_2.setObjectName("label_2")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.label.setText(_translate("Form", "TextLabel"))
        self.label_2.setText(_translate("Form", "TextLabel"))


class Ui_MainWindow(object):
    def __init__(self) -> None:
        self.folder = ""
        self.format = []

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(364, 765)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(80, 640, 181, 51))
        self.pushButton.setObjectName("pushButton")
        self.groupBox = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox.setGeometry(QtCore.QRect(20, 330, 301, 161))
        self.groupBox.setObjectName("groupBox")
        self.checkBox = QtWidgets.QCheckBox(self.groupBox)
        self.checkBox.setGeometry(QtCore.QRect(30, 30, 81, 20))
        self.checkBox.setObjectName("checkBox")
        self.checkBox_2 = QtWidgets.QCheckBox(self.groupBox)
        self.checkBox_2.setGeometry(QtCore.QRect(30, 60, 81, 20))
        self.checkBox_2.setObjectName("checkBox_2")
        self.checkBox_3 = QtWidgets.QCheckBox(self.groupBox)
        self.checkBox_3.setGeometry(QtCore.QRect(170, 30, 81, 20))
        self.checkBox_3.setObjectName("checkBox_3")
        self.checkBox_5 = QtWidgets.QCheckBox(self.groupBox)
        self.checkBox_5.setGeometry(QtCore.QRect(170, 60, 81, 20))
        self.checkBox_5.setObjectName("checkBox_5")
        self.checkBox_6 = QtWidgets.QCheckBox(self.groupBox)
        self.checkBox_6.setGeometry(QtCore.QRect(30, 90, 81, 20))
        self.checkBox_6.setObjectName("checkBox_6")
        self.checkBox_7 = QtWidgets.QCheckBox(self.groupBox)
        self.checkBox_7.setGeometry(QtCore.QRect(170, 90, 81, 20))
        self.checkBox_7.setObjectName("checkBox_7")
        self.groupBox_2 = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_2.setGeometry(QtCore.QRect(20, 500, 301, 91))
        self.groupBox_2.setObjectName("groupBox_2")
        self.comboBox_2 = QtWidgets.QComboBox(self.groupBox_2)
        self.comboBox_2.setGeometry(QtCore.QRect(30, 40, 241, 22))
        self.comboBox_2.setObjectName("comboBox_2")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.groupBox_3 = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_3.setGeometry(QtCore.QRect(20, 230, 301, 91))
        self.groupBox_3.setObjectName("groupBox_3")
        self.checkBox_4 = QtWidgets.QCheckBox(self.groupBox_3)
        self.checkBox_4.setGeometry(QtCore.QRect(30, 40, 251, 20))
        self.checkBox_4.setObjectName("checkBox_4")
        self.groupBox_4 = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_4.setGeometry(QtCore.QRect(20, 120, 301, 101))
        self.groupBox_4.setObjectName("groupBox_4")
        self.lineEdit = QtWidgets.QLineEdit(self.groupBox_4)
        self.lineEdit.setGeometry(QtCore.QRect(30, 30, 241, 22))
        self.lineEdit.setObjectName("lineEdit")
        self.pushButton_2 = QtWidgets.QPushButton(self.groupBox_4)
        self.pushButton_2.setGeometry(QtCore.QRect(90, 60, 111, 28))
        self.pushButton_2.setObjectName("pushButton_2")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(120, 10, 101, 101))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(240, 90, 55, 16))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(85, 620, 300, 16))
        self.label_3.setObjectName("label")
        self.groupBox_4.raise_()
        self.groupBox_3.raise_()
        self.groupBox.raise_()
        self.pushButton.raise_()
        self.groupBox_2.raise_()
        self.label.raise_()
        self.label_2.raise_()
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.menuBar = QtWidgets.QMenuBar(MainWindow)
        self.menuBar.setGeometry(QtCore.QRect(0, 0, 364, 26))
        self.menuBar.setObjectName("menuBar")
        self.menuConversion_d_Images = QtWidgets.QMenu(self.menuBar)
        self.menuConversion_d_Images.setObjectName("menuConversion_d_Images")
        MainWindow.setMenuBar(self.menuBar)
        self.menuBar.addAction(self.menuConversion_d_Images.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", APP_NAME))
        self.pushButton.setText(_translate("MainWindow", "Lancer la conversion"))
        self.groupBox.setTitle(_translate("MainWindow", "Formats d'entrés"))
        self.checkBox.setText(_translate("MainWindow", "JPEG"))
        self.checkBox_2.setText(_translate("MainWindow", "JPG"))
        self.checkBox_3.setText(_translate("MainWindow", "WEBP"))
        self.checkBox_5.setText(_translate("MainWindow", "PNG"))
        self.checkBox_6.setText(_translate("MainWindow", "JFIF"))
        self.checkBox_7.setText(_translate("MainWindow", "Tous"))
        self.groupBox_2.setTitle(_translate("MainWindow", "Format de sortie"))
        self.comboBox_2.setItemText(0, _translate("MainWindow", "PNG"))
        self.comboBox_2.setItemText(1, _translate("MainWindow", "JPEG"))
        self.comboBox_2.setItemText(2, _translate("MainWindow", "JPG"))
        self.comboBox_2.setItemText(3, _translate("MainWindow", "WEBP"))
        self.groupBox_3.setTitle(_translate("MainWindow", "Répercussion sous-dossiers"))
        self.checkBox_4.setText(_translate("MainWindow", "Répercussion dans les sous-dossiers"))
        self.groupBox_4.setTitle(_translate("MainWindow", "Emplacement du dossier"))
        self.pushButton_2.setText(_translate("MainWindow", "Ouvrir un dossier"))
        self.label.setText(_translate("MainWindow", "<html><head/><body><p><img src=\":/newPrefix/main.png\"/></p></body></html>"))
        self.label_2.setText(_translate("MainWindow", VERSION))
        self.menuConversion_d_Images.setTitle(_translate("MainWindow", "Conversion d\'Images"))
    
        self.pushButton_2.clicked.connect(self.browsefolder)
        self.pushButton.clicked.connect(self.submit)
        self.checkBox_7.stateChanged.connect(self.check_tous)

    def browsefolder(self):
        folder=QFileDialog.getExistingDirectory()
        self.lineEdit.setText(folder)
        self.folder = folder

    def check_tous(self, int):
        if self.checkBox_7.isChecked():
            self.checkBox.setChecked(True)
            self.checkBox_2.setChecked(True)
            self.checkBox_3.setChecked(True)
            self.checkBox_5.setChecked(True)
            self.checkBox_6.setChecked(True)
            
            self.checkBox.setEnabled(False)
            self.checkBox_2.setEnabled(False)
            self.checkBox_3.setEnabled(False)
            self.checkBox_5.setEnabled(False)
            self.checkBox_6.setEnabled(False)
        else:
            self.checkBox.setChecked(False)
            self.checkBox_2.setChecked(False)
            self.checkBox_3.setChecked(False)
            self.checkBox_5.setChecked(False)
            self.checkBox_6.setChecked(False)
            
            self.checkBox.setEnabled(True)
            self.checkBox_2.setEnabled(True)
            self.checkBox_3.setEnabled(True)
            self.checkBox_5.setEnabled(True)
            self.checkBox_6.setEnabled(True)

    def submit(self):
        if self.folder == "":
            self.label_3.setGeometry(QtCore.QRect(85, 620, 300, 16))
            self.label_3.setText("Merci de préciser un dossier !")
        else:
            if self.checkBox.isChecked() == True:
                self.format.append(".jpeg")
            if self.checkBox_2.isChecked() == True:
                self.format.append(".jpg")
            if self.checkBox_3.isChecked() == True:
                self.format.append(".webp")
            if self.checkBox_5.isChecked() == True:
                self.format.append(".png")
            if self.checkBox_6.isChecked() == True:
                self.format.append(".jfif")
            if self.format == []:
                self.label_3.setGeometry(QtCore.QRect(40, 620, 300, 16))
                self.label_3.setText("Merci de préciser au moins un format d'entrée !")
            else:
                if self.folder[-1] != "/":
                    self.folder = self.folder + "/"
                # , self.comboBox.currentText()
                self.label_3.setGeometry(QtCore.QRect(110, 620, 300, 16))
                self.label_3.setText("Conversion en cours ...")
                if self.checkBox_4.isChecked() == True:
                    subdirectory = [f.path for f in os.scandir(self.folder) if f.is_dir()]
                    for d in subdirectory:
                        d = d + "/"
                        conversion(d, self.format, self.comboBox_2.currentText().lower())
                else:
                    conversion(self.folder, self.format, self.comboBox_2.currentText().lower())
                self.label_3.setText("Conversion terminé !")
import file 

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())