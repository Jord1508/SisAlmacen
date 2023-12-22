from PyQt5 import QtWidgets, QtGui
from Controlador.funciones import *
from Controlador.login import *
from Vista.vPrincipal import *
f = C_login()
class VentanaLogin(QtWidgets.QMainWindow):
    def __init__(self,parent = None):
        super(VentanaLogin,self).__init__(parent)
        func_Favicon(self,"venta.png")
        cargarUI("UI/login.ui",self)
        
        self.txtPassword.setEchoMode(QtWidgets.QLineEdit.Password)
        self.btnIniciar.clicked.connect(self.iniciarSesion)
        self.show()

    def iniciarSesion(self):
        usuario = self.gettxtUsuario()
        pswd = self.gettxtPassword()
        User = f.C_ValidarLogin(usuario)
        if self.valInputs() == '':
            if User != None :
                if User[1] == pswd:
                    self.close()
                    vprincipal = VentanaPrincipal(self)
                    vprincipal.show()
                else:
                    self.limpiarClave()
                    MensajeError('Error de Sesion','Revise que la clave sea la correcta...!')
            else:
                self.limpiarUsuario()
                MensajeError('Error de Sesion','Revise que el Usuario sea el correcto...!')
        else:
            MensajeError('Error de Sesion', self.valInputs() )

    def valInputs(self):
        if self.gettxtUsuario() == '':
            self.txtUsuario.setFocus()
            return 'El campo de usuario esta vacio...!!'
        elif self.gettxtPassword() == '':
            self.txtPassword.setFocus()
            return 'El campo de contraseña esta vacio...!!'
        else:
            return ''
            
    def gettxtUsuario(self):
        return self.txtUsuario.text()
    def gettxtPassword(self):
        return self.txtPassword.text()
        
    def limpiarUsuario(self):
        self.txtUsuario.clear()
        self.txtUsuario.setFocus()
        
    def limpiarClave(self):
        self.txtPassword.clear()
        self.txtPassword.setFocus()
        