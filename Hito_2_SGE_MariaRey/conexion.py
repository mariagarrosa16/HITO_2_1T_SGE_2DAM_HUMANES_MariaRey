import mysql.connector
#CLASE PARA CONECTARSE A LA BASE DE DATOS 
class Conexion_bd:
    def __init__(self):
        try:
            #CONECTAR A LA BASE D EDATOS 
            self.conexion = mysql.connector.connect(
                host="localhost",
                user="root",
                password="campusfp",
                database="ENCUESTAS",  
                auth_plugin="mysql_native_password"
            )

            #SE VERIFICA LA CONEXION 
            if self.conexion.is_connected():
                print("Conexión exitosa a la base de datos.")
            else:
                print("No se pudo conectar.")
                
            self.cursor = self.conexion.cursor()

        except mysql.connector.Error as e:
            print(f"Error de conexión: {e}")
            self.conexion = None
#FUNCION PARA EJECUTAR CONSULTAS SQL EN LA BASE DE DATOS 
    def ejecutar_query(self, query, datos=None):
        """
        Ejecutar una consulta SQL en la base de datos.
        """
        if self.conexion is not None:
            self.cursor.execute(query, datos)
            self.conexion.commit()
        else:
            print("No hay conexión a la base de datos.")
#METODO PARA OBTENER DATOS DE LA BD
    def obtener_datos(self, query):
    
        if self.conexion is not None:
            self.cursor.execute(query)
            return self.cursor.fetchall()
        return None
#METODO PARA CERRAR LA CONEXION
    def cerrar_conexion(self):
     
        if self.conexion is not None and self.conexion.is_connected():
            self.cursor.close()
            self.conexion.close()
            print("Conexión cerrada.")
