
import pandas as pd

data = {
    'Nombre': ['Juan', 'Maria', 'Pedro', 'Ana', 'Luisa', 'Carlos', 'Juan'],
    'Edad': [25, 30, None, 29, 28, 200, 25],
    'Email': ['juan@mail.com', 'maria@mail.com', 'pedro@mail.com', 'ana@mail.com', 
              'luisa@mail.com', 'carlos@mail.com', 'juan@mail.com'],
    'Pais': ['colombia', 'Colombia', 'Mexico', 'Argentina', 'Colombia', 'Brazil', 'colombia'],
    'Genero': ['M', 'F', 'H', 'F', 'Femenino', 'M', 'M'],
    'Visitas': [5, 7, 6, 4, 8, 2, 5]
}

df = pd.DataFrame(data)

df['Edad'] = df['Edad'].fillna(df['Edad'].median())

df = df.drop_duplicates()

genero_map = {
    'M': 'Masculino',
    'H': 'Masculino',
    'F': 'Femenino'
}
df['Genero'] = df['Genero'].replace(genero_map)

df['Pais'] = df['Pais'].str.title()

df.loc[df['Edad'] > 120, 'Edad'] = df['Edad'].median()

print("DataFrame después de la limpieza:")
print(df)

print("\nInformación del DataFrame limpio:")
print(df.info())

