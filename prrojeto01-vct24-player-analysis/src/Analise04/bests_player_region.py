import pandas as pd

df = pd.read_csv("VCT-Geral-Expanded.csv")

print("Colunas do DataFrame:", df.columns)

df['kill_assists_survived_traded'] = df['kill_assists_survived_traded'].replace('%', '', regex=True)  # Remove o '%'
df['kill_assists_survived_traded'] = pd.to_numeric(df['kill_assists_survived_traded'], errors='coerce')  # Converte para numérico
df['kill_assists_survived_traded'] = df['kill_assists_survived_traded'] / 100  # Converte para número decimal

df['kill_deaths'] = pd.to_numeric(df['kill_deaths'], errors='coerce')
df['kills_per_round'] = pd.to_numeric(df['kills_per_round'], errors='coerce')
df['assists_per_round'] = pd.to_numeric(df['assists_per_round'], errors='coerce')
df['average_combat_score'] = pd.to_numeric(df['average_combat_score'], errors='coerce')

df['kill_assists_survived_traded'] = df['kill_assists_survived_traded'].fillna(0)

df_sorted = df.sort_values(by=['kill_assists_survived_traded', 'average_combat_score'], ascending=False)

# Função para pegar os 7 melhores jogadores por região
def top_7_jogadores_por_regiao(df):
    top_jogadores = {}

    for region in df['region'].unique():
        region_df = df[df['region'] == region]
        top_jogadores[region] = region_df.head(7)

    return top_jogadores

melhores_jogadores = top_7_jogadores_por_regiao(df_sorted)

resultados = []
for region, players in melhores_jogadores.items():
    resultados.append(players[['playerName', 'region', 'kill_assists_survived_traded', 'average_combat_score']])

top_7_df = pd.concat(resultados)

top_7_df.to_excel("Top_7_Jogadores_por_Regiao.xlsx", index=False, engine='openpyxl')

print("Arquivo .xlsx gerado com sucesso!")