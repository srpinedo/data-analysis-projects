import pandas as pd

df = pd.read_csv('Resources/CSV Laboratorio 2 AD-B.csv')

print(df.head())       
print(df.info())      
print(df.describe())  

df['Ingresos Totales'] = df['Precio_unitario'] * df['Cantidad_vendida']

productos_filtrados = df[df['Cantidad_vendida'] > 40]
print(productos_filtrados)

precios_altos = df.nlargest(10, 'Precio_unitario')
print(precios_altos)