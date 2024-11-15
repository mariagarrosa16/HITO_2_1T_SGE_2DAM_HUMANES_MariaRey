import pandas as pd
#METDODO PARA EXPOIRTAR LOS DATOS A UN ARCHIVO EXCEL 
def exportar_resultados_excel(df, nombre_archivo):
    if df is not None:
        df.to_excel(nombre_archivo, index=False)
        print(f"Datos exportados a {nombre_archivo} correctamente.")
    else:
        print("No se pudo exportar los datos debido a datos vacíos.")
