## 🌱 Previsão de Emissões de Gases de Efeito Estufa no Brasil

Este projeto analisa as **emissões de gases de efeito estufa no Brasil entre 1970 e 2019**, com foco no **setor de energia**, e desenvolve um **modelo preditivo** para estimar emissões futuras com base em dados históricos.

O objetivo é aplicar técnicas de **engenharia de atributos temporais** e **machine learning**, avaliando tanto os resultados quanto as **limitações do uso de modelos supervisionados em séries temporais reais**.

---

## 🎯 Problema de Negócio

- Analisar o comportamento histórico das emissões de GEE no Brasil  
- Focar nas emissões associadas ao **setor energético**
- Construir um modelo de previsão baseado em dados anuais
- Avaliar a aplicabilidade de modelos de ML em problemas temporais

---

## 📊 Conjunto de Dados

- Fonte: Base oficial de emissões brasileiras  
- Período: **1970 a 2019**
- Características:
  - Dados reais, sem tratamento artificial de outliers
  - Estrutura hierárquica de categorias (`nivel_1` a `nivel_6`)
  - Valores anuais de emissão

---

## 🧠 Metodologia

### 1. Preparação dos Dados
- Carregamento e exploração dos dados com **Pandas**
- Filtragem das emissões do **setor de energia**
- Verificação de valores nulos e consistência
- Agregação das emissões por ano

### 2. Engenharia de Atributos
Para capturar padrões temporais, foram criadas as seguintes variáveis:
- Defasagens temporais (`lag1`, `lag2`, `lag3`)
- Média móvel das emissões
- Ano como variável numérica

### 3. Modelagem
- Modelo utilizado: **XGBoost Regressor**
- Objetivo: Prever emissões anuais de gases de efeito estufa
- Treinamento realizado sobre dados históricos agregados

> ⚠️ O projeto discute explicitamente as **limitações do uso de modelos baseados em árvores para previsão de séries temporais**, especialmente em horizontes de longo prazo.

---

## 📈 Resultados e Insights

- O modelo apresentou **bom desempenho em previsões de curto prazo**
- Houve degradação de performance em mudanças abruptas de tendência
- O estudo reforça a importância de:
  - Validação adequada para séries temporais
  - Uso de modelos especializados para forecasting

---

## 🛠️ Tecnologias Utilizadas

- **Python**
- **Pandas**
- **NumPy**
- **XGBoost**
- **Scikit-learn**
- **Matplotlib**
- **Jupyter Notebook**

---

## 🚀 Principais Aprendizados

- Dados ambientais reais frequentemente violam pressupostos clássicos de ML
- Engenharia de atributos é essencial em problemas temporais
- Nem todo problema de previsão é bem resolvido com ML tradicional
- Avaliar limitações do modelo é tão importante quanto métricas de erro

---

📌 *Este projeto demonstra pensamento analítico em Ciência de Dados, combinando entendimento do domínio, modelagem e avaliação crítica dos resultados.*
