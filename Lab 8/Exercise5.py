#Realizar un gráfico personalizado para aplicar un estilo atractivo, se requiere visualizar las ventas mensuales de tres tipos de vehículos (SUV, Sedan, y Hatchback) durante un año.

import matplotlib.pyplot as plt
meses = ['Enero', 'Febrero', 'Marzo', 'Abril', 'Mayo', 'Junio', 'Julio', 'Agosto', 
         'Septiembre', 'Octubre', 'Noviembre', 'Diciembre']
ventas_suv = [120, 130, 135, 140, 150, 160, 170, 180, 175, 185, 190, 200]
ventas_sedan = [100, 90, 95, 110, 120, 130, 140, 145, 150, 160, 170, 180]
ventas_hatchback = [80, 85, 90, 95, 100, 105, 110, 115, 120, 125, 130, 135]

fig, ax = plt.subplots(figsize=(10, 6))
ax.plot(meses, ventas_suv, label='SUV', marker='o', color='blue')
ax.plot(meses, ventas_sedan, label='Sedan', marker='s', color='green')
ax.plot(meses, ventas_hatchback, label='Hatchback', marker='^', color='red')

ax.set_xlabel('Meses')
ax.set_ylabel('Ventas')
ax.set_title('Ventas mensuales de vehículos')
ax.legend()

plt.xticks(rotation=45)
plt.tight_layout()
plt.show()