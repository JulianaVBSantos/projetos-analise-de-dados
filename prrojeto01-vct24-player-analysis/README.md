# Análise de Desempenho de Jogadores no Valorant (VCT 2024)

## Sobre o Projeto
Este projeto tem como objetivo analisar o **desempenho de jogadores brasileiros** nos torneios oficiais do **Valorant Champions Tour 2024 (VCT)**.  
A análise será feita com base em estatísticas de jogadores em diferentes competições:

- VCT International  
- VCT Game Changers  
- VCT Challengers
---

## Estrutura do Projeto
projeto-valorant 

```
/projeto-1-analise-valorant/
├── 📄 README.md                    # Este arquivo contém com a documentação do projeto.
│
├── src/                            # Pasta contendo todos os códigos-fonte em Python.
│   ├── Analise01
│       ├── best_players_by_agent.py
│       ├── best_players_by_agent.csv
│   ├── Analise02
│       ├── melhores_times_rating_kast.py
│       ├── teams_best_players_rating_kast.csv
│   ├── Analise03
│       ├── gameplayStyleBalanceIndex.py
│       ├── resultado_extremos_por_regiao.csv
│   ├── Analise04
│       ├── bests_player_region.py
│       ├── Top_7_Jogadores_por_Regiao.xlsx
│   ├── agentsDataHandler # Script da Análise 2.
│   ├── conversorJsonCSV
│   └── pStatisticsDataHandler
│
├── data/
│   ├── Statistics-Valorant.csv
│   ├── input_data
│       ├── agents
│       ├── playerStatistics 
│       ├── vct-challengers
│       ├── vct-game-changer
│       └── vct-international
│   output_data/
│       ├── playerStatistics_tabela
│       ├── vct-challengers
│       ├── vct-game-changer
│       ├── VCT-Geral-Expanded
│       └── vct-international


```
---

## Fontes de Dados
Os dados foram obtidos do Kaggle:  
🔗 [Valorant Champions Tour 2024 Dataset](https://www.kaggle.com/datasets/sauurabhkr/valorant-champions-tour-2024)

---

## Tecnologias Utilizadas
- **Python 3.10+**
- **Pandas** → manipulação de dados
- **OpenPyXL** → leitura de Excel
- **JSON** → leitura de dados originais
- **Matplotlib / Seaborn** → (para visualização, etapas futuras)

---

## Como Executar
1. Clone o repositório ou baixe os arquivos.
2. Instale as dependências:
   ```bash
   pip install pandas openpyxl
