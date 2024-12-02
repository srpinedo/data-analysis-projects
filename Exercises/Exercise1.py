#Realizar un gráfico personalizado (aplicar un estilo atractivo) donde se pueda analizar las ventas de los 8 productos (Producto A, Producto B y Producto C, ingresar los que faltan) en tres ciudades (Bogotá, Cali, Bucaramanga).

import matplotlib.pyplot as plt
import numpy as np

productos = ['Producto A', 'Producto B', 'Producto C', 'Producto D', 'Producto E', 'Producto F', 'Producto G', 'Producto H']
ventas = {
    'Bogotá': [120, 130, 140, 150, 160, 170, 180, 190],
    'Cali': [110, 115, 120, 125, 130, 135, 140, 145],
    'Bucaramanga': [100, 105, 110, 115, 120, 125, 130, 135]
}

x = np.arange(len(productos))
width = 0.3

fig, ax = plt.subplots(figsize=(10, 6))
ax.bar(x - width, ventas['Bogotá'], width, label='Bogotá', color='blue', alpha=0.7)
ax.bar(x, ventas['Cali'], width, label='Cali', color='green', alpha=0.7)
ax.bar(x + width, ventas['Bucaramanga'], width, label='Bucaramanga', color='orange', alpha=0.7)

ax.set_xlabel('Productos')
ax.set_ylabel('Ventas')
ax.set_title('Ventas de productos por ciudad')
ax.set_xticks(x)
ax.set_xticklabels(productos)
ax.legend()

plt.tight_layout()
plt.show()