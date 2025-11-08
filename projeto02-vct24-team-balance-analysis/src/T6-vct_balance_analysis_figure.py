import pandas as pd
import matplotlib.pyplot as plt

# Load processed file
df = pd.read_excel("indice_balanceamento_por_time.xlsx")

# Ordena do menor para o maior
df_sorted = df.sort_values(by="balance_index")

# GARANTE SOMENTE 10 TIMES, mesmo com empate
bottom10 = df_sorted.nsmallest(10, "balance_index").copy()
top10 = df_sorted.nlargest(10, "balance_index").copy()

bottom10["group"] = "Menos agressivos"
top10["group"] = "Mais agressivos"

combined = pd.concat([bottom10, top10])

# ===== PALETA VALORANT =====
valorant_red = "#FF4655"
valorant_black = "#0F1923"
valorant_white = "#ECE8E1"
valorant_accent1 = "#FF9E64"
valorant_accent2 = "#7FD1B9"

# Cores por região
region_colors = {
    region: color for region, color in zip(
        df["region"].unique(),
        [valorant_red, valorant_accent1, valorant_accent2, valorant_white]
    )
}

# Marcadores por categoria
category_markers = {
    "vct-challengers": "o",
    "vct-international": "s",
    "vct-game-changers": "X"
}

# ===== PLOT =====
plt.figure(figsize=(18, 10), facecolor=valorant_black)
ax = plt.gca()
ax.set_facecolor(valorant_black)

for _, row in combined.iterrows():
    plt.scatter(
        row["balance_index"],
        row["team"],
        color=region_colors[row["region"]],
        marker=category_markers.get(row["playerCategory"], "o"),
        s=260,
        edgecolors=valorant_white,
        linewidth=2
    )

# Linha do equilíbrio
plt.axvline(1, linestyle="--", linewidth=2, color=valorant_red)

plt.grid(True, linestyle="--", linewidth=0.5, color=valorant_white, alpha=0.25)

plt.title("Top 10 Mais Agressivos x Top 10 Menos Agressivos no VCT 2024",
          fontsize=18, color=valorant_white)

plt.xlabel("Índice de Balanceamento (FK / %Clutch)", fontsize=14, color=valorant_white)
plt.ylabel("Times", fontsize=14, color=valorant_white)

plt.xticks(color=valorant_white)
plt.yticks(color=valorant_white)

# ==== LEGENDA ====
region_legend = [
    plt.Line2D([0], [0], marker="o", color=color, label=region,
               markersize=12, markeredgecolor=valorant_white, linestyle="")
    for region, color in region_colors.items()
]

category_legend = [
    plt.Line2D([0], [0], marker=symbol, color=valorant_white, label=cat,
               markersize=10, linestyle="")
    for cat, symbol in category_markers.items()
]

legend = plt.legend(
    
    handles=region_legend + category_legend,
    title="Legenda\n\n"
          "Índice = 1 (estilo equilibrado)\n"
          "Índice > 1 (mais agressivo)\n"
          "Índice < 1 (mais reativo)\n"
          "\nCores = Região\n"
          "Marcadores = Categoria\n",    facecolor=valorant_black,
    edgecolor=valorant_white,
    labelcolor=valorant_white,
    fontsize=10, title_fontsize=12,
    bbox_to_anchor=(1.02, 1), loc="upper left"
)

for text in legend.get_texts():
    text.set_color(valorant_white)
legend.get_title().set_color(valorant_white)

plt.tight_layout()
plt.show()