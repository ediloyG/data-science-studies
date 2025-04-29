import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

df = pd.read_csv('clientes-v3-preparado.csv')
print(df.head().to_string())

# Gráfico de Dispersão com Seaborn
sns.jointplot(x='idade', y='salario', data=df, color='blue', alpha=0.5, kind='scatter') # outros tipos: 'kde', 'hist', 'hex'
plt.show()

# Gráfico de densidade
plt.figure(figsize=(10, 6))
sns.kdeplot(df['salario'], fill=True, color='blue')
plt.title('Distribuição de Salário')
plt.xlabel('Salário')
plt.show()

# Gráfico de Pairplot - Dispersão e Histogrma
sns.pairplot(df[['idade', 'salario', 'anos_experiencia', 'nivel_educacao']]) # nivel_educacao não é numérico não esta tratado par ser mostrado
plt.show()

# Gráfico de regrassão
sns.regplot(x='idade', y='salario', data=df, color='#278f65', scatter_kws={'alpha':0.5, 'color': '#34c289'})
plt.title('Regrassão de Idade  Salario')
plt.xlabel('Idade')
plt.ylabel('Salario')
plt.show()

#Gráfico countplot com hue
sns.countplot(x='estado_civil', hue='nivel_educacao', data=df, palette='pastel')
plt.xlabel('Estado Civil')
plt.ylabel('Quantidade Clientes')
plt.legend(title='Nivel de Educação')
plt.show()
