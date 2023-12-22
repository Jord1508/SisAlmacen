from PyQt5 import QtWidgets
from Controlador.producto import *
from Controlador.funciones import *
f = C_producto()

class VentanaCategoria(QtWidgets.QMainWindow):

    def __init__(self,parent = None):
        super(VentanaCategoria,self).__init__(parent)
        func_Favicon(self,"venta.png")
        cargarUI("UI/vCategoria.ui", self)
        """self.ComboBoxes()
        self.ComboEstado()
        self.ComboAlmacen()
        self.ComboUsuario()
        self.ComboProveedor()"""
        
        #BTNs Pagina Principal      >>>   A
        self.btnCrear.clicked.connect(self.btn_2) #conexion a la pagina crear
        self.btnBuscar.clicked.connect(self.btn_3) #conexion a la pagina Buscar
        self.btnActualizar.clicked.connect(self.btn_4)
        self.btnEliminar.clicked.connect(self.btn_5)
        
        self.btnRefrescarA.clicked.connect(self.cargarTabla)
            #BOTON CERRAR
        self.btnXCerrarA.clicked.connect(self.btn_exit)
        
        
        #BTNs Pagina Crear          >>>   B
        self.btn_insertData.clicked.connect(self.InsertarUsuario)
            #BOTON CERRAR
        self.btnXCerrarB.clicked.connect(self.btn_exit)
        self.btnCancelarCrearB.clicked.connect(self.cancelarCrear)
        
        #BTNs Pagina Buscar         >>>    C
        self.btnBuscarC.clicked.connect(self.BuscarCodigoC)
        #self.btnUpdateC
        #self.btnDeleteC
        self.btnXCerrarC.clicked.connect(self.btn_exit)
        self.btnCancelarC.clicked.connect(self.cancelarBuscar)
        self.btnDeleteC.clicked.connect(self.EliminarTuplaUsuario)
        
        #BTNs PAgina Actualizar
        self.btnCancelarD.clicked.connect(self.btn_1)
        self.btnXCerrarD.clicked.connect(self.btn_exit)
        
        #BTN PAgina Eliminar           >>> E
        self.btnEliminarE.clicked.connect(self.EliminarTuplaUsuarioE)
        self.btnXCerrarE.clicked.connect(self.btn_exit)
        self.btnCancelarE.clicked.connect(self.btn_1)
        
        
        
    def refrescarTabla(self):
        self.cargarTabla()
    #FUNCIONES DE BOTONES LATERALES
    def btn_1(self):
        self.container.setCurrentIndex(0)
    
    def btn_2(self):
        self.container.setCurrentIndex(1)
    
    def btn_3(self):
        self.container.setCurrentIndex(2)
    def btn_4(self):
        self.container.setCurrentIndex(3)
    def btn_5(self):
        self.container.setCurrentIndex(4)
    def btn_6(self):
        self.container.setCurrentIndex(5)
    def btn_exit(self):
        self.close()
        return ' Boton de salida'

    def cancelarCrear(self):
        self.inputCodigo.clear()
        self.inputNombre.clear()
        self.inputCantidad.clear()
        self.inputPrecio.clear()
        self.inputAlmacen.setCurrentIndex(0)
        self.inputCategoria.setCurrentIndex(0)
        self.inputEstado.setCurrentIndex(0)
        self.inputProveedor.setCurrentIndex(0)
        
        self.container.setCurrentIndex(0)
        
    def cancelarBuscar(self):
        self.txtCodigoC.setText("")
        self.txtNombreC.setText("")
        self.txtCargoC.setText("")
        self.txtClaveC.setText("")
        self.txtEstadoC.setText("")
        self.inputCodigoC.clear()
        self.container.setCurrentIndex(0)
        
    #FUNCIONES DE CARGA
    def cargarTabla(self):
        
        func_tblDatos(f.tablaProducto(),self.tblUsuario)
        self.txtTotal_item.setText(f'## Usuarios')
        
    def InsertarUsuario(self):
        if self.validar() == "":
            codigo = self.inputCodigo.text()
            nombre = self.inputNombre.text()
            cantidad = self.inputCantidad.text()
            precio = self.inputPrecio.text()
            idCategoria = int(self.inputCategoria.currentIndex())
            idEstado = int(self.inputEstado.currentIndex())
            idProveedor = int(self.inputProveedor.currentIndex())
            idUsuario = int(self.inputUsuario.currentIndex())
            idAlmacen = int(self.inputAlmacen.currentIndex())
            
            idProducto = UltimoIDProducto()
            
            idProducto = str(idProducto + 1)
            ingreso = str('INGRESO' + idProducto)
            print("Linea de id Proveedor",idProveedor)
            
            CADENA = (nombre,cantidad,precio,codigo,idCategoria,idEstado,idProveedor,idUsuario)
            
            print(CADENA)
            
            NuevoProducto(nombre,cantidad,precio,codigo,idCategoria,idEstado,idProveedor,idUsuario)
            NuevoKardex(idProducto,idAlmacen,cantidad,ingreso)
            QtWidgets.QMessageBox.information(self, "Registrar Cliente", "Usuario nuevo registrado", QtWidgets.QMessageBox.Ok)
            self.cancelarCrear()
            
        else:
            QtWidgets.QMessageBox.information(self, "Registrar Cliente", "Error en " + self.validar(), QtWidgets.QMessageBox.Ok)
        
        
    def validar(self):
        if self.inputCodigo.text() == "":
            self.inputCodigo.setFocus()
            return "Codigo del producto...!!!"
        elif self.inputNombre.text() == "":
            self.inputNombre.setFocus()
            return "Nombre del producto...!!!"
        elif self.inputCantidad.text() == "Seleccione":
            self.inputCantidad.setFocus()
            return "Cantidad...!!!"
        elif self.inputPrecio.text() == "":
            self.inputPrecio.setFocus() 
            return "Precio del producto...!!!"
        elif self.inputAlmacen.currentIndex() == 0:
            self.inputAlmacen.setFocus() 
            return "Almacen del producto...!!!"
        elif self.inputCategoria.currentIndex() == 0:
            self.inputCategoria.setFocus() 
            return "Categoria del producto...!!!"
        elif self.inputEstado.currentIndex() == 0:
            self.inputEstado.setFocus() 
            return "Estado del producto...!!!"
        elif self.inputProveedor.currentIndex() == 0:
            self.inputProveedor.setFocus() 
            return "Proveedor del producto...!!!"
        elif self.inputUsuario.currentIndex() == 0:
            self.inputUsuario.setFocus() 
            return "Usuario del producto...!!!"
        else:
            return ""
        
    def validarC(self):
        if self.inputCodigoC.text() == "":
            self.inputCodigoC.setFocus()
            return "campo codigo en blanco...!!!"
        else:
            return ""
        
    #ARREGLOS DE USUARIOS
    """def ComboBoxes(self):
        func_CargarDataCombo(f.TablaCategoria(),self.inputCategoria)"""
        
    def ComboEstado(self):        
        etiquet = []
        lista = f.TablaEstado()
        
        for item in lista:
            etiquet.append(item[1])
            
        self.inputEstado.addItems(etiquet)
        
    def ComboAlmacen(self):        
        etiquet = []
        lista = f.TablaAlmacen()
        
        for item in lista:
            etiquet.append(item[1])
            
        self.inputAlmacen.addItems(etiquet)
    def ComboUsuario(self):        
        etiquet = []
        lista = tablaUsuarioFull()
        
        for item in lista:
            etiquet.append(item[1])
            
        self.inputUsuario.addItems(etiquet)
    def ComboProveedor(self):        
        etiquet = []
        lista = f.tablaProveedor()
        
        for item in lista:
            etiquet.append(item[1])
            
        self.inputProveedor.addItems(etiquet)
    #  PAGINA C  BUSCAR
    def BuscarCodigoC(self):
        
        if self.validarC() == "":
            a = self.inputCodigoC.text()
            if validarUsuario(a) == 1:
                tupla = tablaUsuarioFull()
                for items in tupla:
                    codigo, nombre,cargo,clave,estado = items
                    if codigo == a:
                        self.txtCodigoC.setText(str(" " + codigo))
                        self.txtNombreC.setText(str(" " + nombre))
                        self.txtCargoC.setText(str(" " + cargo))
                        self.txtClaveC.setText(str(" " + clave))
                        self.txtEstadoC.setText(str(" " + estado))
        else:
            QtWidgets.QMessageBox.information(self, "Buscqueda C", "Error en " + self.validarC(), QtWidgets.QMessageBox.Ok)
    
    def EliminarTuplaUsuario(self):
        codigo = self.inputCodigoC.text()
        EliminarUsuario(codigo)
        QtWidgets.QMessageBox.information(self, "Registro de Usuarios", "Usuario Eliminado Exitosamente...!!!", QtWidgets.QMessageBox.Ok)
        self.container.setCurrentIndex(0)
    def EliminarTuplaUsuarioE(self):
        try:
            codigo = self.inputCodigoE.text()
            EliminarUsuario(codigo)
            QtWidgets.QMessageBox.information(self, "Eliminacion de Usuarios", "Usuario Eliminado Exitosamente...!!!", QtWidgets.QMessageBox.Ok)
            self.container.setCurrentIndex(0)
        except:
            QtWidgets.QMessageBox.information(self, "Eliminacion de Usuarios", "Usuario No encontrado...!!!", QtWidgets.QMessageBox.Ok)
            
        
