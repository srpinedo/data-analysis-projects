import pandas as pd

df = pd.read_csv('Resources/CSV Laboratorio 3 AD-B.csv')

print("Análisis inicial de los datos:")
print("\nValores faltantes:")
print(df.isnull().sum())

print("\nFilas duplicadas:")
print(df.duplicated().sum())

print("\nDistribución por ciudad:")
print(df['City'].value_counts())

df = df.drop_duplicates()

df['Category'] = df['Category'].str.strip()
df['Category'] = df['Category'].str.lower()
df['Category'] = df['Category'].replace({
    'cat c': 'category c',
    'cat-c': 'category c',
    'category b': 'category b',
    'category a': 'category a'
})

df['Category'] = df['Category'].fillna('unknown')
df['City'] = df['City'].fillna('unknown')
df['Value'] = df['Value'].fillna(0)

df['Date'] = pd.to_datetime(df['Date']).dt.strftime('%Y-%m-%d')

print("\nValidación final de los datos:")
print("\nValores faltantes después de la limpieza:")
print(df.isnull().sum())

print("\nCategorías únicas:")
print(df['Category'].unique())

df.to_csv('Resources/cleaned_lab3_data.csv', index=False)
