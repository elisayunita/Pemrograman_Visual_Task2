# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'regisojol.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(640, 381)
        Form.setStyleSheet("font: 8pt \"Comic Sans MS\";")
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(130, 10, 377, 49))
        self.label.setStyleSheet("font-weight: 300;\n"
"font-size:35px;\n"
"color: rgb(76, 38, 0);")
        self.label.setObjectName("label")
        self.verticalLayoutWidget = QtWidgets.QWidget(Form)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(270, 90, 361, 211))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.lineEdit_3 = QtWidgets.QLineEdit(self.verticalLayoutWidget)
        self.lineEdit_3.setStyleSheet("background-color:rgba(0,0,0,0);\n"
"color: rgb(76, 38, 0);\n"
"border:none;\n"
"border-bottom:1px solid rgba(105,118,132,255);\n"
"padding-bottom:5px;\n"
"font-size:15px;")
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.verticalLayout.addWidget(self.lineEdit_3)
        self.lineEdit_4 = QtWidgets.QLineEdit(self.verticalLayoutWidget)
        self.lineEdit_4.setStyleSheet("background-color:rgba(0,0,0,0);\n"
"color: rgb(76, 38, 0);\n"
"border:none;\n"
"border-bottom:1px solid rgba(105,118,132,255);\n"
"padding-bottom:5px;\n"
"font-size:15px;")
        self.lineEdit_4.setObjectName("lineEdit_4")
        self.verticalLayout.addWidget(self.lineEdit_4)
        self.lineEdit_5 = QtWidgets.QLineEdit(self.verticalLayoutWidget)
        self.lineEdit_5.setStyleSheet("background-color:rgba(0,0,0,0);\n"
"color: rgb(76, 38, 0);\n"
"border:none;\n"
"border-bottom:1px solid rgba(105,118,132,255);\n"
"padding-bottom:5px;\n"
"font-size:15px;")
        self.lineEdit_5.setObjectName("lineEdit_5")
        self.verticalLayout.addWidget(self.lineEdit_5)
        self.lineEdit_6 = QtWidgets.QLineEdit(self.verticalLayoutWidget)
        self.lineEdit_6.setStyleSheet("background-color:rgba(0,0,0,0);\n"
"color: rgb(76, 38, 0);\n"
"border:none;\n"
"border-bottom:1px solid rgba(105,118,132,255);\n"
"padding-bottom:5px;\n"
"font-size:15px;")
        self.lineEdit_6.setObjectName("lineEdit_6")
        self.verticalLayout.addWidget(self.lineEdit_6)
        self.lineEdit_7 = QtWidgets.QLineEdit(self.verticalLayoutWidget)
        self.lineEdit_7.setStyleSheet("background-color:rgba(0,0,0,0);\n"
"color: rgb(76, 38, 0);\n"
"border:none;\n"
"border-bottom:1px solid rgba(105,118,132,255);\n"
"padding-bottom:5px;\n"
"font-size:15px;")
        self.lineEdit_7.setObjectName("lineEdit_7")
        self.verticalLayout.addWidget(self.lineEdit_7)
        self.lineEdit_8 = QtWidgets.QLineEdit(self.verticalLayoutWidget)
        self.lineEdit_8.setStyleSheet("background-color:rgba(0,0,0,0);\n"
"color: rgb(76, 38, 0);\n"
"border:none;\n"
"border-bottom:1px solid rgba(105,118,132,255);\n"
"padding-bottom:5px;\n"
"font-size:15px;")
        self.lineEdit_8.setObjectName("lineEdit_8")
        self.verticalLayout.addWidget(self.lineEdit_8)
        self.label_2 = QtWidgets.QLabel(Form)
        self.label_2.setGeometry(QtCore.QRect(-10, 60, 251, 231))
        self.label_2.setStyleSheet("image: url(:/newPrefix/ojol.png);")
        self.label_2.setText("")
        self.label_2.setObjectName("label_2")
        self.pushButton = QtWidgets.QPushButton(Form)
        self.pushButton.setGeometry(QtCore.QRect(400, 320, 101, 41))
        self.pushButton.setStyleSheet("QPushButton {\n"
"    background-color: rgb(0, 0, 0);\n"
"    border-radius: 10px;\n"
"    color: rgb(255, 255, 255);\n"
"    font-size:15px;\n"
"    font-weight:500;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: rgb(81, 40, 0);\n"
"}\n"
"\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: rgb(81, 40, 0);\n"
"}\n"
"\n"
"")
        self.pushButton.setObjectName("pushButton")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.label.setText(_translate("Form", "   Registrasi Akun Ojol"))
        self.lineEdit_3.setText(_translate("Form", "Nama Depan"))
        self.lineEdit_3.setPlaceholderText(_translate("Form", "Nama Lengkap"))
        self.lineEdit_4.setText(_translate("Form", "Nama Belakang"))
        self.lineEdit_4.setPlaceholderText(_translate("Form", "NIM"))
        self.lineEdit_5.setText(_translate("Form", "Tempat Tanggal Lahir"))
        self.lineEdit_5.setPlaceholderText(_translate("Form", "URL Github"))
        self.lineEdit_6.setText(_translate("Form", "Jenis Kelamin"))
        self.lineEdit_6.setPlaceholderText(_translate("Form", "URL Github"))
        self.lineEdit_7.setText(_translate("Form", "Buat Alamat Email (@gmail.com)"))
        self.lineEdit_7.setPlaceholderText(_translate("Form", "URL Github"))
        self.lineEdit_8.setText(_translate("Form", "Kata Sandi"))
        self.lineEdit_8.setPlaceholderText(_translate("Form", "URL Github"))
        self.pushButton.setText(_translate("Form", "Submit"))
import images_rc


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())
