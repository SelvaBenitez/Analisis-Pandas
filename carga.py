import pandas as pd

def cargar_datos():
    ventas = pd.read_csv("Data/raw/ventas.csv")
    clientes = pd.read_csv("Data/raw/cliente.csv")

    return clientes, ventas
