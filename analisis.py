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
    requisitos_reto(df)
    ventas_por_mes(df)

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

def requisitos_reto(df):
    print("\n--- REQUISITO DEL RETO: LOC, ILOC Y CONCAT ---")

    # 1. Uso de .loc (selección por etiqueta/condición y nombres de columna)
    ventas_vip = df.loc[df["segmento_cliente"] == "VIP", ["id_venta", "nombre_cliente", "total"]]
    print(f"Total de ventas realizadas a clientes VIP (usando .loc): {len(ventas_vip)}")

    # 2. Uso de .iloc (selección por posición numérica: fila 0, columna 'total')
    primera_venta_id = df.iloc[0, 0]
    print(f"Primer ID de venta en la tabla unida (usando .iloc[0, 0]): {primera_venta_id}")

    # 3. Uso de pd.concat() (unir verticalmente las 3 ventas más altas y las 3 más bajas)
    df_ordenado = df.sort_values(by="total", ascending=False)
    top_3_ventas = df_ordenado.iloc[0:3][["id_venta", "producto", "total"]]
    bottom_3_ventas = df_ordenado.iloc[-3:][["id_venta", "producto", "total"]]

    extremos_ventas = pd.concat([top_3_ventas, bottom_3_ventas], ignore_index=True)
    print("\nComparación de las 3 ventas más altas y 3 más bajas (usando pd.concat):")
    print(extremos_ventas)


def ventas_por_mes(df):
    """Bonus (Sección 10): calcular ventas totales por mes usando to_period('M')."""
    print("\n--- BONUS: VENTAS TOTALES POR MES ---")
    df_mes = df.copy()
    df_mes["mes"] = df_mes["fecha_venta"].dt.to_period("M")
    resumen_mes = df_mes.groupby("mes")["total"].sum()
    print(resumen_mes)
    mes_mayor = resumen_mes.idxmax()
    valor_mayor = resumen_mes.max()
    print(f"El mes con mayores ventas fue {mes_mayor} con un total de ${valor_mayor:,.2f}")