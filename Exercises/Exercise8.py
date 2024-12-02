import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv('Resources/CSV Laboratorio 2 AD-B.csv')

df['Ingresos Totales'] = df['Precio_unitario'] * df['Cantidad_vendida']

ventas_agrupadas = df.groupby(['Sucursal', 'Mes'])['Cantidad_vendida'].sum().unstack()

ventas_agrupadas.plot(kind='bar', figsize=(10, 6))
plt.title('Ventas por Sucursal y Mes')
plt.xlabel('Sucursal')
plt.ylabel('Cantidad Vendida')
plt.legend(title='Mes', bbox_to_anchor=(1.05, 1), loc='upper left')
plt.tight_layout()
plt.show()

plt.figure(figsize=(8, 6))
sns.scatterplot(data=df, x='Precio_unitario', y='Cantidad_vendida', hue='Sucursal', palette='viridis')
plt.title('Relación entre Precio Unitario y Cantidad Vendida')
plt.xlabel('Precio Unitario')
plt.ylabel('Cantidad Vendida')
plt.legend(title='Sucursal', bbox_to_anchor=(1.05, 1), loc='upper left')
plt.tight_layout()
plt.show()
