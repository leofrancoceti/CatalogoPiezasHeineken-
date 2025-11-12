import conexion as con
import sqlite3

def save(pieza):   
    try:
        db = con.conectar()
        cursor = db.cursor()
        
        sql = """
        INSERT INTO piezas (id_pieza, linea, equipo, tipo, cantidad, boquilla, material, imagen1, imagen2, imagen3) 
        VALUES(?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
        """
        
        valores = (
            pieza["id_pieza"],
            pieza["linea"],
            pieza["equipo"],
            pieza["tipo"],
            pieza["cantidad"],
            pieza["boquilla"],
            pieza["material"],
            pieza.get("imagen1"),
            pieza.get("imagen2"), 
            pieza.get("imagen3")
        )
        
        cursor.execute(sql, valores)
        creada = cursor.rowcount > 0
        db.commit()
        
        if creada:
            return {"respuesta": creada, "mensaje": "Pieza creada exitosamente"}
        else:
            return {"respuesta": creada, "mensaje": "No se pudo crear la pieza"}
            
    except Exception as ex:
        error_msg = str(ex)
        if "UNIQUE" in error_msg and "id_pieza" in error_msg:
            mensaje = "Ya existe una pieza con el mismo ID"
        elif "UNIQUE" in error_msg and "equipo" in error_msg:
            mensaje = "Ya existe una pieza con el mismo equipo"
        else:
            mensaje = error_msg
        return {"respuesta": False, "mensaje": mensaje}
    finally:
        if 'cursor' in locals():
            cursor.close()
        if 'db' in locals():
            db.close()

def fiind_all(): 
    try:
        db = con.conectar()
        cursor = db.cursor()
        cursor.execute("SELECT id_pieza, linea, equipo, tipo, cantidad, boquilla, material FROM piezas")
        piezas = cursor.fetchall()
        
        if piezas:
            return {"respuesta": True, "piezas": piezas, "mensaje": "Piezas encontradas"}
        else:
            return {"respuesta": False, "piezas": [], "mensaje": "No hay piezas registradas"} 
            
    except Exception as ex:
        return {"respuesta": False, "mensaje": str(ex)}
    finally:
        if 'cursor' in locals():
            cursor.close()
        if 'db' in locals():
            db.close()

def find(id_pieza): 
    try:
        db = con.conectar()
        cursor = db.cursor()
        cursor.execute("SELECT * FROM piezas WHERE id_pieza=?", (id_pieza,))
        res = cursor.fetchall()
        
        if res:
            info = res[0]
            pieza = {
                "id": info[0],
                "id_pieza": info[1],
                "linea": info[2],
                "equipo": info[3],
                "tipo": info[4],
                "cantidad": info[5],
                "boquilla": info[6],
                "material": info[7],
                "imagen1": info[8],
                "imagen2": info[9],
                "imagen3": info[10]
            }
            return {"respuesta": True, "pieza": pieza, "mensaje": "Pieza encontrada"}
        else:
            return {"respuesta": False, "mensaje": "No existe la pieza"} 
            
    except Exception as ex:
        return {"respuesta": False, "mensaje": str(ex)}
    finally:
        if 'cursor' in locals():
            cursor.close()
        if 'db' in locals():
            db.close()

def update(pieza):     
    try:
        db = con.conectar()
        cursor = db.cursor()
        
        sql = """
            UPDATE piezas
            SET linea=?, equipo=?, tipo=?, cantidad=?, boquilla=?, material=?, imagen1=?, imagen2=?, imagen3=?
            WHERE id_pieza=?
            """
            
        valores = (
            pieza["linea"],
            pieza["equipo"], 
            pieza["tipo"],
            pieza["cantidad"],
            pieza["boquilla"],
            pieza["material"],
            pieza.get("imagen1"),
            pieza.get("imagen2"),
            pieza.get("imagen3"),
            pieza["id_pieza"]
        )
        
        cursor.execute(sql, valores)
        actualizada = cursor.rowcount > 0  
        db.commit()
        
        if actualizada: 
            return {"respuesta": actualizada, "mensaje": "Pieza actualizada exitosamente"} 
        else:
            return {"respuesta": actualizada, "mensaje": "No existe la pieza o no se pudo actualizar"}
            
    except Exception as ex:
        return {"respuesta": False, "mensaje": str(ex)}
    finally:
        if 'cursor' in locals():
            cursor.close()
        if 'db' in locals():
            db.close()

def delete(id_pieza):
    try:
        db = con.conectar()
        cursor = db.cursor()
        sql = "DELETE FROM piezas WHERE id_pieza=?"
        cursor.execute(sql, (id_pieza,))
        eliminada = cursor.rowcount > 0  
        db.commit()
        
        if eliminada: 
            return {"respuesta": eliminada, "mensaje": "Pieza eliminada exitosamente"} 
        else:
            return {"respuesta": eliminada, "mensaje": "No existe la pieza o no se pudo eliminar"}
            
    except Exception as ex:
        return {"respuesta": False, "mensaje": str(ex)}
    finally:
        if 'cursor' in locals():
            cursor.close()
        if 'db' in locals():
            db.close()