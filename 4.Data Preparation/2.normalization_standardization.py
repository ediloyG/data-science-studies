import pandas as pd
from sklearn.preprocessing import StandardScaler, MinMaxScaler, RobustScaler

pd.set_option('display.width', None)
pd.set_option('display.max_columns', None)

df = pd.read_csv('clientes-v2-tratados.csv')

print(df.head())

df = df[['idade', 'salario']]

# Normalização - MinMaxScaler
scaler = MinMaxScaler()
df['idadeMinMaxScaler'] = scaler.fit_transform(df[['idade']]) # Normalização com intervalo de 0 a 1
df['salarioMinMaxScaler'] = scaler.fit_transform(df[['salario']]) # Normalização com intervalo de 0 a 1

min_max_scaler = MinMaxScaler(feature_range=(-1, 1))
df['idadeMinMaxScaler_mm'] = min_max_scaler.fit_transform(df[['idade']]) # Normalização com intervalo de -1 a 1
df['salarioMinMaxScaler_mm'] = min_max_scaler.fit_transform(df[['salario']]) # Normalização com intervalo de -1 a 1

# Padronização - StandardScaler
scaler = StandardScaler()
df['idadeStandardScaler'] = scaler.fit_transform(df[['idade']]) # Padronização com média 0 e desvio padrão 1
df['salarioStandardScaler'] = scaler.fit_transform(df[['salario']]) # Padronização com média 0 e desvio padrão 1

# Padronização - RobustScaler
scaler = RobustScaler()
df['idadeRobustScaler'] = scaler.fit_transform(df[['idade']]) # Padronização com mediana 0 e IQR 1
df['salarioRobustScaler'] = scaler.fit_transform(df[['salario']]) # Padronização com mediana 0 e IQR 1

print(df.head(15))

print("MinMaxScaler (de 0 a 1)")
print("Idade - MIn: {:.4f} Mean: {:.4f} Max: {:.4f} Std:{:.4f}".format(df['idadeMinMaxScaler'].min(),
                                                                       df['idadeMinMaxScaler'].max(),
                                                                       df['idadeMinMaxScaler'].mean(),
                                                                       df['idadeMinMaxScaler'].std()
                                                                       ))
print("\nSalario - MIn: {:.4f} Mean: {:.4f} Max: {:.4f} Std:{:.4f}".format(df['salarioMinMaxScaler'].min(),
                                                                         df['salarioMinMaxScaler'].max(),
                                                                         df['salarioMinMaxScaler'].mean(),
                                                                         df['salarioMinMaxScaler'].std()
                                                                        ))

print("\nMinMaxScaler (de -1 a 1)")
print("Idade - MIn: {:.4f} Mean: {:.4f} Max: {:.4f} Std:{:.4f}".format(df['idadeMinMaxScaler_mm'].min(),
                                                                       df['idadeMinMaxScaler_mm'].max(),
                                                                       df['idadeMinMaxScaler_mm'].mean(),
                                                                       df['idadeMinMaxScaler_mm'].std()
                                                                       ))
print("Salario - MIn: {:.4f} Mean: {:.4f} Max: {:.4f} Std:{:.4f}".format(df['salarioMinMaxScaler_mm'].min(),
                                                                       df['salarioMinMaxScaler_mm'].max(),
                                                                       df['salarioMinMaxScaler_mm'].mean(),
                                                                       df['salarioMinMaxScaler_mm'].std()
                                                                       ))

print("\nStandardScaler(ajuste a media a 0 e desvio padrao 1):")
print("Idade - MIn: {:.4f} Mean: {:.18f} Max: {:.4f} Std:{:.4f}".format(df['idadeStandardScaler'].min(),
                                                                       df['idadeStandardScaler'].max(),
                                                                       df['idadeStandardScaler'].mean(),
                                                                       df['idadeStandardScaler'].std()
                                                                       ))
print("\nSalario - MIn: {:.4f} Mean: {:.18f} Max: {:.4f} Std:{:.4f}".format(df['salarioStandardScaler'].min(),
                                                                       df['salarioStandardScaler'].max(),
                                                                       df['salarioStandardScaler'].mean(),
                                                                       df['salarioStandardScaler'].std()
                                                                       ))

print("\nRobustScaler(ajuste a mediana e IQR ):")
print("Idade - MIn: {:.4f} Mean: {:.4} Max: {:.4f} Std:{:.4f}".format(df['idadeRobustScaler'].min(),
                                                                       df['idadeRobustScaler'].max(),
                                                                       df['idadeRobustScaler'].mean(),
                                                                       df['idadeRobustScaler'].std()
                                                                       ))
print("\nSalario - MIn: {:.4f} Mean: {:.4f} Max: {:.4f} Std:{:.4f}".format(df['salarioRobustScaler'].min(),
                                                                       df['salarioRobustScaler'].max(),
                                                                       df['salarioRobustScaler'].mean(),
                                                                       df['salarioRobustScaler'].std()
                                                                       ))

