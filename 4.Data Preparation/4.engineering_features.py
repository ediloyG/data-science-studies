import pandas as pd
import numpy as np
from scipy import stats

pd.set_option('display.width', None)

df = pd.read_csv('clientes-v2-tratados.csv')

# transformação Logarítimica

df['Salario_log'] = np.log1p(df['Salario']) # Log1p é usado para evitar valores negativos e zeros

print("\nDataframe após transformação logarítmica do salario: \n", df.head())

#Transformação Box-Cox

df['Salario_boxcox'], _ = stats.boxcox(df)