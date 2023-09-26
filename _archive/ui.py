import sys
import yaml
from PyQt5 import QtWidgets, QtCore, QtGui

class MainWindow(object):
    def setup_ui(self, form):
        form.setObjectName("Main Window")
        form.resize(752, 568)
        self.widget = QtWidgets.QWidget(form)


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    form = QtWidgets.QWidget()
    ui = MainWindow()
    ui.setup_ui(form)
    form.show()
    sys.exit(app.exec_())