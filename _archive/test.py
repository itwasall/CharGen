# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'F:\CharGen\test.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
import yaml

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(400, 300)
        self.gridLayoutWidget = QtWidgets.QWidget(Form)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(5, 50, 391, 241))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.scrollArea = QtWidgets.QScrollArea(self.gridLayoutWidget)
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scollWidget = QtWidgets.QWidget()
        self.scollWidget.setGeometry(QtCore.QRect(0, 0, 387, 237))
        self.scollWidget.setObjectName("scollWidget")
        self.text = QtCore.QUrl.fromLocalFile('data.yaml')
        self.outputTextBos = QtWidgets.QTextBrowser(self.scollWidget)
        self.outputTextBos.setGeometry(QtCore.QRect(5, 0, 381, 241))
        self.outputTextBos.setObjectName("outputTextBos")
        self.outputTextBos.setSource(self.text)
        self.scrollArea.setWidget(self.scollWidget)
        self.gridLayout.addWidget(self.scrollArea, 0, 0, 1, 1)
        self.verticalLayoutWidget = QtWidgets.QWidget(Form)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(2, 9, 391, 25))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.topButtonHBox = QtWidgets.QHBoxLayout(self.verticalLayoutWidget)
        self.topButtonHBox.setContentsMargins(0, 0, 0, 0)
        self.topButtonHBox.setObjectName("topButtonHBox")
        self.generateCharacter = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.generateCharacter.setObjectName("generateCharacter")
        self.topButtonHBox.addWidget(self.generateCharacter)
        self.loadYaml = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.loadYaml.setObjectName("loadYaml")
        self.topButtonHBox.addWidget(self.loadYaml)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.generateCharacter.setText(_translate("Form", "PushButton"))
        self.loadYaml.setText(_translate("Form", "PushButton"))


if __name__ == "__main__":
    with open('output.yaml') as f:
        out = yaml.safe_load(f)
    with open('data.yaml') as f:
        data = yaml.safe_load(f)
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())
