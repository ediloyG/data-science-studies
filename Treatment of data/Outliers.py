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
