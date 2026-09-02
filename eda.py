import pandas as pd

pd.set_option("display.max_columns", None)
pd.set_option("display.width", 200)

path = r"sales_data_sample.csv"
df = pd.read_csv(path, encoding="latin1")

print("=" * 80)
print("SHAPE:", df.shape)
print("=" * 80)
print("\nCOLUMNS AND DTYPES:")
print(df.dtypes)

print("\n" + "=" * 80)
print("NULL VALUES PER COLUMN:")
print(df.isnull().sum())

print("\n" + "=" * 80)
print("DUPLICATED ROWS:", df.duplicated().sum())

print("\n" + "=" * 80)
print("DESCRIBE (numeric):")
print(df.describe())

print("\n" + "=" * 80)
print("DESCRIBE (categorical):")
cat_cols = df.select_dtypes(include="object").columns
print(df[cat_cols].describe())

print("\n" + "=" * 80)
print("UNIQUE VALUES per key categorical columns:")
for col in ["STATUS", "PRODUCTLINE", "DEALSIZE", "COUNTRY", "TERRITORY", "YEAR_ID", "QTR_ID", "MONTH_ID"]:
    if col in df.columns:
        print(f"\n{col} ({df[col].nunique()} unique):")
        print(df[col].value_counts())

print("\n" + "=" * 80)
print("SALES by PRODUCTLINE:")
print(df.groupby("PRODUCTLINE")["SALES"].agg(["sum", "mean", "count"]).sort_values("sum", ascending=False))

print("\n" + "=" * 80)
print("SALES by YEAR_ID:")
print(df.groupby("YEAR_ID")["SALES"].agg(["sum", "mean", "count"]))

print("\n" + "=" * 80)
print("TOP 10 CUSTOMERS by SALES:")
print(df.groupby("CUSTOMERNAME")["SALES"].sum().sort_values(ascending=False).head(10))

print("\n" + "=" * 80)
print("TOP 10 COUNTRIES by SALES:")
print(df.groupby("COUNTRY")["SALES"].sum().sort_values(ascending=False).head(10))

print("\n" + "=" * 80)
print("CORRELATION (numeric columns):")
print(df.corr(numeric_only=True)["SALES"].sort_values(ascending=False))
