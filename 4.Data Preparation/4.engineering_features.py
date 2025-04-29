import pandas as pd
import numpy as np
from scipy import stats

pd.set_option('display.width', None)

df = pd.read_csv('clientes-v2-tratados.csv')

# transformação Logarítimica

df['Salario_log'] = np.log1p(df['Salario']) # Log1p é usado para evitar valores negativos e zeros

print("\nDataframe após transformação logarítmica do salario: \n", df.head())

# Transformação Box-Cox

df['Salario_boxcox'], _ = stats.boxcox(df)['salario'] +1 # Boxcox é usado para normalizar a distribuição de dados, tornando-a mais simétrica e próxima de uma distribuição normal. +1 se caso houver valores negativos ou zeros.

print("\nDataframe após transformação Box-Cox do salario: \n", df.head())

# Codificação de frequencia para 'estado'
estrado_freq = df['estado'].value_counts() / len(df) # contra os estados e divide pelo total de linhas do dataframe
df['estado_freq'] = df['estado'].map(estrado_freq) # mapeia os valores de estado para a frequencia calculada

print("\nDataframe após codificação de frequencia do estado: \n", df.head())

# Interações 
df['intreacao_idade_filhos'] = df['idade'] * df['numero_filhos'] # Multiplica a idade pelo número de filhos para criar uma nova variável que representa a interação entre essas duas variáveis.

print("\nDataframe após interação entre 'idade' e 'numero_filhos': \n", df.head())