import pandas as pd

input_file = "dados_filtrados.xlsx"   # arquivo após filtragem de times
output_file = "indice_balanceamento_por_time.xlsx"

df = pd.read_excel(input_file)

df["first_kills_per_round"] = pd.to_numeric(df["first_kills_per_round"], errors="coerce").fillna(0)
df["clutch_success_percentage"] = pd.to_numeric(df["clutch_success_percentage"], errors="coerce").fillna(0)

df["balance_index"] = df.apply(
    lambda row: row["first_kills_per_round"] / row["clutch_success_percentage"]
                if row["clutch_success_percentage"] != 0 else 0,
    axis=1
)

df_avg = df.groupby(["team", "region", "playerCategory"], as_index=False).agg({
    "balance_index": "mean",
    "first_kills_per_round": "mean",
    "clutch_success_percentage": "mean"
})

df_avg = df_avg.sort_values(by="balance_index", ascending=False)

df_avg.to_excel(output_file, index=False)

print("\nCálculo finalizado!")
print(f"Arquivo gerado: {output_file}")
print(f"Total de equipes válidas encontradas: {len(df_avg)}")