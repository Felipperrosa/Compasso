import boto3
import pandas as pd

# Criando Sessão
session = boto3.Session(profile_name="AdministratorAccess-442426891183")

s3 = session.client("s3", region_name="us-east-1")


bucket_name = "bucket-compass-sprint5"
object_name = "DADOS_ABERTOS_TECNOVIGILANCIA.csv"
path = "DADOS_ABERTOS_TECNOVIGILANCIA.csv"


# Baixando o arquivo do bucket
try:
    s3.download_file(bucket_name, object_name, path)
    print(f"Arquivo '{path}' Baixado com sucesso!!")
except Exception as e:
    print(f"Erro:{e}")


df = pd.read_csv(path, sep=";", encoding="utf-8")

# total_rows_initial = len(df )
# print(f"Número de linhas: {total_rows_initial}")


# 1. Filtrar dados usando dois operadores lógicos
filtro_df = df[
    (df["UF_EMPRESA_NOTIFICANTE"].isin(["RJ", "SP"])) & (df["ANO_NOTIFICACAO"] <= 2022)
].copy()


# 2. Duas funções de Agregação
#  2.1 Contar ocorrencia de cada 'TIPO_NOTIFICAÇÃO'
tipo_counts = filtro_df.groupby("TIPO_NOTIFICACAO").size()
filtro_df["CONTAGEM_TIPO_NOTIFICACAO"] = filtro_df["TIPO_NOTIFICACAO"].map(tipo_counts)

# 2.2 Contar notificações por 'CLASSE_RISCO' de ocorrência
uf_counts = filtro_df.groupby("CLASSE_RISCO").size()
filtro_df["CONTAGEM_UF_OCORRENCIA"] = filtro_df["CLASSE_RISCO"].map(uf_counts)


# print("\nContagem de ocorrências por TIPO_NOTIFICACAO:")
# print(tipo)

# print("\contar notificações por 'CLASSE_RISCO' de ocorrência :")
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


# 6. Função string
filtro_df = filtro_df.replace("--", "NAO INFORMADO")
filtro_df = filtro_df.fillna("NAO INFORMADO")


filtro_df = filtro_df.sort_values(
    by=["DATA_NOTIFICACAO", "ANO_NOTIFICACAO"], ascending=True
)

final_path = "DADOS_ABERTOS_TECNOVIGILANCIA_MANIPULADOS.csv"
filtro_df.to_csv(final_path, index=False, sep=";")
print(
    f"Novo dataset gerado e salvo em '{
final_path}'"
)


bucket = "bucket-compass-sprint5"

# Configurando para enviar para o s3

session = boto3.Session(profile_name="AdministratorAccess-442426891183")
s3 = session.client("s3")

try:
    with open(final_path, "rb") as data:
        s3.upload_fileobj(data, bucket, final_path)
        print(
            f"path '{
final_path} enviado para o bucket '{bucket}!!'"
        )
except Exception as e:
    print(f"Erro!{e}")
