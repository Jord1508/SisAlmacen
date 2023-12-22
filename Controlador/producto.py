from DB.conexion import *

class C_producto:
    
    def tablaProductos(self):
        cursor = f"select p.nombre,p.codigo,c.nombre,p.cantidad,p.precio from producto p INNER JOIN categoria c on p.id_categoria = c.id_categoria"
        rows = AskDataBase(cursor)
        return rows
    
    def TablaCategoria(self):
        cursor = f"SELECT * FROM Categoria"
        rows = AskDataBase(cursor)
        return rows
    
    def TablaAlmacen(self):
        cursor = f"SELECT * FROM almacen"
        rows = AskDataBase(cursor)
        return rows
    
    def tablaProveedor(self):
        cursor = f"SELECT * FROM proveedor"
        rows = AskDataBase(cursor)
        return rows
    
    def TablaEstado():
        cursor = f"SELECT * FROM estado"
        rows = AskDataBase(cursor)
        return rows
    
def tablaUsuarioFull():
    conn, cursor = conexion()
    cursor.execute(f"select u.codigo,u.nombre,u.cargo,u.clave,e.act_noact from usuario u inner join estado e on u.estado = e.id_status")
    rows = cursor.fetchall()
    
    CerrarConexion(cursor,conn)
    return rows

def AddDeleteUsuario(cadena):
    conn, cursor = conexion()
    cursor.execute(cadena)
    rows = cursor.fetchall()
    
    CerrarConexion(cursor,conn)
    return rows

def validarUsuario(codigo):
    cadena = AddDeleteUsuario(f"select id_producto from producto where id_producto={codigo}")
    print("Resultado de Validacion busqueda",cadena)
    id = 0
    for item in cadena:
        print("Aqui el Item ", id , item[0])
        if item[0]  == codigo:
            id = 1
            print("Val Item", id)
    return id
        
def EliminarUsuario(codigo):
    conn, cursor = conexion()
    
    cursor.execute(f"DELETE usuario WHERE codigo = {codigo}")
    conn.commit()
    
    CerrarConexion(cursor,conn)
    
    
def NuevoProducto(nombre,cantidad,precio,codigo,idCategoria,idEstado,idProveedor,idUsuario):
    conn, cursor = conexion()
    
    cursor.execute(f"insert into producto (nombre,cantidad,precio,codigo,id_categoria,id_estado,id_proveedor,id_usuario) values ('{nombre}',{cantidad},{precio},'{codigo}',{idCategoria},{idEstado},{idProveedor},{idUsuario})")
    conn.commit()
    
    CerrarConexion(cursor,conn)
    
def UltimoIDProducto():
    conn, cursor = conexion()
    
    cursor.execute(f"select max(id_producto) from producto")
    rows = cursor.fetchall()
    id = rows[0]
    id = id[0]
    
    CerrarConexion(cursor,conn)
    return id

def NuevoKardex(idProducto,idAlmacen,cantidad,ingreso):
    conn, cursor = conexion()
    
    cursor.execute(f"insert into kardex(id_producto,id_almacen,existencia,descripcion) values ({idProducto},{idAlmacen},{cantidad},'{ingreso}')")
    conn.commit()
    
    CerrarConexion(cursor,conn)
