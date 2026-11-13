from pathlib import Path
import pandas as pd

PROCESSED = Path(__file__).parent / "Data" / "processed"


def validar_premerge(clientes, ventas):
    """Revisa que el merge se pueda hacer. Devuelve True si todo está bien, False si no."""
    print("=== VALIDACIÓN PRE-MERGE ===")

    if "id_cliente" not in clientes.columns or "id_cliente" not in ventas.columns:
        print("Error: falta la columna 'id_cliente' en alguna de las tablas.")
        return False
    print("- Columna 'id_cliente' presente en ambas tablas: OK")


    duplicados = clientes["id_cliente"].duplicated().sum()
    if duplicados > 0:
        print(f"Error: hay {duplicados} 'id_cliente' repetidos en clientes.")
        return False
    print("- Sin 'id_cliente' duplicados en clientes: OK")


    tipo_clientes = clientes["id_cliente"].dtype
    tipo_ventas = ventas["id_cliente"].dtype
    if tipo_clientes != tipo_ventas:
        print(
            f"Error: el tipo de 'id_cliente' no coincide "
            f"(clientes: {tipo_clientes}, ventas: {tipo_ventas})."
        )
        return False
    print(f"- Tipos de dato de 'id_cliente' coinciden ({tipo_ventas}): OK")

    ventas_sin_cliente = (~ventas["id_cliente"].isin(clientes["id_cliente"])).sum()
    print(f"- Ventas sin cliente asociado en clientes: {ventas_sin_cliente}")

    return True


def unir(clientes, ventas):
    """Une ventas con clientes usando 'id_cliente' y guarda el resultado en Data/processed/merge.csv."""
    if not validar_premerge(clientes, ventas):
        print("No se realizó el merge porque falló la validación previa.")
        return None

    df = ventas.merge(clientes, on="id_cliente", how="left", validate="m:1")

   # Guardamos el resultado en Data/processed/merge.csv
    PROCESSED.mkdir(parents=True, exist_ok=True)
    ruta_salida = PROCESSED / "merge.csv"
    df.to_csv(ruta_salida, index=False)

    print("=== RESULTADO DEL MERGE ===")
    print(f"Filas y columnas resultantes: {df.shape[0]} filas x {df.shape[1]} columnas")
    print(f"Archivo guardado en: {ruta_salida}")

    return df