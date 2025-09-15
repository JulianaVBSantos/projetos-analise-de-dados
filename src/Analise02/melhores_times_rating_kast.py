import pandas as pd

df = pd.read_csv("VCT-Geral-Expanded.csv")

df_selected = df[["playerName", "rating", "kill_assists_survived_traded", "team"]].copy()

df_selected = df_selected.rename(columns={"kill_assists_survived_traded": "KAST"})

df_selected["KAST"] = df_selected["KAST"].astype(str).str.replace("%", "").astype(float)

top_rating = df_selected.sort_values(by="rating", ascending=False).head(5)

top_kast = df_selected.sort_values(by="KAST", ascending=False).head(5)

best_players = pd.concat([top_rating, top_kast]).drop_duplicates()

print("Jogadores com maior Rating ou KAST:")
print(best_players.to_string(index=False))

teams_with_best = best_players["team"].unique()
print("\nTimes com jogadores de maior impacto e consistência:")
print(teams_with_best)

best_players.to_csv("teams_best_players_rating_kast.csv", index=False, encoding="utf-8")