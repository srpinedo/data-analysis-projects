import pandas as pd

data = {
    'Nombre': ['Carlos', 'Ana', 'Luis', 'Pedro', 'María', None],
    'Edad': [34, 29, None, 45, 25, 33],
    'Fecha Ingreso': ['2021-01-15', '2020/03/12', '2022-07-01', '2021/12/01', '2021-05-20', '2020-03-12'],
    'Resultado Prueba': ['Positivo', 'Negativo', 'Positivo', 'Positivo', 'Negativo', 'Negativo']
}

df = pd.DataFrame(data)
