import pandas as pd

df = pd.read_csv("VCT-Geral-Expanded.csv")

df_filtered = df[(df["region"] == "Americas") & (df["playerCategory"] == "vct-international")]

df_agents = df_filtered.melt(
    id_vars=["playerName", "team", "rating", "region", "playerCategory"],
    value_vars=["agent_1", "agent_2", "agent_3"],
    var_name="agent_slot",
    value_name="agent"
)

df_agents = df_agents.dropna(subset=["agent"])

best_by_agent = df_agents.loc[df_agents.groupby("agent")["rating"].idxmax()]

best_by_agent = best_by_agent.sort_values(by=["agent", "rating"], ascending=[True, False])
result = best_by_agent[["agent", "playerName", "team", "rating"]]

print(result.to_string(index=False))

result.to_csv("best_players_by_agent.csv", index=False, encoding="utf-8")
