# 🔍 Comparação: Busca Sequencial vs Busca Binária

Este projeto implementa e compara os algoritmos de **busca sequencial** (`O(n)`) e **busca binária** (`O(log n)`) utilizando uma interface gráfica interativa com **Tkinter**. O foco é demonstrar, de forma prática e visual, o comportamento e desempenho desses algoritmos em diferentes tamanhos de entrada e tipos de caso.

---

## 🎯 Objetivo

Avaliar:
- Tempo de execução
- Número de posições visitadas
- Comportamento prático vs. Complexidade teórica

---

## 🖥️ Interface Gráfica

A aplicação possui uma GUI intuitiva que permite:

- Escolher entre listas de **1.000**, **10.000**, **100.000** ou um **tamanho personalizado**
- Ver os resultados para:
  - **Caso médio** (elemento presente aleatoriamente)
  - **Pior caso** (elemento inexistente)
- Observar complexidades teóricas (`O(n)`, `O(log n)`) ao lado dos resultados

---



## ⚙️ Tecnologias Utilizadas

- **Python 3.11+**
- **Tkinter** (GUI nativa)
- **time** (medições de desempenho)
- **random** (geração de alvo aleatório)

---

## 🚀 Como Executar

1. Clone o repositório:

```bash
git clone https://github.com/PedroHenriqueAraujo18/Atividade-de-Recupera-o---Avalia-o-P2.git
cd Atividade-de-Recupera-o---Avalia-o-P2

python busca_interface.py

