import matplotlib.pyplot as plt

sitios = ['Sitio A', 'Sitio B', 'Sitio C', 'Sitio D', 'Sitio E']
tiempos = [1.2, 2.5, 0.9, 3.0, 1.8]

plt.figure(figsize=(10, 6))
plt.bar(sitios, tiempos, color='lightgreen')
plt.title('Tiempo de Carga por Sitio Web')
plt.ylabel('Tiempo (segundos)')

for i, v in enumerate(tiempos):
    plt.text(i, v + 0.1, f'{v}s', ha='center')

plt.show()