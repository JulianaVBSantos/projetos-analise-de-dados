import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_excel("indice_balanceamento_por_time.xlsx")

df_sorted = df.sort_values(by="balance_index")

bottom10 = df_sorted.head(10)
top10 = df_sorted.tail(10)

def plot_group(data, title):
    plt.figure(figsize=(12, 6))
    plt.barh(data["team"] + " (" + data["region"] + ")", data["balance_index"])
    plt.axvline(1, linestyle="--")
    plt.legend(["Linha de corte (1.0)\n>1 agressivo\n=1 equilibrado\n<1 pacífico"])
    plt.title(title)
    plt.xlabel("Índice de Balanceamento (FKs / Clutches %)")
    plt.gca().invert_yaxis()
    plt.tight_layout()
    plt.show()

plot_group(bottom10, "TOP 10 Times mais Pacíficos (menor índice)")
plot_group(top10, "TOP 10 Times mais Agressivos (maior índice)")
