from DB.conexion import *

class C_Usuario:
    def tablaUsuario(self):
        cursor = (f"select * from usuario")
        rows = AskDataBase(cursor)
        return rows
    
    def TotalUser(self):
        return len(self.tablaUsuario())
    
    def TablaCargos(self):
        cursor = f"SELECT * FROM cargo"
        rows = AskDataBase(cursor)
        return rows

    def tablaUsuarioFull(self):
        cursor = f"select u.codigo,u.nombre,u.cargo,u.clave,e.act_noact from usuario u inner join estado e on u.estado = e.id_status"
        rows = AskDataBase(cursor)
        return rows
    def tablaUsuarioOneFull(self,idUsuario):
        cursor = f"select u.codigo,u.nombre,u.cargo,u.clave,e.act_noact from usuario u inner join estado e on u.estado = e.id_status where u.codigo = '{idUsuario}'"
        rows = AskDataBase(cursor)
        return rows
        
    
    def C_ValidarLogin(self,idUsuario):
        cursor = f"select codigo,clave from usuario where codigo = '{idUsuario}'"
        rows = AskDataBase(cursor)
        for rowss in rows:
            return rowss
        
    def validarUsuario(self,codigo):
        cadena = self.AddDeleteUsuario(f"select codigo from usuario where codigo={codigo}")
        print("Resultado de Validacion busqueda",cadena)
        id = 0
        for item in cadena:
            print("Aqui el Item ", id , item[0])
            if item[0]  == codigo:
                id = 1
                print("Val Item", id)
        return id


    def AddDeleteUsuario(self,cadena):
        cursor = cadena
        rows = AskDataBase(cursor)
        return rows
        
def EliminarUsuario(codigo):
    conn, cursor = conexion()
    
    cursor.execute(f"DELETE usuario WHERE codigo = {codigo}")
    conn.commit()
    
    CerrarConexion(cursor,conn)    
    
def NuevoUsuario(codigo,nombre,cargo,clave):
    conn, cursor = conexion()
    
    cursor.execute(f"INSERT INTO usuario (codigo,nombre,cargo,clave,estado) VALUES ({codigo},'{nombre}','{cargo}',{clave},1)")
    conn.commit()
    
    CerrarConexion(cursor,conn)
