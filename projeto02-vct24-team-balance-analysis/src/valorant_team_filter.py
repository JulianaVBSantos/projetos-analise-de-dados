import pandas as pd

excel_file = "dados.xlsx"
teams_file = "lista_times.txt"
output_file = "dados_filtrados.xlsx"

df = pd.read_excel(excel_file)

df["team"] = df["team"].astype(str).str.strip().str.lower()

with open(teams_file, "r", encoding="utf-8") as f:
    valid_teams = [line.strip().lower() for line in f]

df_filtered = df[df["team"].isin(valid_teams)]

print(f"Total de linhas antes do filtro: {len(df)}")
print(f"Total de linhas após o filtro:  {len(df_filtered)}")
print(f"Times válidos carregados:       {len(valid_teams)}\n")

df_filtered.to_excel(output_file, index=False)

print(f"Arquivo filtrado salvo como: {output_file}")