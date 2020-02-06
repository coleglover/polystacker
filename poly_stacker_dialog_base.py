# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'poly_stacker_dialog_base.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_PolyStackerDialogBase(object):
    def setupUi(self, PolyStackerDialogBase):
        PolyStackerDialogBase.setObjectName("PolyStackerDialogBase")
        PolyStackerDialogBase.resize(363, 142)
        self.cancelBox = QtWidgets.QDialogButtonBox(PolyStackerDialogBase)
        self.cancelBox.setGeometry(QtCore.QRect(182, 97, 71, 32))
        self.cancelBox.setOrientation(QtCore.Qt.Horizontal)
        self.cancelBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel)
        self.cancelBox.setObjectName("cancelBox")
        self.comboBox = QtWidgets.QComboBox(PolyStackerDialogBase)
        self.comboBox.setGeometry(QtCore.QRect(68, 51, 231, 22))
        self.comboBox.setObjectName("comboBox")
        self.selectFeatureLabel = QtWidgets.QLabel(PolyStackerDialogBase)
        self.selectFeatureLabel.setGeometry(QtCore.QRect(71, 30, 211, 16))
        self.selectFeatureLabel.setObjectName("selectFeatureLabel")
        self.okButton = QtWidgets.QPushButton(PolyStackerDialogBase)
        self.okButton.setGeometry(QtCore.QRect(109, 101, 71, 23))
        self.okButton.setObjectName("okButton")

        self.retranslateUi(PolyStackerDialogBase)
        self.cancelBox.rejected.connect(PolyStackerDialogBase.reject)
        self.okButton.clicked.connect(PolyStackerDialogBase.accept)
        QtCore.QMetaObject.connectSlotsByName(PolyStackerDialogBase)

    def retranslateUi(self, PolyStackerDialogBase):
        _translate = QtCore.QCoreApplication.translate
        PolyStackerDialogBase.setWindowTitle(_translate("PolyStackerDialogBase", "Polygon Stacker"))
        self.selectFeatureLabel.setText(_translate("PolyStackerDialogBase", "Select the layer you want to stack"))
        self.okButton.setToolTip(_translate("PolyStackerDialogBase", "R"))
        self.okButton.setText(_translate("PolyStackerDialogBase", "OK"))
        self.okButton.setShortcut(_translate("PolyStackerDialogBase", "R"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    PolyStackerDialogBase = QtWidgets.QDialog()
    ui = Ui_PolyStackerDialogBase()
    ui.setupUi(PolyStackerDialogBase)
    PolyStackerDialogBase.show()
    sys.exit(app.exec_())

