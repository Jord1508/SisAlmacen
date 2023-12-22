import pyodbc
def conexion():
    server = 'JORD'
    database = 'druppy'
    username = 'sa'
    password = '1239875'
    driver = '{ODBC Driver 17 for SQL Server}'  # Asegúrate de tener el controlador adecuado instalado

    conn_str = f'SERVER={server};DATABASE={database};UID={username};PWD={password};DRIVER={driver}'
    conn = pyodbc.connect(conn_str)
    cursor = conn.cursor()
    return conn , cursor

def CerrarConexion(cursor,conn):
    cursor.close()
    conn.close()

def AskDataBase(stringing):
    conn, cursor = conexion()
    cursor.execute(stringing)
    rows = cursor.fetchall()
    CerrarConexion(cursor,conn)
    
    return rows

