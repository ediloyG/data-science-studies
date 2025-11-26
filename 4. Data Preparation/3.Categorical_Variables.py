import pandas as pd
from sklearn.preprocessing import LabelEncoder

pd.set_option('display.width', None)

df = pd.read_csv('clientes-v2-tratados.csv')

print(df.head())

# Codificação one-hot para 'estado-civil'
df = pd.concat([df, pd.get_dummies(df['estado_civil'], prefix='estado_civil')], axis=1)

print("\nDataframe após codificação one-hot: \n", df.head())

# Codificação ordinal para 'nivel-educacao'
educacao_ordem = {'Ensino Fundamental': 1,
                   'Ensino Médio': 2,
                   'Ensino Superior': 3,
                   'Pós-Graduação': 4}
df['nivel_educacao_ordinal'] = df['nivel_educacao'].map(educacao_ordem)

print("\nDataframe após codificação ordinal para nivel_educacional: \n", df.head())

# transformar 'area_atuação' em categoria codificadas usando o método .cat.codes
df['area_atuacao'] = df['area_atuacao'].astype('category').cat.codes

print("\nDataframe após transformar area_atuacao em códigos numéricos: \n", df.head())

# LabelEncoder para 'estado_civil'
# LabelEncoder converte cada valor único em números de 0 a n_classes-1
LabelEncoder = LabelEncoder()
df['estado_civil'] = LabelEncoder.fit_transform(df['estado'])

print("\nDataframe após LabelEncoder para estado: \n", df.head())

