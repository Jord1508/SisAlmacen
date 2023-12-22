
from Vista.vLogin import *
from Controlador.funciones import *
from DB.conexion import *

class C_login:

    def C_ValidarLogin(self,idUsuario):
        user = idUsuario
        conn, cursor = conexion()
        cursor.execute(f"select codigo,clave from usuario where codigo = '{user}'")
        rows = cursor.fetchall()
        CerrarConexion(cursor,conn)
        for rowss in rows:
            return rowss

