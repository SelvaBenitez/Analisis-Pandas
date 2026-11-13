import pandas as pd

pd.set_option("display.width", 200)
pd.set_option("display.max_columns", 20)


def analizar(df):
    print("\nInfo general:")
    df.info()
    print("\nEstadísticas numéricas:")
    print(df.describe())

    ingresos_por_categoria(df)
    canal_que_mas_vende(df)
    clientes_vip_vs_regular(df)
    metodo_pago_mas_usado(df)
    top5_clientes(df)


def ingresos_por_categoria(df):
    print("\n--- 1. INGRESOS POR CATEGORÍA ---")
    ingresos = df.groupby("categoria")["total"].sum().sort_values(ascending=False)
    print(ingresos)
    print(f"Categoría que más ingresos genera: {ingresos.index[0]} (${ingresos.iloc[0]:,.2f})")


def canal_que_mas_vende(df):
  
    print("\n--- 2. VENTAS E INGRESOS POR CANAL ---")
    por_canal = (
        df.groupby("canal")
        .agg(ventas=("id_venta", "count"), ingresos=("total", "sum"))
        .sort_values(by="ingresos", ascending=False)
    )
    print(por_canal)


def clientes_vip_vs_regular(df):
    print("\n--- 3. CLIENTES VIP VS REGULAR ---")
    segmentos = df.groupby("segmento_cliente").agg(
        clientes=("id_cliente", "nunique"),
        compras=("id_venta", "count"),
        gasto_total=("total", "sum"),
    )
    segmentos["compras_por_cliente"] = (segmentos["compras"] / segmentos["clientes"]).round(2)
    segmentos["gasto_por_cliente"] = (segmentos["gasto_total"] / segmentos["clientes"]).round(2)
    print(segmentos)


def metodo_pago_mas_usado(df):
    print("\n--- 4. MÉTODO DE PAGO MÁS USADO ---")
    conteo = df["metodo_pago"].value_counts()
    print(conteo)
    print(f"Método de pago más usado: {conteo.index[0]} ({conteo.iloc[0]} ventas)")


def top5_clientes(df):
    print("\n--- 5. TOP 5 CLIENTES CON MÁS COMPRAS ---")
    top5 = (
        df.groupby(["id_cliente", "nombre_cliente"])
        .agg(compras=("id_venta", "count"), gasto_total=("total", "sum"))
        .sort_values(by=["compras", "gasto_total"], ascending=[False, False])
        .head(5)
    )
    print(top5)