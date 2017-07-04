# -*- coding: utf-8 -*-

# Password Manager Rasberry Pi Program
#
# Created by: Omar Ahmed
#
from PyQt5 import QtCore, QtGui, QtWidgets
import sys
from python.Views.scanFinger_widget_ui import Ui_Form

    #TODO: Create Authentication Functions



if __name__ == "__main__":
    # Display Main Screen
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())