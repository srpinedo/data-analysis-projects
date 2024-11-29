#Realizar un gráfico personalizado (aplicar un estilo atractivo) para visualizar la relación entre el número de horas estudiadas y la puntuación obtenida en un examen, utilizando el nivel de motivación como tercera variable (representado por el tamaño de los puntos)
import matplotlib.pyplot as plt
horas = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
puntuaciones = [50, 60, 65, 70, 75, 78, 80, 82, 85, 87, 90, 92, 94, 96, 98, 99, 100, 102, 103, 105]
motivacion = [20, 25, 30, 35, 40, 45, 50, 55, 60, 65, 70, 75, 80, 85, 90, 95, 100, 105, 110, 115]

plt.figure(figsize=(10, 6))
scatter = plt.scatter(horas, puntuaciones, s=motivacion, c=motivacion, cmap='viridis', alpha=0.7, edgecolor='k')
plt.colorbar(scatter, label='Nivel de motivación')
plt.xlabel('Horas estudiadas')
plt.ylabel('Puntuación en el examen')
plt.title('Relación entre horas estudiadas, puntuación y motivación')
plt.show()