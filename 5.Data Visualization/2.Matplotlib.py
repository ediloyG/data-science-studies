import matplotlib.pyplot as plt
import pandas as pd

df = pd.read_csv('clientes-v3-preparado.csv')
print(df.head().to_string())

# Gráfico de Barras
df['nivel_educacao'].value_counts().plot(kind='bar', color='#90ee70')
plt.title('Divisão de escolaridade - 1')
plt.xlabel('Nivel de Educação')
plt.ylabel('Quantidade')
plt.xticks(rotation=0)
plt.show()

x = df['nivel_educacao'].value_counts().index
y = df['nivel_educacao'].value_counts().values 

plt.figure(figsize=(10, 6))
plt.bar(x, y, color='#60aa65')
plt.title('Divisão de escolaridade - 2')
plt.xlabel('Nivel de Educação')
plt.ylabel('Quantidade')
plt.show()

# Gráfico de Pizza
plt.figure(figsize=(10, 6))
plt.pie(y, labels=x, autopct='%.1f%%', startangle=90,)
plt.title('Distribuicao de Educacao')
plt.show()

# Gráfico de dispersão
plt.hexbin(df['idade'], df['salario'], gridsize=40, cmap='Blues')
plt.colorbar(label='Contagem dentro do bin')
plt.xlabel('Idade')
plt.ylabel('Salario')
plt.title('dispersão de Idade e Salario')
plt.show()

