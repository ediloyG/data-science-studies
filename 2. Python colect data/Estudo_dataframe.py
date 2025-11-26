import pandas as pd

# lista: uma coleção ordenada de elementos que pode ser de qualquer tipo 

listar_nomes = ['Lucas', 'João', 'Maria', 'José', 'Ana', 'Pedro', 'Paulo', 'Carlos', 'Ricardo', 'Marta']
print('Lista de nomes: \n', listar_nomes)
print('Primeiro nome: ', listar_nomes[0])
print('\n')

# dicionario: Estrutura composta de pares chave-valor

dicionario_pessoa = {
    'nome':'Ana',
    'idade': 25,
    'sexo': 'Feminino',
    'cidade': 'Macatuba',
    }

print('Dicionario pessoa:\n ', dicionario_pessoa)
print('Atributo do dicionario: \n', dicionario_pessoa.get('idade')) # get() retorna o valor da chave
print('\n')

# Lista de dicionario: Estrutura de dados que combina listas e dicionarios

dados =[
    {'nome':'Ana', 'idade': 25, 'sexo': 'Feminino', 'cidade': 'Macatuba'},
    {'nome':'Lucas', 'idade': 30, 'sexo': 'Masculino', 'cidade': 'Bauru'},
    {'nome':'João', 'idade': 35, 'sexo': 'Masculino', 'cidade': 'Pederneiras'},
]
# dataframe: Estrutura de dados bidimensional, semelhante a uma planilha

df = pd.DataFrame(dados)
print('Dataframe: \n', df)

# Selecionar coluna
print('Selecionar coluna nome: \n', df['nome'])
print('\n')

# Selecionar varias colunas
print('Selecionar colunas nome e idade: \n', df[['nome', 'idade']])
print('\n')

# Selecionar linha
print('Selecionar linha 0: \n', df.iloc[0]) # iloc() retorna a linha
print('\n')

# Adicionar nova coluna
df['salario'] = [2000, 3000, 4000]

# Adicionar um novo registro

df.loc[len(df)] = {
    'nome':'Marta',
    'idade': 40,
    'sexo': 'Feminino',
    'cidade': 'Bauru',
    'salario': 5000}

print('Dataframe com nova coluna e registro: \n', df)
print('\n')

# Remover coluna

df.drop('salario', axis=1, inplace=True) # axis=1 remove a coluna, inplace=True remove a coluna do dataframe
print('Dataframe sem a coluna salario: \n', df)
print('\n')

# Filtrando pessoas com mais de 20 anos
print('Pessoas com mais de 20 anos: \n', df[df['idade'] > 20]) # df['idade'] > 20 retorna as pessoas com mais de 20 anos
print('\n')

# Filtrando pessoas com mais de 20 anos e que moram em Bauru
print('Pessoas com mais de 20 anos e que moram em Bauru: \n', df[(df['idade'] > 20) & (df['cidade'] == 'Bauru')])
print('\n')

# Salvando do Dataframe em um arquivo CSV
df.to_csv('pessoas.csv', index=False) # index=False remove o indice do dataframe
print('Dataframe salvo em pessoas.csv')

# Lendo um arquivo CSV
df_ler = pd.read_csv('pessoas.csv')
print('Dataframe lido do arquivo pessoas.csv: \n', df_ler)