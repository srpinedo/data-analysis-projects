#Realizar un gráfico personalizado (aplicar un estilo atractivo) para visualizar la distribución de las puntuaciones en un examen según el nivel de motivación de los estudiantes, utilizando histogramas separados para baja, media y alta motivación.
import pandas as pd
import matplotlib.pyplot as plt

data = {
    'Puntuación': [50, 60, 65, 70, 75, 78, 80, 82, 85, 87, 90, 92, 94, 96, 98, 99, 100, 102, 103, 105],
    'Nivel de motivación': ['Baja', 'Media', 'Media', 'Alta', 'Alta', 'Media', 'Media', 'Alta', 
                            'Alta', 'Baja', 'Alta', 'Alta', 'Media', 'Alta', 'Alta', 'Media', 
                            'Alta', 'Media', 'Baja', 'Alta']
}

df = pd.DataFrame(data)

plt.figure(figsize=(10, 6))
sns.histplot(data=df, x='Puntuación', hue='Nivel de motivación', multiple='stack', kde=True, palette='viridis')
plt.title('Distribución de puntuaciones según el nivel de motivación')
plt.xlabel('Puntuación')
plt.ylabel('Frecuencia')
plt.show()