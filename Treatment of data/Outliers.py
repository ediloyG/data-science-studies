import pandas as pd
from scipy import stats

pd.set_option('display.width', None)

df = pd.read_csv('clientes_tratados.csv')

df_filtro_basico = df[df['idade'] > 100]

print('Filtro básico \n', df_filtro_basico[['idade','idade']])

# Identificar z-score
z_scores = stats.zscore(df['idade'])
outliers_z = df[z_scores > 3]
print("Outliers pelo Z-score \n", outliers_z)

# Filtrar outliers pelo Z-score

df_zscore = df[(stats.zscore(df['idade']) < 3)]

# Identificar outliers pelo IQR
Q1 = df['idade'].quantile(0.25)
Q3 = df['idade'].quantile(0.75)
IQR = Q3 - Q1

Limite_abaixo = Q1 - 1.5 * IQR
Limite_alto = Q3 + 1.5 * IQR

print("Limites IQR: ", Limite_abaixo, Limite_alto) 

outliers_iqr = df[(df['idade'] < Limite_abaixo) | (df['idade'] > Limite_alto)]
print("Outliers pelo IQR \n", outliers_iqr)

# filtrar outliers pelo IQR
df_iqr = df[(df['idade'] >= Limite_abaixo) & (df['idade'] <= Limite_alto)]

Limite_abaixo = 1
Limite_alto = 100
df = df[(df['idade'] >= Limite_abaixo) & (df['idade'] <= Limite_alto)]

# Filtrar endereços invalidos
df['endereco'] = df['endereco'].apply(lambda x: 'Endereço inválido' if len(x.split('\n')) < 3 else x) # Se o endereço tiver menos de 3 linhas, considera inválido

# Tratar campo de texto
df['nome'] = df['nome'].apply(lambda x: 'Nome Invalido' if isinstance(x, str) and len(x) > 50 else x)
print('Qtd registros com nomes grandes: ',(df['nome'] == 'Nome Invalido').sum())

print ('Dados com Outliers Tratados: \n',df)

# Salvar dataframe
df.to_csv('Clientes_remove_outliers.csv', index=False)

