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
