import sys
from PyQt5 import QtWidgets
from Vista.vLogin import VentanaLogin

if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    window = VentanaLogin()
    app.exec_()
