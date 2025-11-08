# utilizado para separar os dados da aba agents
# exemplo de entrada: Cryocells ['brimstone', 'astra', 'jett']

import pandas as pd
import ast

df_raw = pd.read_csv("agents.csv", sep=",", dtype=str)
df_raw['agent'] = df_raw['agent'].str.strip('"')
df_raw['agent'] = df_raw['agent'].fillna('[]').apply(lambda x: ast.literal_eval(x) if x else [])
max_agents = df_raw['agent'].apply(len).max()
agents_expanded = pd.DataFrame(df_raw['agent'].tolist(),columns=[f'agent_{i+1}' for i in range(max_agents)])
df_final = pd.concat([df_raw[['playerName']], agents_expanded], axis=1)
df_final.to_csv("agents_tabela_expandidas.csv", index=False)
print(df_final.head())