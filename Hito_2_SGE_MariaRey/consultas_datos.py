import pandas as pd
from conexion import Conexion_bd

class Consultas:
    def __init__(self):
        self.bd = Conexion_bd()
#FUNCION PARA OBTENER DATOS DESDE LA BASE DE DATOS
    def obtener_datos(self, query):
   
        if self.bd.conexion is not None:
            try:
                # USAMOS PANSAS.READ_SQL PARA PODER OBTENER LA DATAFRAME
                df = pd.read_sql(query, self.bd.conexion)
                print("Datos obtenidos:", df.head())  
                return df
            except Exception as e:
                print(f"Error al obtener los datos: {e}")
                return None
        else:
            print("No se pudo obtener los datos debido a un problema de conexión.")
            return None
# FUNCION PARA EXPORTAR RESULTADOS DE UNA CONSULTA A UN ARCHIVO EXCEL
    def exportar_a_excel(self, df, nombre_archivo):
     
        if df is not None:
            try:
                # Exportar el DataFrame a un archivo Excel
                df.to_excel(nombre_archivo, index=False)
                print(f"Datos exportados exitosamente a {nombre_archivo}.")
            except Exception as e:
                print(f"Error al exportar a Excel: {e}")
        else:
            print("No se pudo exportar a Excel debido a datos vacíos.")
 # FUNCION PARA INSERTAR UNA ENCUESTA
    def insertar_datos(self, consulta, params):
     
        if self.bd.conexion is not None:
            try:
                # Usamos el cursor para ejecutar la consulta con parámetros
                cursor = self.bd.conexion.cursor()
                cursor.execute(consulta, params)
                self.bd.conexion.commit()  # Confirmar la transacción
                print("Datos insertados correctamente.")
                return True
            except Exception as e:
                print(f"Error al insertar los datos: {e}")
                return False
        else:
            print("No se pudo insertar los datos debido a un problema de conexión.")
            return False
# Función para eliminar una encuesta
    def eliminar_datos(self, id_encuesta):
    
        if self.bd.conexion is not None:
            try:
                # Usamos el cursor para ejecutar la consulta de eliminación
                cursor = self.bd.conexion.cursor()
                consulta = "DELETE FROM ENCUESTA WHERE idEncuesta = %s"
                cursor.execute(consulta, (id_encuesta,))
                self.bd.conexion.commit()  # Confirmar la transacción
                if cursor.rowcount > 0:
                    print(f"Encuesta con ID {id_encuesta} eliminada correctamente.")
                    return True
                else:
                    print(f"No se encontró ninguna encuesta con el ID {id_encuesta}.")
                    return False
            except Exception as e:
                print(f"Error al eliminar los datos: {e}")
                return False
        else:
            print("No se pudo eliminar los datos debido a un problema de conexión.")
            return False
  #FUNCION PARA ACTUALIZAR DATOS 
    def actualizar_datos(self, consulta, params):
        if self.bd.conexion is not None:
            try:
                # Usamos el cursor para ejecutar la consulta de actualización con parámetros
                cursor = self.bd.conexion.cursor()
                cursor.execute(consulta, params)
                self.bd.conexion.commit()  # Confirmar la transacción
                if cursor.rowcount > 0:
                    print("Datos actualizados correctamente.")
                    return True
                else:
                    print("No se encontraron registros para actualizar.")
                    return False
            except Exception as e:
                print(f"Error al actualizar los datos: {e}")
                return False
        else:
            print("No se pudo actualizar los datos debido a un problema de conexión.")
            return False
    
#funcion para verificar si el id proporcionado existe 
    def verificar_id_unico(self, id_encuesta):
  
        query = "SELECT COUNT(*) FROM ENCUESTA WHERE idEncuesta = %s"
        df = self.obtener_datos(query, (id_encuesta,))
        if df is not None and df.iloc[0, 0] > 0:
            return False  # El ID ya existe
        return True  # El ID es único
#funcion para obtener el valor maximo de idunico     
    def obtener_max_id(self):
    
        query = "SELECT MAX(idEncuesta) FROM ENCUESTA"
        df = self.obtener_datos(query)
        if df is not None and not df.empty:
            max_id = df.iloc[0, 0]  # Obtiene el valor máximo de idEncuesta
            return max_id + 1  # Devuelve el siguiente id único
        return 1  # Si no hay registros, empieza desde 1
