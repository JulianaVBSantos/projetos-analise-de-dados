# tentativa 02 -> agrupar por região

import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_excel("indice_balanceamento_por_time.xlsx")

regions = df["region"].unique()

for region in regions:
    subset = df[df["region"] == region].sort_values(by="balance_index", ascending=False)

    plt.figure(figsize=(12, 8))
    plt.barh(
        subset["team"] + " (" + subset["playerCategory"] + ")",  # Nome do time + categoria
        subset["balance_index"]
    )

    plt.axvline(1, linestyle="--")

    plt.legend([
        "Linha de corte (Índice = 1)\n> 1: mais agressivo\n= 1: equilibrado\n< 1: menos agressivo"
    ])

    plt.title(f"Índice de Balanceamento por Time - Região: {region}")
    plt.xlabel("Índice de Balanceamento (FKs / Clutches %)")
    plt.ylabel("Times (Categoria do Jogador)")

    plt.gca().invert_yaxis()
    plt.tight_layout()

    plt.show()
