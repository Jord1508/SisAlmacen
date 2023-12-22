from PyQt5 import QtWidgets, QtGui
from DB.conexion import *
from Controlador.funciones import *
from Controlador.usuario import *
f = C_Usuario()
class VentanaUsuario(QtWidgets.QMainWindow):

    def __init__(self,parent = None):
        super(VentanaUsuario,self).__init__(parent)
        func_Favicon(self,"venta.png")
        cargarUI("UI/vUsuario.ui", self)
        self.cargarTablaUsuario()
        self.comboCargo()
        
        #BTNs Pagina Principal      >>>   A
        self.btnCrear.clicked.connect(self.paginaB1) #conexion a la pagina crear
        self.btnBuscar.clicked.connect(self.paginaC2) #conexion a la pagina Buscar
        self.btnActualizar.clicked.connect(self.paginaD4)
        self.btnEliminar.clicked.connect(self.paginaC2)
        
            #BOTON CERRAR
        self.btnXCerrarA.clicked.connect(self.btn_exit)
        
        
        #BTNs Pagina Crear          >>>   B
        self.btn_insertData.clicked.connect(self.InsertarUsuario)
            #BOTON CERRAR
        self.btnXCerrarB.clicked.connect(self.btn_exit)
        self.btnCancelarCrearB.clicked.connect(self.cancelarCrear)
        
        #BTNs Pagina Buscar         >>>    C
        self.btnBuscarC.clicked.connect(self.BuscarCodigoC)
        self.btnUpdateC.clicked.connect(self.ToUpdatePageD4)
        self.btnXCerrarC.clicked.connect(self.btn_exit)
        self.btnCancelarC.clicked.connect(self.cancelarBuscar)
        self.btnDeleteC.clicked.connect(self.EliminarTuplaUsuario)
        
        #BTNs PAgina Actualizar
        self.btnBuscarD.clicked.connect(self.BuscarCodigoD)
        self.btnCancelarD.clicked.connect(self.paginaA0)
        self.btnXCerrarD.clicked.connect(self.btn_exit)
              
    #FUNCIONES DE BOTONES LATERALES
    def paginaA0(self):
        self.container.setCurrentIndex(0)
    
    def paginaB1(self):
        self.container.setCurrentIndex(1)
    
    def paginaC2(self):
        self.container.setCurrentIndex(2)
    def paginaD4(self):
        self.container.setCurrentIndex(3)
        
    def btn_exit(self):
        self.close()
        return ' Boton de salida'

    def cancelarCrear(self):
        self.inputCodigo.clear()
        self.inputNombre.clear()
        self.inputCargo.setCurrentIndex(0)
        self.inputClave.clear()
        self.container.setCurrentIndex(0)
        
    def cancelarBuscar(self):
        self.inputCodigoC.clear()
        self.container.setCurrentIndex(0)
        
    #FUNCIONES DE CARGA
    def cargarTablaUsuario(self):
        
        func_tblDatos(f.tablaUsuarioFull(),self.tblUsuario)
        func_tblDatos(f.tablaUsuarioFull(),self.tbl_rstlC3)      
        self.txtTotal_item.setText(f'{self.numUsuarios()} Usuarios')
        
    def numUsuarios(self):
        return len(f.tablaUsuarioFull())
    
    def InsertarUsuario(self):
        if self.validarTxtInputB1() == "":
            a = self.inputCodigo.text()
            b = self.inputNombre.text()
            c = self.inputCargo.currentText()
            d = self.inputClave.text()
            num = f.validarUsuario(a)
            if num == 0:
                NuevoUsuario(a,b,c,d)
                MensajeInformacionOk(self, "Registrar Cliente", "Usuario nuevo registrado")
                self.cargarTablaUsuario()
                self.cancelarCrear()
            else:
                MensajeInformacionOk(self, "Registrar Cliente", "Id de Usuario ya registrado")
        else:
            MensajeInformacionOk(self,"Registrar Cliente", "Error en " + self.validarTxtInputB1())
        
        
    def validarTxtInputB1(self):
        if self.inputCodigo.text() == "":
            self.inputCodigo.setFocus()
            return "Codigo del usuario...!!!"
        elif self.inputNombre.text() == "":
            self.inputNombre.setFocus()
            return "Nombre del usuario...!!!"
        elif self.inputCargo.currentText() == "Seleccione":
            self.inputCargo.setFocus()
            return "Cargo del usuario...!!!"
        elif self.inputClave.text() == "":
            self.inputClave.setFocus() 
            return "Password del usuario...!!!"
        else:
            return ""
        
    def validarC(self):
        if self.inputCodigoC.text() == "":
            self.inputCodigoC.setFocus()
            return "Codigo del Usuario...!!!"
        else:
            return ""
    def validarD(self):
        if self.inputCodigoD.text() == "":
            self.inputCodigoD.setFocus()
            return "Codigo del Usuario...!!!"
        else:
            return ""
        
    #ARREGLOS DE USUARIOS
    def comboCargo(self):
        
        func_CargarDataCombo(self.inputCargo,f.TablaCargos())
        func_CargarDataCombo(self.inputCargoD,f.TablaCargos())
        
    #  PAGINA C  BUSCAR
    def BuscarCodigoC(self):
        if self.validarC() == "":
            idUser = self.inputCodigoC.text()
            if f.validarUsuario(idUser) == 1:
                func_tblDatos(f.tablaUsuarioOneFull(idUser),self.tbl_rstlC3)
        else:
            MensajeInformacionOk(self, "Buscqueda C", "Error en tbl_rstlC3" + self.validarC())
    
    def EliminarTuplaUsuario(self):
        if self.validarC() == "":
            codigo = self.inputCodigoC.text()
            if f.validarUsuario(codigo) == 1:
                EliminarUsuario(codigo)
                MensajeInformacionOk(self, "Registro de Usuarios", "Usuario Eliminado Exitosamente...!!!")
                self.cargarTablaUsuario()
                self.paginaA0()
        else:
            MensajeInformacionOk(self, "Buscqueda C", "Error en tbl_rstlC3" + self.validarC())
            
    def ToUpdatePageD4(self):
        if self.validarC() == "":
            idUser = self.inputCodigoC.text()
            if f.validarUsuario(idUser) == 1:
                User = f.tablaUsuarioOneFull(idUser)
                for items in User:
                    print('Aqui el rstl De Act Nombre',items[1])
                    self.inputCodigoD.setText(items[0])
                    self.inputNombreD.setText(items[1])
                    self.inputClaveD.setText(items[4])
                self.paginaD4()
        else:
            self.paginaD4()
            
    def BuscarCodigoD(self):
        if self.validarD() == "":
            idUser = self.inputCodigoD.text()
            if f.validarUsuario(idUser) == 1:
                User = f.tablaUsuarioOneFull(idUser)
                for items in User:
                    print('Aqui el rstl De Act Nombre',items[1])
                    self.inputNombreD.setText(items[1])
                    self.inputClaveD.setText(items[4])
        else:
            MensajeInformacionOk(self, "Buscqueda C", "Error en " + self.validarD())
            