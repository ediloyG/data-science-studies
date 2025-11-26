\# 📊 Projeto de Análise e Pré-processamento de Credit Score



Este repositório representa a \*\*primeira etapa\*\* de um projeto completo de \*\*modelagem de Credit Score\*\*.  

O foco desta fase é realizar uma \*\*análise exploratória detalhada\*\* e um \*\*pré-processamento robusto\*\* da base de clientes, preparando-a para o treinamento de modelos de Machine Learning.



---



\## 📂 Sobre o Dataset



O conjunto de dados contém informações \*\*demográficas e financeiras\*\* de clientes, com o objetivo final de prever sua pontuação de crédito (`Credit Score`).



| Coluna               | Descrição                                         |

| -------------------- | ------------------------------------------------- |

| \*\*Age\*\*              | Idade do cliente.                                 |

| \*\*Gender\*\*           | Gênero do cliente.                                |

| \*\*Income\*\*           | Renda anual do cliente.                           |

| \*\*Education\*\*        | Nível de escolaridade.                            |

| \*\*Marital Status\*\*   | Estado civil.                                     |

| \*\*Number of Children\*\* | Número de filhos.                               |

| \*\*Home Ownership\*\*   | Indica posse ou aluguel de imóvel.                 |

| \*\*Credit Score\*\*     | Variável alvo: pontuação de crédito.              |



---



\## 🔎 Metodologia



O notebook segue um fluxo estruturado de preparação de dados:



\### 1. Carregamento e Limpeza

\- Importação dos dados a partir de `.csv`.

\- Inspeção inicial com `df.info()` e verificação de valores ausentes.



\### 2. Pré-processamento

\- \*\*Valores ausentes:\*\* preenchimento da coluna `Age` com a mediana.  

\- \*\*Conversão de tipos:\*\* `Income` convertido para numérico.  

\- \*\*Checagem de categorias:\*\* inspeção de colunas categóricas para consistência.  



\### 3. Análise Exploratória (EDA)

\- \*\*Univariada:\*\* histogramas, boxplots e contagem de categorias.  

\- \*\*Bivariada:\*\* estudo de relações como:

&nbsp; - Salário × Gênero  

&nbsp; - Salário × Educação  

&nbsp; - Score × Posse de imóvel  



\### 4. Preparação para ML

\- \*\*Codificação de variáveis:\*\*  

&nbsp; - `Label Encoding` para binárias (`Gender`, `Marital Status`, `Home Ownership`)  

&nbsp; - `One-Hot Encoding` para `Education`  

\- \*\*Correlação:\*\* matriz entre variáveis numéricas.  

\- \*\*Divisão treino/teste:\*\* 80%/20% com `stratify=y`.  

\- \*\*Balanceamento:\*\* aplicação do \*\*SMOTE\*\* apenas no conjunto de treino.  



---



\## 📈 Principais Insights



\- Clientes com \*\*maior escolaridade, renda mais alta e posse de imóvel próprio\*\* tendem a apresentar `Credit Score = High`.  

\- A base é naturalmente \*\*desbalanceada\*\*, predominando a classe \*High\*.  

\- O perfil médio do cliente é \*\*37 anos, casado, com ensino superior e casa própria\*\*.  



---



\## 🛠️ Tecnologias Utilizadas



\- \*\*Python 3.x\*\*  

\- \*\*Pandas\*\* → Manipulação e análise de dados  

\- \*\*Seaborn \& Matplotlib\*\* → Visualizações  

\- \*\*Scikit-learn\*\* → Pré-processamento e divisão dos dados  

\- \*\*Imbalanced-learn\*\* → Balanceamento com `SMOTE`  



---



\## 🚀 Próximos Passos



\- Testar modelos de classificação (Logistic Regression, Random Forest, XGBoost).  

\- Avaliar métricas de desempenho (Accuracy, Recall, Precision, F1-score).  

\- Criar visualizações interativas em dashboards.  



---



\## 👨‍💻 Autor



Projeto desenvolvido por \*\*\Ediloy\*\*  

📌 \*Estudante de TI e futuro Cientista de Dados\*  

Se este projeto te ajudou, considere deixar uma ⭐ no repositório!



