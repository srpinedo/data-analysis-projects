#Realizar un gráfico personalizado (aplicar un estilo atractivo) para visualizar la evolución de las ventas de tres productos (Papa, Cebolla, Tomate) a lo largo de 8 meses en tres ciudades diferentes.
import seaborn as sns
import matplotlib.pyplot as plt

meses = ['Enero', 'Febrero', 'Marzo', 'Abril', 'Mayo', 'Junio', 'Julio', 'Agosto']
ventas_papa = [100, 150, 200, 250, 300, 400, 300, 150]
ventas_cebolla = [90, 120, 160, 200, 240, 100, 200, 150]
ventas_tomate = [80, 110, 150, 190, 230, 330, 350, 240]

fig, ax = plt.subplots(figsize=(10, 6))
ax.plot(meses, ventas_papa, label='Papa (Cali)', marker='o', color='red')
ax.plot(meses, ventas_cebolla, label='Cebolla (Bogotá)', marker='s', color='purple')
ax.plot(meses, ventas_tomate, label='Tomate (Cartagena)', marker='^', color='green')

ax.set_xlabel('Meses')
ax.set_ylabel('Ventas')
ax.set_title('Evolución de las ventas por ciudad')
ax.legend()

plt.xticks(rotation=45)
plt.tight_layout()
plt.show()