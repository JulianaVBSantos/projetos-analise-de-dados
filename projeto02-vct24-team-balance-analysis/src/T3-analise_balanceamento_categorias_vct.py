# tentativa 03 --> agrupar por categoria

import pandas as pd
import matplotlib.pyplot as plt

input_path = "indice_balanceamento_por_time.xlsx"
df = pd.read_excel(input_path)

categories = df["playerCategory"].unique()

for category in categories:
    subset = df[df["playerCategory"] == category].sort_values(by="balance_index", ascending=False)

    plt.figure(figsize=(12, 8))
    plt.barh(
        subset["team"] + " (" + subset["region"] + ")",  # Nome do time + região
        subset["balance_index"]
    )

    plt.axvline(1, linestyle="--")

    plt.legend([
        "Linha de corte (Índice = 1)\n> 1: mais agressivo\n= 1: equilibrado\n< 1: menos agressivo"
    ])

    plt.title(f"Índice de Balanceamento por Time - Categoria: {category}")
    plt.xlabel("Índice de Balanceamento (FKs / Clutches %)")
    plt.ylabel("Times (Região)")

    plt.gca().invert_yaxis()
    plt.tight_layout()
    plt.show()