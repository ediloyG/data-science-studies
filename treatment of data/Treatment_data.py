import pandas as pd

df = pd.read_csv('clientes.csv')

# verifica os primeiros registros
print(df.head().to_string()) # to_string() para exibir todas as colunas

# verifica quantidade de linhas e colunas
print('quantidade de linhas e colunas:', df.shape)

# verifica os tipos de dados
print('Tipagem dos dados:', df.dtypes)

# Checar valores nulos
print('Valores nulos:', df.isnull().sum())