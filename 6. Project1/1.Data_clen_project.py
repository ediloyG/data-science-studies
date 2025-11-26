import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

pd.set_option('display.width', None)

df = pd.read_csv('ecommerce_preparados.csv')

# Contagens
total_nulos = df.isnull().sum().sum()
total_vazios = (df == '').sum().sum()
total_duplicados = df.duplicated().sum()

print(f"Total de valores nulos: {total_nulos}")
print(f"Total de campos vazios: {total_vazios}")
print(f"Total de linhas duplicadas: {total_duplicados}")

# Incluindo dados em campos vazios
df['Gênero'] = df['Gênero'].fillna('desconhecido')
df['Nota'] = df['Nota'].fillna(df['Nota'].mean())
df['Qtd_Vendidos_Cod'] = df['Qtd_Vendidos_Cod'].fillna(df['Qtd_Vendidos_Cod'].mean())
df['N_Avaliações'] = df['N_Avaliações'].fillna(df['N_Avaliações'].mean())
df['Desconto'] = df['Desconto'].fillna(df['Desconto'].mean())

# Histograma da coluna 'Nota'
plt.figure(figsize=(10, 6))
sns.histplot(df['Nota'].dropna(), bins=20, kde=True, color='skyblue')
plt.title('Distribuição das Notas dos Produtos', fontsize=16)
plt.xlabel('Nota', fontsize=12)
plt.ylabel('Quantidade de Produtos', fontsize=12)
plt.show()

# Dispersão entre 'Preço' e 'Nota'
plt.figure(figsize=(10, 6))
sns.scatterplot(x='Preço', y='Nota', data=df, color='purple')
plt.title('Dispersão entre Preço e Nota', fontsize=16)
plt.xlabel('Preço (R$)', fontsize=12)
plt.ylabel('Nota', fontsize=12)
plt.show()

# Mapa de calor das correlações
plt.figure(figsize=(14, 10))
corr = df[['Nota', 'N_Avaliações', 'Desconto', 'Preço']].corr()
sns.heatmap(corr, annot=True, cmap='coolwarm', linewidths=0.5)
plt.title('Mapa de Calor das Correlações', fontsize=16)
plt.show()


# Gráfico de barras para as 10 marcas mais frequentes
top_marcas = df['Marca'].value_counts().head(10)

plt.figure(figsize=(12, 6))
sns.barplot(x=top_marcas.index, y=top_marcas.values, palette='viridis')
plt.title('Top 10 Marcas Mais Frequentes', fontsize=16)
plt.xlabel('Marca', fontsize=12)
plt.ylabel('Quantidade de Produtos', fontsize=12)
plt.xticks(rotation=45)
plt.show()

# Gráfico de pizza para a distribuição de gêneros
genero_counts = df['Gênero'].value_counts()

plt.figure(figsize=(8, 8))
plt.pie(genero_counts, labels=genero_counts.index, autopct='%1.1f%%', startangle=140, colors=sns.color_palette('pastel'))
plt.title('Distribuição dos Gêneros dos Produtos', fontsize=16)
plt.axis('equal')
plt.show()

# Gráfico de densidade para preço
plt.figure(figsize=(10, 6))
sns.kdeplot(df['Preço'].dropna(), shade=True, color='green')
plt.title('Densidade do Preço dos Produtos', fontsize=16)
plt.xlabel('Preço (R$)', fontsize=12)
plt.ylabel('Densidade', fontsize=12)
plt.show()

# Grafico de regrassão para preço e nota
plt.figure(figsize=(10, 6))
sns.regplot(x='Preço', y='Nota', data=df, scatter_kws={'color': 'red'}, line_kws={'color': 'blue'})
plt.title('Relação entre Preço e Nota (Regressão Linear)', fontsize=16)
plt.xlabel('Preço (R$)', fontsize=12)
plt.ylabel('Nota', fontsize=12)
plt.show()

