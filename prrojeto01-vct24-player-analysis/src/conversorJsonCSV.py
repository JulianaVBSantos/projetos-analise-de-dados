import pandas as pd
import json
import os

arquivos = ["vct-challengers.json", "vct-game-changer.json", "vct-international.json"]

for arquivo in arquivos:
    with open(arquivo, "r", encoding="utf-8") as f:
        dados = json.load(f)

    df = pd.DataFrame(dados)

    nome_csv = arquivo.replace(".json", ".csv")
    df.to_csv(nome_csv, index=False)
    print(f"{nome_csv} salvo com sucesso!")