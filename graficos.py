from pathlib import Path

import matplotlib.pyplot as plt

SALIDA = Path(__file__).parent / "Data" / "processed" / "graficos"


def grafico_ventas_por_categoria(df):
    SALIDA.mkdir(parents=True, exist_ok=True)

    datos = df.groupby("categoria")["total"].sum().sort_values(ascending=False)

    plt.figure(figsize=(8, 5))
    datos.plot(kind="bar", color="steelblue", edgecolor="black")
    plt.title("Total vendido por categoría")
    plt.xlabel("Categoría")
    plt.ylabel("Ingresos totales ($)")
    plt.xticks(rotation=0)

    plt.savefig(SALIDA / "ventas_por_categoria.png", bbox_inches="tight")
    print(f"Gráfico guardado en: {SALIDA / 'ventas_por_categoria.png'}")

    plt.show()
    plt.close()


def grafico_ventas_por_canal(df):

    SALIDA.mkdir(parents=True, exist_ok=True)

    datos = df.groupby("canal")["total"].sum().sort_values(ascending=False)

    plt.figure(figsize=(8, 5))
    datos.plot(kind="bar", color="darkorange", edgecolor="black")
    plt.title("Total vendido por canal (Online vs Tienda)")
    plt.xlabel("Canal")
    plt.ylabel("Ingresos totales ($)")
    plt.xticks(rotation=0)

    plt.savefig(SALIDA / "ventas_por_canal.png", bbox_inches="tight")
    print(f"Gráfico guardado en: {SALIDA / 'ventas_por_canal.png'}")

    plt.show()
    plt.close()


def graficar(df):
    grafico_ventas_por_categoria(df)
    grafico_ventas_por_canal(df)