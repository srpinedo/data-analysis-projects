import matplotlib.pyplot as plt
import numpy as np

asignaturas = ['Matemáticas', 'Ciencias', 'Historia', 'Inglés', 'Arte']
calificaciones = [85, 90, 78, 88, 92]

plt.figure(figsize=(10, 6))
plt.bar(asignaturas, calificaciones, color='skyblue')
plt.title('Calificaciones Promedio por Asignatura')
plt.ylabel('Calificación')
plt.ylim(0, 100)

for i, v in enumerate(calificaciones):
    plt.text(i, v + 1, str(v), ha='center')

plt.show()