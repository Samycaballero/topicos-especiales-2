import pandas as pd
import matplotlib.pyplot as plt

path = r"sales_data_sample.csv"
df = pd.read_csv(path, encoding="latin1")
df["ORDERDATE"] = pd.to_datetime(df["ORDERDATE"])

fig, axes = plt.subplots(2, 2, figsize=(14, 10))

# 1. Sales by product line
pl = df.groupby("PRODUCTLINE")["SALES"].sum().sort_values(ascending=True)
axes[0, 0].barh(pl.index, pl.values, color="#4C72B0")
axes[0, 0].set_title("Ventas totales por línea de producto")
axes[0, 0].set_xlabel("Ventas ($)")

# 2. Monthly sales trend
monthly = df.set_index("ORDERDATE").resample("ME")["SALES"].sum()
axes[0, 1].plot(monthly.index, monthly.values, color="#DD8452")
axes[0, 1].set_title("Tendencia de ventas mensuales")
axes[0, 1].tick_params(axis="x", rotation=45)

# 3. Top 10 countries
top_countries = df.groupby("COUNTRY")["SALES"].sum().sort_values(ascending=False).head(10)
axes[1, 0].bar(top_countries.index, top_countries.values, color="#55A868")
axes[1, 0].set_title("Top 10 países por ventas")
axes[1, 0].tick_params(axis="x", rotation=60)

# 4. Deal size distribution
ds = df["DEALSIZE"].value_counts()
axes[1, 1].pie(ds.values, labels=ds.index, autopct="%1.1f%%", colors=["#C44E52", "#8172B2", "#937860"])
axes[1, 1].set_title("Distribución por tamaño de trato")

plt.tight_layout()
out_path = r"C:\Work\WdYn7\eda_overview.png"
plt.savefig(out_path, dpi=120)
print("Saved:", out_path)
