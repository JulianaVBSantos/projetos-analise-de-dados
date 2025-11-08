# tentativa de colocar todas as regiões, todas as categorias e todos os times  em um só gráfico

import pandas as pd
import matplotlib.pyplot as plt

input_file = "dados_filtrados.xlsx"   # arquivo já filtrado
output_file = "indice_balanceamento_por_time.xlsx"

df = pd.read_excel(input_file)

df["first_kills_per_round"] = pd.to_numeric(df["first_kills_per_round"], errors="coerce").fillna(0)
df["clutch_success_percentage"] = pd.to_numeric(df["clutch_success_percentage"], errors="coerce").fillna(0)

df["balance_index"] = df.apply(
    lambda row: row["first_kills_per_round"] / row["clutch_success_percentage"]
                if row["clutch_success_percentage"] != 0 else 0,
    axis=1
)

df_avg = df.groupby(["team", "region", "playerCategory"], as_index=False)[
    ["balance_index", "first_kills_per_round", "clutch_success_percentage"]
].mean()

df_avg = df_avg.sort_values(by="balance_index", ascending=False)

plt.figure(figsize=(12, 12))

plt.barh(
    df_avg["team"] + " (" + df_avg["region"] + ")",
    df_avg["balance_index"]
)

# Linha de corte no valor 1
plt.axvline(1, linestyle="--")

plt.title("Índice de Balanceamento por Time (Agrupado por Região)\nLinha de corte = 1")
plt.xlabel("Índice de Balanceamento (FKs / Clutches %)")
plt.ylabel("Times (Região)")

plt.gca().invert_yaxis()

plt.tight_layout()
plt.show()

df_avg.to_excel(output_file, index=False)

print("Gráfico gerado!")
print(f"Arquivo salvo: {output_file}")