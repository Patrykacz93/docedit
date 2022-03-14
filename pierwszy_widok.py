from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(400, 300)
        self.przycisk = QtWidgets.QPushButton(Dialog)
        self.przycisk.setGeometry(QtCore.QRect(160, 240, 80, 23))
        self.przycisk.setObjectName("przycisk")
        self.etykieta = QtWidgets.QLabel(Dialog)
        self.etykieta.setGeometry(QtCore.QRect(170, 110, 59, 15))
        self.etykieta.setText("")
        self.etykieta.setObjectName("etykieta")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.przycisk.setText(_translate("Dialog", "Generuj!"))