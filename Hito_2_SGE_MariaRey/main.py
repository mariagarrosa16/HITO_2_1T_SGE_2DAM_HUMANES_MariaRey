import tkinter as tk
from tkinter import ttk, messagebox
from PIL import Image, ImageTk
from consultas_datos import Consultas
from visualizacion_graficos import graficar_datos
from exportar_datos import exportar_resultados_excel

class Aplicacion:
    def __init__(self, master):
        self.master = master
        self.master.title("Interfaz de Salud y Consumo de Alcohol")
        self.master.geometry("800x600")

        # Menú principal
        self.menu = tk.Menu(master)
        master.config(menu=self.menu)

        self.menu_archivo = tk.Menu(self.menu)
        self.menu.add_cascade(label="Archivo", menu=self.menu_archivo)
        self.menu_archivo.add_command(label="Exportar a Excel", command=self.exportar_datos)
        self.menu_archivo.add_command(label="Salir", command=master.quit)

        # Botones y entradas
        self.label = tk.Label(master, text="Consumo de Alcohol y Salud")
        self.label.pack(pady=10)

        self.boton_consultar = tk.Button(master, text="Consultar Datos", command=self.consultar_datos)
        self.boton_consultar.pack(pady=5)

        self.boton_graficar = tk.Button(master, text="Generar Gráfico", command=self.generar_grafico)
        self.boton_graficar.pack(pady=5)

        self.boton_agregar = tk.Button(master, text="Añadir Datos", command=self.agregar_formulario)
        self.boton_agregar.pack(pady=5)
        self.boton_eliminar = tk.Button(master, text="Eliminar Datos", command=self.eliminar_datos)
        self.boton_eliminar.pack(pady=5)

        self.boton_actualizar = tk.Button(master, text="Actualizar Datos", command=self.actualizar_datos)
        self.boton_actualizar.pack(pady=5)
        # Filtros de búsqueda
        self.filtro_sexo_label = tk.Label(master, text="Sexo:")
        self.filtro_sexo_label.pack(pady=5)
        self.filtro_sexo = ttk.Combobox(master, values=["", "Hombre", "Mujer"])
        self.filtro_sexo.set("")  # Valor inicial vacío
        self.filtro_sexo.pack(pady=5)

        self.filtro_edad_label = tk.Label(master, text="Edad (Mayor que):")
        self.filtro_edad_label.pack(pady=5)
        self.filtro_edad = ttk.Entry(master)
        self.filtro_edad.pack(pady=5)

        # Crear el Treeview para mostrar los datos en forma de tabla
        self.treeview = ttk.Treeview(master, columns=("idEncuesta", "edad", "Sexo", "BebidasSemana", "CervezasSemana", 
                                                     "BebidasFinSemana", "BebidasDestiladasSemana", "VinosSemana", 
                                                     "PerdidasControl", "DiversionDependenciaAlcohol", 
                                                     "ProblemasDigestivos", "TensionAlta", "DolorCabeza"), show="headings")
        
        # Definir los encabezados de la tabla
        self.treeview.heading("idEncuesta", text="ID Encuesta")
        self.treeview.heading("edad", text="Edad")
        self.treeview.heading("Sexo", text="Sexo")
        self.treeview.heading("BebidasSemana", text="Bebidas/semana")
        self.treeview.heading("CervezasSemana", text="Cervezas/semana")
        self.treeview.heading("BebidasFinSemana", text="Bebidas fin de semana")
        self.treeview.heading("BebidasDestiladasSemana", text="Bebidas destiladas/semana")
        self.treeview.heading("VinosSemana", text="Vinos/semana")
        self.treeview.heading("PerdidasControl", text="Perdidas de control")
        self.treeview.heading("DiversionDependenciaAlcohol", text="Diversión/Dependencia")
        self.treeview.heading("ProblemasDigestivos", text="Problemas digestivos")
        self.treeview.heading("TensionAlta", text="Tensión alta")
        self.treeview.heading("DolorCabeza", text="Dolor de cabeza")

        # Colocar el Treeview en la ventana
        self.treeview.pack(pady=20, padx=20, fill="both", expand=True)
#FUNCION PARA AGREGAR NUEVOS DATOS A LA BASE DE DATOS 
    def agregar_formulario(self):
        """
        Abre una ventana emergente para agregar nuevos datos a la base de datos.
        """
        self.formulario_agregar = tk.Toplevel(self.master)
        self.formulario_agregar.title("Agregar Datos")
        self.formulario_agregar.geometry("400x700")  # Ajusta el tamaño según sea necesario

        # Etiquetas y campos de entrada para cada columna de la tabla
        self.label_edad = tk.Label(self.formulario_agregar, text="Edad:")
        self.label_edad.pack(pady=5)
        self.entry_edad = tk.Entry(self.formulario_agregar)
        self.entry_edad.pack(pady=5)

        self.label_sexo = tk.Label(self.formulario_agregar, text="Sexo:")
        self.label_sexo.pack(pady=5)
        self.combobox_sexo = ttk.Combobox(self.formulario_agregar, values=["Hombre", "Mujer"])
        self.combobox_sexo.pack(pady=5)

        self.label_bebidas_semana = tk.Label(self.formulario_agregar, text="Bebidas Semana:")
        self.label_bebidas_semana.pack(pady=5)
        self.entry_bebidas_semana = tk.Entry(self.formulario_agregar)
        self.entry_bebidas_semana.pack(pady=5)

        self.label_cervezas_semana = tk.Label(self.formulario_agregar, text="Cervezas Semana:")
        self.label_cervezas_semana.pack(pady=5)
        self.entry_cervezas_semana = tk.Entry(self.formulario_agregar)
        self.entry_cervezas_semana.pack(pady=5)

        self.label_bebidas_fin_semana = tk.Label(self.formulario_agregar, text="Bebidas Fin de Semana:")
        self.label_bebidas_fin_semana.pack(pady=5)
        self.entry_bebidas_fin_semana = tk.Entry(self.formulario_agregar)
        self.entry_bebidas_fin_semana.pack(pady=5)

        self.label_bebidas_destiladas_semana = tk.Label(self.formulario_agregar, text="Bebidas Destiladas Semana:")
        self.label_bebidas_destiladas_semana.pack(pady=5)
        self.entry_bebidas_destiladas_semana = tk.Entry(self.formulario_agregar)
        self.entry_bebidas_destiladas_semana.pack(pady=5)

        self.label_vinos_semana = tk.Label(self.formulario_agregar, text="Vinos Semana:")
        self.label_vinos_semana.pack(pady=5)
        self.entry_vinos_semana = tk.Entry(self.formulario_agregar)
        self.entry_vinos_semana.pack(pady=5)

        self.label_perdidas_control = tk.Label(self.formulario_agregar, text="Pérdidas de Control:")
        self.label_perdidas_control.pack(pady=5)
        self.entry_perdidas_control = tk.Entry(self.formulario_agregar)
        self.entry_perdidas_control.pack(pady=5)

        self.label_diversion_dependencia = tk.Label(self.formulario_agregar, text="Diversión o Dependencia de Alcohol:")
        self.label_diversion_dependencia.pack(pady=5)
        self.combobox_diversion_dependencia = ttk.Combobox(self.formulario_agregar, values=["Sí", "No"])
        self.combobox_diversion_dependencia.pack(pady=5)

        self.label_problemas_digestivos = tk.Label(self.formulario_agregar, text="Problemas Digestivos:")
        self.label_problemas_digestivos.pack(pady=5)
        self.combobox_problemas_digestivos = ttk.Combobox(self.formulario_agregar, values=["Sí", "No"])
        self.combobox_problemas_digestivos.pack(pady=5)

        self.label_tension_alta = tk.Label(self.formulario_agregar, text="Tensión Alta:")
        self.label_tension_alta.pack(pady=5)
        self.combobox_tension_alta = ttk.Combobox(self.formulario_agregar, values=["Sí", "No", "A veces"])
        self.combobox_tension_alta.pack(pady=5)

        self.label_dolor_cabeza = tk.Label(self.formulario_agregar, text="Dolor de Cabeza:")
        self.label_dolor_cabeza.pack(pady=5)
        self.combobox_dolor_cabeza = ttk.Combobox(self.formulario_agregar, values=["Sí", "No", "A veces"])
        self.combobox_dolor_cabeza.pack(pady=5)

        # Botón para guardar los datos
        self.boton_guardar = tk.Button(self.formulario_agregar, text="Guardar", command=self.guardar_datos)
        self.boton_guardar.pack(pady=10)
#GUARDAR LOS DATOS EN UNA BASE DE DATOS 
    def guardar_datos(self):

        edad = self.entry_edad.get()
        sexo = self.combobox_sexo.get()
        bebidas_semana = self.entry_bebidas_semana.get()
        cervezas_semana = self.entry_cervezas_semana.get()

        #VALIDACION DE DATOS 
        if not edad.isdigit() or not bebidas_semana.isdigit() or not cervezas_semana.isdigit():
            messagebox.showerror("Error", "Por favor, ingrese valores válidos para edad y consumo.")
            return
        
        #CRAER LA CONSULTA SQL
        consulta = """
            INSERT INTO ENCUESTA (edad, Sexo, BebidasSemana, CervezasSemana)
            VALUES (%s, %s, %s, %s)
        """
        params = (int(edad), sexo, int(bebidas_semana), int(cervezas_semana))

        # Ejecutar la consulta de inserción
        consultas = Consultas()
        success = consultas.insertar_datos(consulta, params)

        if success:
            messagebox.showinfo("Éxito", "Datos guardados correctamente.")
            self.formulario_agregar.destroy()  # Cerrar la ventana emergente
            self.consultar_datos()  # Refrescar los datos
        else:
            messagebox.showerror("Error", "No se pudo guardar los datos.")
#FUNCION PARA CONSUKTAR LOS DATOS DE LA BASE DE DATOS CON FILTROS Y MOSTRALOS EN UNA TABLA
    def consultar_datos(self):
     
        print("Consultando datos...") 
        consultas = Consultas()

        #SE OBTIENE LOS FILTROS DE LA INERFAZ
        sexo = self.filtro_sexo.get()
        edad = self.filtro_edad.get()

       #SE COMPRUEBA QUE LOS NUMEROS SEAN ENTEROS 
        try:
            edad = int(edad) if edad else None  
        except ValueError:
            edad = None  

       
        query = """
            SELECT idEncuesta, edad, Sexo, BebidasSemana, CervezasSemana, BebidasFinSemana,
                BebidasDestiladasSemana, VinosSemana, PerdidasControl, DiversionDependenciaAlcohol,
                ProblemasDigestivos, TensionAlta, DolorCabeza
            FROM ENCUESTA
            WHERE 1=1
        """

        if sexo:
            query += f" AND Sexo = '{sexo}'"
        if edad is not None:  
            query += f" AND edad > {edad}"

       
        print(f"Consulta SQL: {query}")

        
        datos = consultas.obtener_datos(query)

      
        if datos is None:
            print("No se pudo obtener los datos. Verifica la consulta o la conexión.")
        elif datos.empty:
            print("La consulta no devolvió resultados.")
        else:
            print("Datos obtenidos exitosamente.")
            
        #LIMPIA EL Treeview ANTES DE AGREGAR NUEVOS DATOS 
        for item in self.treeview.get_children():
            self.treeview.delete(item)

        if datos is not None and not datos.empty:
            #INSERTAR LOS DATOS EN EL  Treeview
            for index, row in datos.iterrows():
                self.treeview.insert("", "end", values=tuple(row))
            messagebox.showinfo("Consulta", "Consulta ejecutada correctamente.")
        else:
            messagebox.showerror("Error", "No se pudo obtener los datos.")
#METODO PARA GENERAR UN GRAFICO
    def generar_grafico(self):
   
        print("Generando gráfico...")  # Depuración
        consultas = Consultas()

        #CONSULTA PARA OBTNER LOS DATOS DE LA EDAD Y DE LAS BEBIDAD TOMADAS POR SEMNA A
        query = """
            SELECT edad, BebidasSemana
            FROM ENCUESTA
        """
        datos = consultas.obtener_datos(query)

        if datos is not None and not datos.empty:
            graficar_datos(datos, "edad", "BebidasSemana")
        else:
            messagebox.showerror("Error", "No se pudo generar el gráfico.")
#METODO PARA EXPORTAR LOS DATOS 
    def exportar_datos(self):
        
        print("Exportando datos...")  # Depuración
        consultas = Consultas()

        #CONSULTA DONDE SE OBTIENE LOS DATOS DE LA TABLA 
        query = """
            SELECT idEncuesta, edad, Sexo, BebidasSemana, CervezasSemana, BebidasFinSemana,
                   BebidasDestiladasSemana, VinosSemana, PerdidasControl, DiversionDependenciaAlcohol,
                   ProblemasDigestivos, TensionAlta, DolorCabeza
            FROM ENCUESTA
        """
        datos = consultas.obtener_datos(query)

        if datos is not None and not datos.empty:
            exportar_resultados_excel(datos, "resultado_consulta.xlsx")
            messagebox.showinfo("Exportación", "Datos exportados a Excel correctamente.")
        else:
            messagebox.showerror("Error", "No se pudo exportar los datos.")
    #FUNION PARA ELIMNAR DATOS
    def eliminar_datos(self):
       
        self.formulario_eliminar = tk.Toplevel(self.master)
        self.formulario_eliminar.title("Eliminar Datos")
        self.formulario_eliminar.geometry("300x200")

        # Etiqueta y campo de entrada para el ID
        self.label_id = tk.Label(self.formulario_eliminar, text="ID Encuesta a eliminar:")
        self.label_id.pack(pady=5)
        self.entry_id = tk.Entry(self.formulario_eliminar)
        self.entry_id.pack(pady=5)

        # Botón para confirmar eliminación
        self.boton_confirmar_eliminar = tk.Button(self.formulario_eliminar, text="Eliminar", command=self.confirmar_eliminar)
        self.boton_confirmar_eliminar.pack(pady=10)
    #FUNCION PARA VERIFICAR SI SE HA ELIMNADO 
    def confirmar_eliminar(self):
        id_encuesta = self.entry_id.get()

        if not id_encuesta.isdigit():
            messagebox.showerror("Error", "Por favor, ingrese un ID válido.")
            return

        consultas = Consultas()
        success = consultas.eliminar_datos(int(id_encuesta))

        if success:
            messagebox.showinfo("Éxito", "Datos eliminados correctamente.")
            self.formulario_eliminar.destroy()  # Cerrar la ventana emergente
            self.consultar_datos()  # Refrescar los datos
        else:
            messagebox.showerror("Error", "No se pudo eliminar los datos.")
    #fUNCION PARA ACTUALIZAR 
    def actualizar_datos(self):
       
        self.formulario_actualizar = tk.Toplevel(self.master)
        self.formulario_actualizar.title("Actualizar Datos")
        self.formulario_actualizar.geometry("400x300")

        # Etiquetas y campos de entrada para el ID y el nuevo valor
        self.label_id_actualizar = tk.Label(self.formulario_actualizar, text="ID Encuesta a actualizar:")
        self.label_id_actualizar.pack(pady=5)
        self.entry_id_actualizar = tk.Entry(self.formulario_actualizar)
        self.entry_id_actualizar.pack(pady=5)

        self.label_campo = tk.Label(self.formulario_actualizar, text="Campo a actualizar (ej. Edad, BebidasSemana):")
        self.label_campo.pack(pady=5)
        self.entry_campo = tk.Entry(self.formulario_actualizar)
        self.entry_campo.pack(pady=5)

        self.label_nuevo_valor = tk.Label(self.formulario_actualizar, text="Nuevo valor:")
        self.label_nuevo_valor.pack(pady=5)
        self.entry_nuevo_valor = tk.Entry(self.formulario_actualizar)
        self.entry_nuevo_valor.pack(pady=5)

        # Botón para confirmar actualización
        self.boton_confirmar_actualizar = tk.Button(self.formulario_actualizar, text="Actualizar", command=self.confirmar_actualizar)
        self.boton_confirmar_actualizar.pack(pady=10)
    def confirmar_actualizar(self):
        id_encuesta = self.entry_id_actualizar.get()
        campo = self.entry_campo.get()
        nuevo_valor = self.entry_nuevo_valor.get()

        if not id_encuesta.isdigit() or not nuevo_valor:
            messagebox.showerror("Error", "Por favor, ingrese valores válidos.")
            return

        consultas = Consultas()
        success = consultas.actualizar_datos(int(id_encuesta), campo, nuevo_valor)

        if success:
            messagebox.showinfo("Éxito", "Datos actualizados correctamente.")
            self.formulario_actualizar.destroy()  # Cerrar la ventana emergente
            self.consultar_datos()  # Refrescar los datos
        else:
            messagebox.showerror("Error", "No se pudo actualizar los datos.")

# Verifica que el archivo se esté ejecutando directamente
if __name__ == "__main__":
    root = tk.Tk()  # Crea la ventana principal
    interfaz = Aplicacion(root)  # Instancia la interfaz
    root.mainloop()  # Mantén la ventana abierta
