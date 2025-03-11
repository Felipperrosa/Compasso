import sys
from awsglue.transforms import *
from awsglue.utils import getResolvedOptions
from pyspark.context import SparkContext
from awsglue.context import GlueContext
from awsglue.job import Job
from pyspark.sql.functions import (
    current_date,
    lit,
    year,
    month,
    dayofmonth,
    split,
    explode,
    col,
    date_format,
    row_number,
    monotonically_increasing_id,
    trim,
    lower,
)
from pyspark.sql.window import Window

# Obter argumentos do job
args = getResolvedOptions(
    sys.argv, ["JOB_NAME", "S3_INPUT_PATH_1", "S3_INPUT_PATH_2", "S3_TARGET_PATH"]
)

# Criar contexto Spark e Glue
sc = SparkContext()
glueContext = GlueContext(sc)
spark = glueContext.spark_session
job = Job(glueContext)
job.init(args["JOB_NAME"], args)

# Ler os arquivos Parquet
df1 = spark.read.parquet(args["S3_INPUT_PATH_1"])
df2 = spark.read.parquet(args["S3_INPUT_PATH_2"])

# Renomear colunas para evitar problemas
df1 = df1.withColumnRenamed("paísOrigem", "pais_origem")
df2 = df2.withColumnRenamed("paísOrigem", "pais_origem")

# Padronizar tipos de colunas
df2 = df2.withColumn("tempoMinutos", df2["tempoMinutos"].cast("long"))

# Tratar a coluna 'genero'
df1 = df1.withColumn("genero", explode(col("genero")))
df2 = df2.withColumn("genero", explode(split(col("genero"), ",")))

# Adicionar colunas ausentes
for col_name in set(df1.columns) - set(df2.columns):
    df2 = df2.withColumn(col_name, lit(None))
for col_name in set(df2.columns) - set(df1.columns):
    df1 = df1.withColumn(col_name, lit(None))

# Unir os DataFrames
df = df1.unionByName(df2)

# Explodir a coluna 'pais_origem' para que cada país seja uma linha separada
df_explodido = df.withColumn("pais_origem", explode(col("pais_origem")))

# Explodir a coluna 'produtoras' para que cada produtora seja uma linha separada
df_explodido_produtoras = df_explodido.withColumn(
    "produtora", explode(col("produtoras"))
)

# Explodir a coluna 'linguasFaladas' para que cada língua seja uma linha separada
df_explodido_linguas = df_explodido_produtoras.withColumn(
    "lingua", explode(col("linguasFaladas"))
)

# Filtrar e garantir que valores nulos sejam removidos
df_explodido_linguas = df_explodido_linguas.filter(col("pais_origem").isNotNull())

# Explodir a coluna 'dataLancamentoPorPais' para acessar 'dataLancamento'
df_explodido_data = df.withColumn(
    "dataLancamento", explode(col("dataLancamentoPorPais"))
)

# Criar tabelas dimensionais com IDs sequenciais
dim_atores = (
    df.selectExpr("explode(atores) as ator")
    .selectExpr(
        "ator.nome as nome_ator",
        "ator.personagem as personagem",
        "ator.popularidade as popularidade",
    )
    .dropDuplicates()
    .withColumn("id_atores", row_number().over(Window.orderBy(lit(1))))
)

# Dimensão de países - sem data de lançamento
dim_paises = (
    df.selectExpr("explode(dataLancamentoPorPais) as data")
    .selectExpr("data.pais as pais", "data.tipo as tipo")
    .dropDuplicates()
    .withColumn("pais", trim(lower(col("pais"))))
    .withColumn("id_paises", row_number().over(Window.orderBy(lit(1))))
)

dim_diretores = (
    df.selectExpr("diretor as nome_diretor")
    .filter(col("diretor").isNotNull())
    .filter(col("diretor") != "")
    .dropDuplicates()
    .withColumn("id_diretores", row_number().over(Window.orderBy(lit(1))))
)

dim_produtoras = (
    df.selectExpr("explode(produtoras) as nome_produtora")
    .dropDuplicates()
    .withColumn("id_produtoras", row_number().over(Window.orderBy(lit(1))))
)

dim_generos = (
    df.selectExpr("genero as nome_genero")
    .dropDuplicates()
    .withColumn("id_generos", row_number().over(Window.orderBy(lit(1))))
)

dim_linguas = (
    df.selectExpr("explode(linguasFaladas) as nome_lingua")
    .dropDuplicates()
    .withColumn("id_linguas", row_number().over(Window.orderBy(lit(1))))
)

# Agora, podemos acessar o 'dataLancamento' diretamente
dim_tempo = df_explodido_data.select(
    col("dataLancamento.dataLancamento").alias(
        "data"
    ),  # Acessa o 'dataLancamento' dentro da estrutura
    year(col("dataLancamento.dataLancamento")).alias("ano"),
    month(col("dataLancamento.dataLancamento")).alias("mes"),
    dayofmonth(col("dataLancamento.dataLancamento")).alias("dia"),
    date_format(col("dataLancamento.dataLancamento"), "EEEE").alias("dia_da_semana"),
    date_format(col("dataLancamento.dataLancamento"), "MMMM").alias("nome_mes"),
).dropDuplicates()

# Criar a tabela fato associando os novos IDs e adicionando um ID único para os filmes
fato_filmes = (
    df_explodido_linguas.join(
        dim_tempo, df_explodido_linguas["anoLancamento"] == dim_tempo["ano"], "left"
    )
    .join(
        dim_diretores,
        df_explodido_linguas["diretor"] == dim_diretores["nome_diretor"],
        "left",
    )
    .join(dim_paises, df_explodido_linguas["pais_origem"] == dim_paises["pais"], "left")
    .join(
        dim_produtoras,
        df_explodido_linguas["produtora"] == dim_produtoras["nome_produtora"],
        "left",
    )
    .join(
        dim_generos,
        df_explodido_linguas["genero"] == dim_generos["nome_genero"],
        "left",
    )
    .join(
        dim_linguas,
        df_explodido_linguas["lingua"] == dim_linguas["nome_lingua"],
        "left",
    )
    .select(
        df_explodido_linguas["id"].alias("id_filmes"),
        df_explodido_linguas["tituloOriginal"],
        df_explodido_linguas["anoLancamento"],
        df_explodido_linguas["avaliacaoIMDB"],
        df_explodido_linguas["votosIMDB"],
        df_explodido_linguas["premiosIMDB"],
        df_explodido_linguas["bilheteria"],
        df_explodido_linguas["orcamento"],
        df_explodido_linguas["tempoMinutos"],
        dim_tempo["data"],
        dim_diretores["id_diretores"],
        dim_paises["id_paises"],
        dim_produtoras["id_produtoras"],
        dim_generos["id_generos"],
        dim_linguas["id_linguas"],
    )
    .dropDuplicates(["id_filmes"])
)

refined_path = args["S3_TARGET_PATH"]

# Salvar tabelas no S3
dim_atores.write.mode("overwrite").parquet(f"{refined_path}dim_atores/")
dim_tempo.write.mode("overwrite").parquet(f"{refined_path}dim_tempo/")
dim_paises.write.mode("overwrite").parquet(f"{refined_path}dim_paises/")
dim_diretores.write.mode("overwrite").parquet(f"{refined_path}dim_diretores/")
dim_produtoras.write.mode("overwrite").parquet(f"{refined_path}dim_produtoras/")
dim_generos.write.mode("overwrite").parquet(f"{refined_path}dim_generos/")
dim_linguas.write.mode("overwrite").parquet(f"{refined_path}dim_linguas/")
fato_filmes.write.mode("overwrite").parquet(f"{refined_path}fato_filmes/")

# Finalizar job
job.commit()
