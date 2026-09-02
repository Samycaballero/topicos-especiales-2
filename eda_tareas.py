import pandas as pd

pd.set_option("display.max_columns", None)
pd.set_option("display.width", 200)

path = r"sales_data_sample.csv"
df = pd.read_csv(path, encoding="latin1")

# 3. Nuevo DataFrame con columnas seleccionadas
cols = ["ORDERNUMBER", "PRODUCTLINE", "COUNTRY", "CUSTOMERNAME",
        "QUANTITYORDERED", "PRICEEACH", "SALES", "DEALSIZE"]
df_sub = df[cols].copy()
print("=" * 80)
print("3. NUEVO DATAFRAME (head):")
print(df_sub.head())

# 4. Filtrar Vintage Cars
vintage = df_sub[df_sub["PRODUCTLINE"] == "Vintage Cars"]
print("\n" + "=" * 80)
print(f"4. Pedidos de Vintage Cars: {len(vintage)}")

# 5. País distinto de USA
vintage_no_usa = vintage[vintage["COUNTRY"] != "USA"]
print("\n" + "=" * 80)
print(f"5. Pedidos de Vintage Cars fuera de USA: {len(vintage_no_usa)}")

# 6. Ordenar por SALES desc, top 10
top10 = vintage_no_usa.sort_values("SALES", ascending=False)
print("\n" + "=" * 80)
print("6. TOP 10 (Vintage Cars, sin USA, ordenado por SALES desc):")
print(top10.head(10))

# 7. País más frecuente
pais_frecuente = top10["COUNTRY"].value_counts().idxmax()
print("\n" + "=" * 80)
print("7. País más frecuente en ese filtro:")
print(top10["COUNTRY"].value_counts())
print(f"-> Respuesta: {pais_frecuente}")

# 8. loc vs iloc sobre el resultado ya ordenado
print("\n" + "=" * 80)
print("8. df.loc[5] vs df.iloc[5] sobre 'top10' (ya ordenado):")
try:
    print("\ntop10.loc[5]:")
    print(top10.loc[5])
except KeyError as e:
    print(f"\ntop10.loc[5] -> KeyError: {e} (no existe una fila con índice ETIQUETA 5 tras el sort)")
print("\ntop10.iloc[5]:")
print(top10.iloc[5])

# 9. Tipo de dato de ORDERDATE
print("\n" + "=" * 80)
print("9. Tipo de dato de ORDERDATE (crudo, tal como llega del CSV):")
print(df["ORDERDATE"].dtype)
print("Ejemplo de valor:", df["ORDERDATE"].iloc[0], "-> tipo Python:", type(df["ORDERDATE"].iloc[0]))

# 10. Convertir a fecha
df["ORDERDATE"] = pd.to_datetime(df["ORDERDATE"])
print("\n" + "=" * 80)
print("10. ORDERDATE convertida con pd.to_datetime():")
print(df["ORDERDATE"].dtype)
print(df["ORDERDATE"].head())

# 11. COUNTRY a category y comparar memoria
print("\n" + "=" * 80)
print("11. Memoria ANTES de convertir COUNTRY a category:")
mem_antes = df.memory_usage(deep=True)
print(mem_antes)
print(f"\nTotal ANTES: {mem_antes.sum():,} bytes")
print(f"Memoria de la columna COUNTRY (object) ANTES: {mem_antes['COUNTRY']:,} bytes")

df["COUNTRY"] = df["COUNTRY"].astype("category")

mem_despues = df.memory_usage(deep=True)
print("\nMemoria DESPUÉS de convertir COUNTRY a category:")
print(mem_despues)
print(f"\nTotal DESPUÉS: {mem_despues.sum():,} bytes")
print(f"Memoria de la columna COUNTRY (category) DESPUÉS: {mem_despues['COUNTRY']:,} bytes")
ahorro = mem_antes['COUNTRY'] - mem_despues['COUNTRY']
print(f"\nAhorro en COUNTRY: {ahorro:,} bytes ({ahorro/mem_antes['COUNTRY']*100:.1f}%)")
