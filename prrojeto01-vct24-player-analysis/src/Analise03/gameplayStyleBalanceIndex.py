import pandas as pd

NOME_DO_ARQUIVO_CSV = 'VCT-Geral-Expanded.csv'
NOME_ARQUIVO_SAIDA = 'resultado_extremos_por_regiao.csv'

def analisar_extremos_por_regiao(caminho_arquivo, arquivo_saida):
    """
    Encontra o time mais agressivo e o menos agressivo de cada região principal.
    """
    try:
        df = pd.read_csv(caminho_arquivo)
        print(f"Arquivo '{caminho_arquivo}' carregado com sucesso.\n")

        df['clutch_success_percentage_numeric'] = pd.to_numeric(df['clutch_success_percentage'].str.replace('%', ''),
                                                                errors='coerce') / 100
        df_limpo = df.dropna(subset=['first_kills_per_round', 'clutch_success_percentage_numeric'])
        df_limpo = df_limpo[df_limpo['clutch_success_percentage_numeric'] > 0]
        df_limpo['indice_balanceamento'] = df_limpo['first_kills_per_round'] / df_limpo[
            'clutch_success_percentage_numeric']

        regioes_para_analisar = ['Americas', 'EMEA', 'Pacific', 'China']
        lista_de_resultados = []

        for regiao in regioes_para_analisar:
            print(f"Analisando região: {regiao}...")
            df_regiao = df_limpo[df_limpo['region'].str.lower() == regiao.lower()]

            if df_regiao.empty:
                print(f"  -> Sem dados para a região {regiao}.")
                continue

            perfil_times = df_regiao.groupby('team')['indice_balanceamento'].mean().reset_index()
            perfil_times = perfil_times.rename(columns={'indice_balanceamento': 'indice_balanceamento_medio'})

            if len(perfil_times) < 2:
                print(f"  -> Dados insuficientes para comparar times na região {regiao}.")
                continue

            time_mais_agressivo = perfil_times.loc[perfil_times['indice_balanceamento_medio'].idxmax()]

            time_menos_agressivo = perfil_times.loc[perfil_times['indice_balanceamento_medio'].idxmin()]

            lista_de_resultados.append({
                'regiao': regiao,
                'perfil': 'Mais Agressivo',
                'team': time_mais_agressivo['team'],
                'indice_balanceamento_medio': round(time_mais_agressivo['indice_balanceamento_medio'], 2)
            })
            lista_de_resultados.append({
                'regiao': regiao,
                'perfil': 'Menos Agressivo (Pacífico)',
                'team': time_menos_agressivo['team'],
                'indice_balanceamento_medio': round(time_menos_agressivo['indice_balanceamento_medio'], 2)
            })

        if not lista_de_resultados:
            print("\nNenhum resultado foi gerado. Verifique seus dados e os nomes das regiões.")
            return

        resultado_final = pd.DataFrame(lista_de_resultados)
        resultado_final.to_csv(arquivo_saida, index=False, sep=';', encoding='utf-8-sig')

        print("\n--- Análise de Extremos Concluída ---")
        print(f"O resultado foi salvo com sucesso no arquivo: '{arquivo_saida}'")
        print("\nResultado Final:")
        print(resultado_final.to_string(index=False))

    except FileNotFoundError:
        print(f"ERRO: O arquivo '{caminho_arquivo}' não foi encontrado.")
    except KeyError as e:
        print(f"ERRO: A coluna {e} não foi encontrada no arquivo.")


if __name__ == "__main__":
    analisar_extremos_por_regiao(NOME_DO_ARQUIVO_CSV, NOME_ARQUIVO_SAIDA)