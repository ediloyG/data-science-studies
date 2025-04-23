import pandas as pd
import numpy as np

pd.set_option('display.width', None)
pd.set_option('display.max_columns', None)

df = pd.read_csv('Clientes_remove_outliers.csv')

print(df.head())

# Mascara de cpf
df['cpf_mascara'] = df['cpf'].apply(lambda cpf: f'{cpf[3]}.***.***{cpf[-2:]}') # aplica marcação de cpf

# Corrige formatad da data

df['data'] = pd.to_datetime(df['data'], format='%Y-%m-%d', errors='coerce') # converte para data

data_atual = pd.to_datetime('today') #
df['data_atualizada'] = df['data'].where(df['data'] <= data_atual, pd.to_datetime('1900-01-01')) # se a data atualizador for menos que atual então atualiza para 1900-01-01
df['idade_ajustada'] = data_atual.year - df['data_atualizada'].dt.year # calcula a idade ajustada
df['idade_ajustada'] -=((data_atual.month <= df['data_atualizada'].dt.month) & (data_atual.day < df['data_atualizada'].dt.day)).astype(int) # ajusta a data de nascimento se o aniversario for no mesmo ano
df.loc[df['idade_ajustada'] > 100, 'idade_ajustada'] = np.nan # se a idade ajustada for maior que 100 então é nulo

# Corrigir campo multiplos informações

df['endereco_curto'] = df['endereco'].apply(lambda x: x.split('\n')[0].strip()) # separa o endereço e pega o primeiro item
df['bairro'] = df['endereco'].apply(lambda x: x.split('\n')[1].strip() if len(x.split('\n')) > 1 else 'Desconhecido') # separa o bairro e pega o segundo item
df['estado_sigla'] = df['endereco'].apply(lambda x: x.split(' / ')[-1].strip() if len(x.split('\n')) > 1 else 'Desconhecido') # separa o estado e pega o último item

# Verificar a formatação do endereço

df['endereco_curto'] = df['endereco_curto'].apply(lambda x: 'Endereço inválido' if pd.isna(x) or len(x) < 5 or len(x) > 150 else x) # se o endereço for maior que 50 ou menor que 5 então é inválido

# Corrigir dados erronios

df['cpf'] = df['cpf'].apply(lambda x: x if len(x) == 14 else 'CPF inválido') # se o cpf for diferente de 14 então é inválido

estado_br = ['AC', 'AL', 'AP', 'AM', 'BA', 'CE', 'DF', 'ES', 'GO', 'MA', 'MT', 'MS', 'MG', 'PA', 'PB', 'PR', 'PE', 'PI', 'RJ', 'RN', 'RS', 'RO', 'RR', 'SC', 'SP', 'SE', 'TO']
df['estado_sigla'] = df['estado_sigla'].str.upper().apply(lambda x: x if x in estado_br else 'Estado inválido') # se o estado não estiver na lista de estados então é inválido

print('Dados tratados: \n', df.head())

df['cpf'] = df['cpf_mascara'] # substitui o cpf pelo cpf mascarado
df['idade'] = df['idade_ajustada'] # substitui a idade pela idade ajustada
df['endereco'] = df['endereco_curto'] # substitui o endereço pelo endereço curto
df['estado'] = df['estado_sigla'] # substitui o estado pela sigla do estado
df_salvar = df[['cpf', 'idade', 'endereco', 'bairro', 'estado']] # seleciona as colunas para salvar
df_salvar.to_csv('Clientes_tratados.csv', index=False) # salva o arquivo

