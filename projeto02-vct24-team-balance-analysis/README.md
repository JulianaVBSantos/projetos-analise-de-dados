# 🎯 VCT Team Balance Analysis  
Análise do Índice de Estilo de Jogo dos times do **Valorant Champions Tour (VCT 2024)** com visualizações personalizadas no tema do jogo.

---

## 📌 Sobre o projeto

Este projeto realiza a análise do **Índice de Balanceamento de jogo** dos times do VCT, comparando agressividade e reatividade com base nas métricas:

- **First Kills por Round**
- **% de Sucesso em Clutches**

O índice é calculado por:

Índice = First Kills por Round ÷ % Clutch

### Interpretação do índice:

| Valor do Índice | Estilo do Time |
|----------------|----------------|
| > 1.0          | Mais agressivo |
| = 1.0          | Equilibrado    |
| < 1.0          | Mais reativo (pacífico) |

---

## 📊 Visualizações disponíveis

✔ Comparação dos 10 times mais agressivos e 10 menos agressivos  
✔ Gráficos por região  
✔ Gráficos por categoria (VCT International, Challengers, Game Changers)  
✔ Scatter plot temático no estilo **Valorant**  
✔ Legendas personalizadas para região e categoria  

---

## 🧾 Estrutura dos arquivos

| Arquivo | Função |
|--------|--------|
| `valorant_team_filter.py` | Filtra apenas times válidos do dataset e gera `dados_filtrados.xlsx` |
| `team_balance_index.py` | Calcula o índice e gera `indice_balanceamento_por_time.xlsx` |
| `T1-analise_balanceamento_vct_times.py` | Gera 1 gráfico para todos os elementos inclusos |
| `T2-analise_regional_balanceamento.py` | Gera 4 gráficos por região |
| `T3-analise_balanceamento_categorias_vct.py` | Gera 3 gráficos por categoria |
| `T4-analise_top10_separado.py` | Gera 2 gráficos dos 10 mais agressivos e dos 10 mais pacíficos |
| `T5-analise_top10_juntos.py` | Cria 1 gráfico dos 10 mais agressivos vs 10 mais reativos juntos |
| `T6-vct_balance_analysis_figure.py` | Cria 1 gráfico dos 10 mais agressivos vs 10 mais reativos - aprimorado|
---

## 🚀 Como executar

### 1. Instalar dependências
pip install pandas matplotlib openpyxl
### 2. Rodar o pipeline
python valorant_team_filter.py
python team_balance_index.py
### 3. Gerar o gráfico principal
python 6-vct_balance_analysis_figure.py

🧠 Tecnologias utilizadas
Python 3.11

Pandas

Matplotlib

OpenPyXL (leitura de Excel)

🎮 Tema visual
Todos os gráficos utilizam a paleta inspirada em Valorant:

Cor	Hex
Vermelho Valorant	#FF4655
Preto	#0F1923
Branco	#ECE8E1
Acento 1	#FF9E64
Acento 2	#7FD1B9

📎 Observações
Os gráficos foram otimizados para leitura visual mesmo com grande volume de times e categorias.

Este projeto foi desenvolvido para fins acadêmicos na disciplina de Análise de Dados do curso Bacharelado em Tecnologia da Informação/UFRN

✨ Autora
👩🏻‍💻 Juliana Vieira Barbosa dos Santos