# utilizado para separar os dados da aba playerStatistic
# exemplo de entrada: {'average_combat_score': '186.5', 'kill_deaths': '0.93', 'kill_assists_survived_traded': '',
# 'average_damage_per_round': '108.8', 'kills_per_round': '0.68', 'assists_per_round': '0.32', 'first_kills_per_round': '0.07', 'first_deaths_per_round': '0.07',
# 'headshot_percentage': '', 'clutch_success_percentage': ''}

import pandas as pd
import json

df_raw = pd.read_csv("playerStatistics.csv", header=None, dtype=str)

linhas = df_raw.iloc[:, 0].dropna()

dicts = []
for linha in linhas:
    try:
        dicts.append(json.loads(linha.replace("'", '"')))
    except Exception as e:
        print("Erro ao processar linha:", linha)
        print("Detalhe:", e)

df_final = pd.DataFrame(dicts)

print(df_final.head())

df_final.to_csv("playerStatistics_tabela.csv", index=False)
