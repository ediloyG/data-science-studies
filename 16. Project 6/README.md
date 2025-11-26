# **Projeto: Modelo de Regressão Linear (Simples e Múltipla) para Predição do Valor de Aluguel**

Este projeto aplica técnicas de **regressão linear simples e múltipla** para prever o **Valor de Aluguel** de imóveis a partir de variáveis estruturais presentes na base `ALUGUEL.csv`.

---

## 📂 1. Descrição do Projeto
A base contém dados de imóveis, incluindo:

- **Valor_Aluguel**
- **Valor_Condominio**
- **Metragem**
- **N_Quartos**
- **N_banheiros**
- **N_Suites**
- **N_Vagas**

O projeto realiza:
- Pré-processamento  
- Análise de correlação  
- Regressão Linear Simples  
- Regressão Linear Múltipla  
- Avaliação do modelo  

---

## 🔧 2. Pré-processamento
Etapas executadas:

- Leitura da base `ALUGUEL.csv`
- Conversão de variáveis numéricas originalmente como string
- Verificação de tipos
- Identificação/remoção de valores faltantes
- Separação em **treino** e **teste**

---

## 📊 3. Análise de Correlação
Principais correlações com **Valor_Aluguel**:

| Variável | Correlação |
|---------|------------|
| **Metragem** | **0.73** |
| **Valor_Condominio** | **0.69** |
| **N_Vagas** | **0.65** |
| **N_Suites** | **0.61** |
| **N_banheiros** | **0.60** |

---

## 📈 4. Regressão Linear Simples
Usando apenas **Metragem** como variável independente.

Resultados:
- **R² treino:** ~0.52  
- **R² teste:** ~0.56  

**Insight:**  
A relação existe, mas é limitada → modelo subajustado.

---

## 🧮 5. Regressão Linear Múltipla
Usando todas as variáveis independentes.

Resultados:
- **R² treino:** ~0.56  
- **R² teste:** ~0.69  

**Insight:**  
O modelo melhora significativamente e explica 69% da variação do aluguel.

---

## 🧠 6. Conclusões

- Regressão Múltipla supera Regressão Simples.
- Várias variáveis influenciam fortemente o aluguel.
- O modelo generaliza bem.
- Excelente desempenho para dados reais.

---

## 📁 7. Tecnologias
- Python  
- Pandas  
- Matplotlib  
- Seaborn  
- Scikit-learn

---

## ▶️ 8. Como Rodar
```bash
pip install pandas numpy matplotlib seaborn scikit-learn
```

Execute o notebook `Projeto6.ipynb`.

---

## 💡 9. Possíveis Extensões
- Ridge, Lasso, Elastic Net  
- Seleção automática de variáveis (VIF, Stepwise)  
- RMSE/MAE  
- Variáveis categóricas  
