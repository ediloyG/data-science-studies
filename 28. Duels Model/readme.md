## ⚔️ Duelo de Modelos de Machine Learning

Este projeto tem como objetivo comparar o desempenho de **diferentes modelos de Machine Learning supervisionados** em um problema de **classificação binária**, utilizando um conjunto de dados real amplamente conhecido.

A proposta é avaliar, de forma estruturada, como diferentes algoritmos se comportam diante do mesmo problema, desde o **pré-processamento dos dados** até a **avaliação de desempenho dos modelos**.

---

## 🎯 Problema

- Prever a **classe alvo** a partir de variáveis demográficas e categóricas
- Comparar o desempenho de diferentes algoritmos de classificação
- Avaliar impacto de pré-processamento e balanceamento de classes
- Selecionar o modelo com melhor performance geral

---

## 📊 Conjunto de Dados

- Dataset de classificação supervisionada
- Contém variáveis numéricas e categóricas
- Presença de valores ausentes e desbalanceamento de classes
- Dados representativos de um problema real

---

## 🧠 Metodologia

### 1. Exploração e Preparação dos Dados
- Análise exploratória inicial (EDA)
- Tratamento de valores nulos
- Codificação de variáveis categóricas
- Normalização / padronização de atributos numéricos

### 2. Pré-processamento
- Separação entre dados de treino e teste
- Balanceamento de classes quando necessário
- Pipeline de preparação para garantir reprodutibilidade

### 3. Modelagem e Comparação
Foram treinados e avaliados diferentes modelos de classificação, incluindo:
- Regressão Logística
- K-Nearest Neighbors (KNN)
- Árvores de Decisão
- Random Forest
- Outros algoritmos supervisionados

### 4. Avaliação
- Métricas utilizadas:
  - Acurácia
  - Precisão
  - Recall
  - F1-score
- Comparação objetiva dos resultados entre modelos

---

## 📈 Resultados e Insights

- Diferenças significativas de desempenho entre os algoritmos
- Modelos baseados em ensemble apresentaram melhor equilíbrio entre métricas
- O pré-processamento teve impacto direto na performance final
- Nem sempre o modelo mais complexo é o mais adequado

---

## 🛠️ Tecnologias Utilizadas

- **Python**
- **Pandas**
- **NumPy**
- **Scikit-learn**
- **Matplotlib / Seaborn**
- **Jupyter Notebook**

---

## 🚀 Principais Aprendizados

- Importância de comparar múltiplos modelos antes da decisão final
- Pré-processamento adequado é decisivo para bons resultados
- Métricas devem ser analisadas em conjunto, não isoladamente
- Avaliação crítica é essencial em projetos de Machine Learning

---

📌 *Este projeto demonstra capacidade analítica em Machine Learning, com foco em comparação de modelos, avaliação crítica e boas práticas em classificação supervisionada.*
