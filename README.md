# Proyecto de Análisis de Encuestas Clínicas

Este proyecto es una herramienta interactiva desarrollada en Python para gestionar y analizar datos de encuestas clínicas relacionadas con el consumo de alcohol y sus implicaciones en la salud. Utiliza **MySQL** como base de datos para almacenar los datos y **Tkinter** para proporcionar una interfaz gráfica amigable para el usuario. Además, incorpora funcionalidades avanzadas como generación de gráficos y exportación a Excel.

## Características principales

1. **Gestión de Datos (CRUD)**:  
   - Crear, leer, actualizar y eliminar registros de la base de datos.
   - Búsquedas personalizadas para filtrar encuestas por frecuencia de consumo de alcohol y pérdida de control.

2. **Visualización de Datos**:  
   - Generación de gráficos de barras para representar patrones de consumo.
   - Exportación de datos filtrados a un archivo Excel.

3. **Interfaz Gráfica de Usuario (GUI)**:  
   - Diseñada con Tkinter, incluye menús, botones y campos de entrada para realizar operaciones CRUD y análisis de datos.

4. **Conexión a Base de Datos MySQL**:  
   - Configuración para conectar con un servidor MySQL local y gestionar los datos de forma eficiente.

---

## Archivos del Proyecto

### 1. **`Conexion.py`**

Este archivo gestiona la conexión con la base de datos MySQL.  
**Código**:
```python
import mysql.connector

try:
    conexion = mysql.connector.connect(
        host="localhost",
        user="root",
        password="campusfp",
        database="encuestas",
        auth_plugin="mysql_native_password"
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
Funciones Clave:

Establece la conexión con la base de datos encuestas.
Maneja errores de conexión.
2. CRUD.py
Define las operaciones CRUD para la base de datos, además de consultas personalizadas.
Código Resumido:

python
Copiar código
def insertar_registro(conexion, datos):
    cursor = conexion.cursor()
    query = "INSERT INTO ENCUESTA (Edad, Sexo, Consumo, PerdidaControl) VALUES (%s, %s, %s, %s)"
    cursor.execute(query, datos)
    conexion.commit()

def consultar_todos(conexion):
    cursor = conexion.cursor()
    query = "SELECT * FROM ENCUESTA"
    cursor.execute(query)
    return cursor.fetchall()

# Más funciones disponibles: actualizar_registro, eliminar_registro, filtrar_por_consumo...
Funciones Clave:

insertar_registro: Inserta un nuevo registro en la tabla ENCUESTA.
consultar_todos: Recupera todos los registros.
Consultas avanzadas: Filtros basados en consumo y frecuencia de pérdida de control.
3. graficar_datos.py
Este archivo genera gráficos de barras basados en datos del DataFrame.
Código:

python
Copiar código
import matplotlib.pyplot as plt
import pandas as pd

def graficar_datos(df, columna_x, columna_y):
    plt.figure(figsize=(10, 5))
    plt.bar(df[columna_x], df[columna_y], color='skyblue')
    plt.xlabel(columna_x)
    plt.ylabel(columna_y)
    plt.title(f"Gráfico de {columna_y} vs {columna_x}")
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()
Funciones Clave:

graficar_datos: Crea gráficos interactivos para visualizar tendencias en los datos.
4. MAIN.py
Actúa como punto de entrada para la aplicación. Combina las funcionalidades de conexión, CRUD y visualización en la GUI.
Código Resumido:

python
Copiar código
import tkinter as tk
from tkinter import messagebox
from Conexion import conexion
from CRUD import consultar_todos, insertar_registro
from graficar_datos import graficar_datos

# Configuración de la ventana principal
ventana = tk.Tk()
ventana.title("Análisis de Encuestas Clínicas")
ventana.geometry("600x400")

# Funciones vinculadas a botones
def mostrar_datos():
    registros = consultar_todos(conexion)
    print(registros)

# Más lógica de interfaz...
ventana.mainloop()
Funciones Clave:

Proporciona una interfaz interactiva para ejecutar operaciones CRUD.
Botones conectados a las funciones definidas en CRUD.py.
Cómo Usar el Proyecto
Requisitos Previos
Software:

Python 3.x
MySQL Server
Librerías: mysql-connector-python, pandas, matplotlib, tkinter, openpyxl
Base de Datos:

Crea una base de datos MySQL llamada encuestas con la siguiente tabla:
sql
Copiar código
CREATE TABLE ENCUESTA (
    Id INT AUTO_INCREMENT PRIMARY KEY,
    Edad INT NOT NULL,
    Sexo VARCHAR(10) NOT NULL,
    Consumo VARCHAR(50) NOT NULL,
    PerdidaControl VARCHAR(50) NOT NULL
);
Configuración:

Actualiza las credenciales de MySQL en el archivo Conexion.py si es necesario.
Ejecución
Asegúrate de que el servidor MySQL esté en ejecución.
Ejecuta el archivo MAIN.py:
bash
Copiar código
python MAIN.py
Interactúa con la interfaz para realizar operaciones CRUD, analizar datos o generar gráficos.
