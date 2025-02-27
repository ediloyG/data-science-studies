import pandas as pd

df = pd.read_csv('clientes.csv')

# remove dados

df.drop('pais', axis=1, inplace=True) # remove a colunas pais, inplace=True para aplicar a alteração no DataFrame
df.drop(2, axis=0, inplace=True) # remove a linha 2,

# normaliza campos de texto

df['nome'] = df['nome'].str.title() # normaliza o campo nome para a primeira letra maiúscula
df['endereco'] = df['endereco'].str.lower # normaliza o campo endereco para letras minúsculas
df['estado'] = df['estado'].str.upper() # normaliza o campo estado para letras maiúsculas 

# Converter tipo de dados

df['idade'] = df['idade'].astype('int') # converte o campo idade para inteiro

print('Nomalizar textos', df.head())

# Tratar valores nulos

df_fillna = df.fillna(0) # preenche os valores nulos com 0
df_dropna = df.dropna() # remove as linhas com valores nulos
df_dropna4 = df.dropna(thresh=4) # remove as linhas que tenham 4 ou mais valores nulos
df = df.dropna(subset=['cpf']) # remove as linhas com valores nulos no campo cpf

print('Valores nulos:\n', df.isnull().sum()) # exibe a quantidade de valores nulos
print('Qtd de registros nulos com fillna:', df_fillna.isnull().sum()) # exibe a quantidade de valores nulos
print('Qtd de registros nulos com dropna:', df_dropna.isnull().sum()) # exibe a quantidade de valores nulos
print('Qtd de registros nulos com dropna4:', df_dropna4.isnull().sum()) # exibe a quantidade de valores nulos
print('Qtd de registros nulos com CPF:', df.isnull().sum()) # exibe a quantidade de valores nulos

df.fillna({'estado':'Desconhecido'}, inplace=True) # preenche os valores nulos do campo estado com 'Desconhecido'
df['enderco'] = df['endereco'].fillna('não informado') # preenche os valores nulos do campo endereco com 'não informado'
df['idade_corrigida'] = df['idade'].fillna(df['idade'].mean()) # preenche os valores nulos do campo idade

# Trata formatado de dados

df['data_corrigida'] = pd.to_datetime(df['data'], format='%d/%m/%Y', errors = 'coerce') # converte a data para o formato datetime e preenche com NaT os valores inválidos

# Tratar valores duplicados

pri