import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_excel("indice_balanceamento_por_time.xlsx")

df_sorted = df.sort_values(by="balance_index")

bottom10 = df_sorted.head(10).copy()
top10 = df_sorted.tail(10).copy()

bottom10["group"] = "Menos agressivos"
top10["group"] = "Mais agressivos"

combined = pd.concat([bottom10, top10])

plt.figure(figsize=(14, 7))

for grp in combined["group"].unique():
    subset = combined[combined["group"] == grp]
    plt.scatter(subset["balance_index"], subset["team"], label=grp)

plt.axvline(1, linestyle="--")

plt.legend()

plt.title("Comparação: Top 10 Times Mais Agressivos vs. Top 10 Menos Agressivos")
plt.xlabel("Índice de Balanceamento (FKs / Clutches %)")
plt.ylabel("Times")
plt.tight_layout()
plt.show()