import sqlite3

def conectar():
    try:
        conexion = sqlite3.connect("Pieza1.db")
        cursor = conexion.cursor()
        
        sql = """
        CREATE TABLE IF NOT EXISTS piezas (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            id_pieza TEXT NOT NULL UNIQUE,
            linea INTEGER NOT NULL,
            equipo TEXT NOT NULL,
            tipo TEXT NOT NULL,
            cantidad INTEGER NOT NULL,
            boquilla TEXT NOT NULL,
            material TEXT NOT NULL,
            imagen1 BLOB,
            imagen2 BLOB,
            imagen3 BLOB
        )
        """     
        cursor.execute(sql)
        conexion.commit()
        return conexion
        
    except Exception as ex:
        print(f"Error de conexión: {ex}")
        return None