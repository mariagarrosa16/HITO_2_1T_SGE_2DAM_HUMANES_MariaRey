import mysql.connector

try:
    conexion = mysql.connector.connect(
        host="localhost",
        user="root",
        password="campusfp",
        database="encuestas",  
        auth_plugin = "mysql_native_password"
    )

    if conexion.is_connected():
        print("Conexión exitosa a la base de datos.")
    else:
        print("No se pudo conectar.")

except mysql.connector.Error as e:
    print(f"Error de conexión: {e}")
finally:
    if conexion.is_connected():
        conexion.close()
