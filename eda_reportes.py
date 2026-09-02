import pandas as pd

path = r"sales_data_sample.csv"
df = pd.read_csv(path, encoding="latin1")
df["ORDERDATE"] = pd.to_datetime(df["ORDERDATE"])

total_sales = df["SALES"].sum()

# Reporte 1: concentracion de clientes (Pareto)
by_cust = df.groupby("CUSTOMERNAME")["SALES"].sum().sort_values(ascending=False)
top5_share = by_cust.head(5).sum() / total_sales * 100
top10_share = by_cust.head(10).sum() / total_sales * 100
n_customers = df["CUSTOMERNAME"].nunique()
print(f"R1: {n_customers} clientes totales. Top 5 = {top5_share:.1f}% de ventas. Top 10 = {top10_share:.1f}%.")

# Reporte 2: estacionalidad
by_qtr = df.groupby("QTR_ID")["SALES"].sum()
q4_share = by_qtr[4] / total_sales * 100
print(f"\nR2: Ventas por trimestre:\n{by_qtr}")
print(f"Q4 = {q4_share:.1f}% del total de ventas anuales")

# Reporte 3: deal size grande, concentracion por producto
large = df[df["DEALSIZE"] == "Large"]
large_by_pl = large["PRODUCTLINE"].value_counts()
print(f"\nR3: Total pedidos 'Large': {len(large)} ({len(large)/len(df)*100:.1f}% de todos)")
print(f"Distribución de 'Large' por línea de producto:\n{large_by_pl}")
print(f"Venta promedio Large: ${large['SALES'].mean():,.2f} vs Small: ${df[df['DEALSIZE']=='Small']['SALES'].mean():,.2f}")

# Reporte 4: precio vs cantidad como driver de ventas
corr_price = df["PRICEEACH"].corr(df["SALES"])
corr_qty = df["QUANTITYORDERED"].corr(df["SALES"])
near_max_price = (df["PRICEEACH"] >= 95).mean() * 100
print(f"\nR4: Correlación PRICEEACH-SALES = {corr_price:.2f}, QUANTITYORDERED-SALES = {corr_qty:.2f}")
print(f"% de pedidos con PRICEEACH >= 95 (precio casi tope): {near_max_price:.1f}%")
