import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import pandas as pd

archivo = "/home/hadoop/online_retail/online_retail.csv"

df = pd.read_csv(archivo)

df = df[
    (df["Quantity"] > 0) &
    (df["UnitPrice"] > 0)
].copy()

df["TotalVenta"] = df["Quantity"] * df["UnitPrice"]

ventas = df.groupby("Country")["TotalVenta"].sum()

ventas = ventas.sort_values(ascending=False).head(10)
ventas = ventas.sort_values()

plt.figure(figsize=(10, 6))
ventas.plot(kind="barh")

plt.title("Top 10 paises por ventas")
plt.xlabel("Ventas totales")
plt.ylabel("Pais")
plt.tight_layout()

plt.savefig(
    "/home/hadoop/online_retail/ventas_por_pais.png",
    dpi=150
)

print("Grafico creado correctamente.")
print("/home/hadoop/online_retail/ventas_por_pais,png")
