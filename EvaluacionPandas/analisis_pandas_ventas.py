
import pandas as pd


df = pd.read_csv("ventas_sinteticas_100k.csv", parse_dates=["FECHA"])

# 1
print("1. Total de registros:", len(df))

# 2
print("2. Ventas por estado:", df["ESTADO"].value_counts())

# 3
print("3. Valor total de ventas:", df["VALOR_VENTA"].sum())

# 4
print("4. Promedio comisión ventas cerradas:", df[df["ESTADO"]=="Cerrado"]["COMISION"].mean())

# 5
print("5. Ciudad con más ventas cerradas:", df[df["ESTADO"]=="Cerrado"]["CIUDAD"].value_counts().idxmax())

# 6
print("6. Valor total ventas por ciudad:", df.groupby("CIUDAD")["VALOR_VENTA"].sum())

# 7
print("7. Top 5 productos más vendidos:", df["PRODUCTO"].value_counts().head(5))

# 8
print("8. Productos únicos:", df["PRODUCTO"].nunique())

# 9
print("9. Vendedor con más ventas cerradas:", df[df["ESTADO"]=="Cerrado"]["VENDEDOR"].value_counts().idxmax())

# 10
max_sale = df.loc[df["VALOR_VENTA"].idxmax(), ["VALOR_VENTA","CLIENTE"]]
print("10. Venta mayor valor:", max_sale)

# 11
print("11. Ventas nulas o negativas:", len(df[(df["VALOR_VENTA"]<=0)|(df["COMISION"]<=0)]))

# 12
print("12. Media de ventas por mes:", df.groupby(df["FECHA"].dt.month)["VALOR_VENTA"].mean())

# 13
print("13. Mes con más ventas cerradas:", df[df["ESTADO"]=="Cerrado"].groupby(df["FECHA"].dt.month).size().idxmax())

# 14
print("14. Ventas por trimestre:", df.groupby(df["FECHA"].dt.to_period("Q")).size())

# 15
print("15. Productos en >3 ciudades:", df.groupby("PRODUCTO")["CIUDAD"].nunique()[lambda x: x>3])

# 16
print("16. Duplicados:", df.duplicated().sum())

# 17
print("17. Filas después de eliminar nulos:", len(df.dropna(subset=["CLIENTE","PRODUCTO","VALOR_VENTA"])))

