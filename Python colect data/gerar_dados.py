import pandas as pd
import random
from faker import Faker

faker = Faker('pt_BR')

Dados_pessoas = []

for _ in range(10):
    nome = faker.name()
    cpf = faker.cpf()
    idade = random.randint(18, 60)
    data = faker.date_of_birth(minimum_age=idade, maximum_age=idade).strftime('%d/%m/%Y')
    endereco = faker.address()
    estado = faker.state()
    pais = 'Brasil'
    
    pessoa = {
        'nome': nome,
        'cpf': cpf,
        'idade': idade,
        'data_nascimento': data,
        'endereco': endereco,
        'estado': estado,
        'pais': pais
    }
    
    Dados_pessoas.append(pessoa)

df_pessoas = pd.DataFrame(Dados_pessoas)
print(df_pessoas)
print('\n')

    