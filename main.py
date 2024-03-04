import sys
from PyQt5 import QtWidgets
from Vista.vLogin import VentanaLogin
""" este es un comentario"""
if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    window = VentanaLogin()
    app.exec_()
