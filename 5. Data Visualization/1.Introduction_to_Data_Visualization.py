import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

df = pd.read_csv('clientes-v3-preparado.csv')
print(df.head().to_string())

# Mistrograma
plt.hist(df['salario']) # plt.hist cria um histograma
plt.show() # força visualização do gráfico

# Histrograma com paremetros
plt.figure(figsize=(10, 6)) # define o tamanho da figura
plt.hist(df['salario'], bins=10, color='blue', alpha=0.7, edgecolor='black') # bins define o número de barras do histograma, alpha define a transparência, edgecolor define a cor da borda
plt.title('Histograma - Distribuição de Salário') # título do gráfico
plt.xlabel('Salário') # nome do eixo x
plt.xticks(ticks=range(0, int(df['salario'].max()) + 2000, 2000)) # define os ticks do eixo x
plt.ylabel('Frequência') # nome do eixo y
plt.grid(True) # ativa a grade
plt.show()

# Multiplos gráficos
plt.figure(figsize=(10, 6))
plt.subplot(2, 2, 1) # cria uma grade 2x2 e ativa o primeiro gráfico
# Grafico de dispersão
plt.scatter(df['salario'], df['salario']) # cria um gráfico de dispersão
plt.title('Dispersão - salario vs salario')
plt.xlabel('Salário')
plt.ylabel('Salário')

plt.subplot(2, 2, 2)
plt.scatter(df['salario'], df['anos_experiencia'], color='#5883a8', alpha=0.6, s=30)
plt.title('Salário vs Anos de Experiência')
plt.xlabel('Salário')
plt.ylabel('Anos de Experiência')

# Mapa de calor
corr = df[['salario', 'anos_experiencia']].corr()
plt.subplot(2, 2, 3)
sns.heatmap(corr, annot = True, cmap='coolwarm') # cria um mapa de calor

plt.tight_layout
plt.show()