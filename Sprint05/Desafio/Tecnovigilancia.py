import boto3
import pandas as pd


# Carregar o arquivo CSV original

arquivo = "DADOS_ABERTOS_TECNOVIGILANCIA.csv"
arquivo_final = "DADOS_FILTRADOS.csv"
df = pd.read_csv(arquivo, sep=";", encoding="utf-8")

# total_rows_initial = len(df )
# print(f"Número de linhas: {total_rows_initial}")


# 1. Filtrar dados usando dois operadores lógicos
filtro_df = df[
    (df["UF_EMPRESA_NOTIFICANTE"] == "RJ") & (df["ANO_NOTIFICACAO"] <= 2022)
].copy()

# 2. Duas funções de Agregação

#  2.1 Contar ocorrencia de cada 'TIPO_NOTIFICAÇÃO'
tipo_counts = filtro_df.groupby("TIPO_NOTIFICACAO").size()
filtro_df["CONTAGEM_TIPO_NOTIFICACAO"] = filtro_df["TIPO_NOTIFICACAO"].map(tipo_counts)

# 2.2 Contar notificações por estado de ocorrência e adicionar ao DataFrame
uf_counts = filtro_df.groupby("UF_OCORRENCIA").size()
filtro_df["CONTAGEM_UF_OCORRENCIA"] = filtro_df["UF_OCORRENCIA"].map(uf_counts)

# print("\nContagem de ocorrências por TIPO_NOTIFICACAO:")
# print(tipo)

# print("\nMédia de notificações por UF_OCORRENCIA :")
# print(notificações)

# 3. Função Condicional
filtro_df["ALTO_RISCO"] = filtro_df["CLASSE_RISCO"].apply(
    lambda x: "Sim" if x in ["III", "IV"] else "Nao"
)

# print("\nNova coluna 'ALTO_RISCO' adicionada:")
# print(filtro_df [["CLASSE_RISCO", "ALTO_RISCO"]].head(50))


#  4. Função Conversão
filtro_df["DATA_NOTIFICACAO"] = pd.to_datetime(
    filtro_df["DATA_NOTIFICACAO"], errors="coerce", dayfirst=True
)

# print("\nData modificada:")
# print(filtro_df["DATA_NOTIFICACAO"].head())

# 5. Função data - Calcular a diferença entre duas datas
filtro_df["DIFERENCA_DIAS"] = (
    filtro_df["DATA_NOTIFICACAO"]
    - pd.to_datetime(filtro_df["ANO_NOTIFICACAO"].astype(str) + "-01-01")
).dt.days

# print("\nData modificada:")
# print(filtro_df ['MES_NOTIFICACAO'].head())

# # 6. Função string
filtro_df = filtro_df.replace("--", "NAO INFORMADO")
filtro_df = filtro_df.fillna("NAO INFORMADO")


filtro_df = filtro_df.sort_values(
    by=["DATA_NOTIFICACAO", "ANO_NOTIFICACAO"], ascending=True
)

filtro_df.to_csv(arquivo_final, index=False, sep=";")
print(f"Novo dataset gerado e salvo em '{arquivo_final}'")

# bucket = "meu-bucket-compasso-sprint5"

# # Configurando

# session = boto3.Session(profile_name="AdministratorAccess-442426891183")
# s3 = session.client("s3")

# try:
#     with open(arquivo_final, "rb") as data:
#         s3.upload_fileobj(data, bucket, arquivo_final)
#         print(f"Arquivo '{arquivo_final} enviado para o bucket '{bucket}!!'")
# except Exception as e:
#     print(f"Erro!{e}")
