from pyspark.sql.functions import lit
import sys
import re
from awsglue.transforms import *
from awsglue.utils import getResolvedOptions
from pyspark.context import SparkContext
from awsglue.context import GlueContext
from awsglue.job import Job
from pyspark.sql.functions import current_date

# Inicialização do contexto
sc = SparkContext()
glueContext = GlueContext(sc)
spark = glueContext.spark_session
job = Job(glueContext)

# Parâmetros do Job
args = getResolvedOptions(sys.argv, ["JOB_NAME", "S3_INPUT_PATH", "S3_TARGET_PATH"])
job.init(args["JOB_NAME"], args)

# Extração de ano, mês e dia do caminho de entrada
match = re.search(r"(\d{4})/(\d{2})/(\d{2})", args["S3_INPUT_PATH"])
ano, mes, dia = match.groups()

# Ler dados da Raw Zone (todos os arquivos JSON no caminho especificado)
df_raw = spark.read.json(args["S3_INPUT_PATH"], multiLine=True)

# Adicionar as colunas de 'ano', 'mes' e 'dia' ao DataFrame
df_raw = df_raw.withColumn("ano", lit(ano))
df_raw = df_raw.withColumn("mes", lit(mes))
df_raw = df_raw.withColumn("dia", lit(dia))

# Particionar os dados por 'ano', 'mes' e 'dia' e salvar como Parquet
df_raw.write.partitionBy("ano", "mes", "dia").mode("overwrite").parquet(
    f"{args['S3_TARGET_PATH']}"
)

# Finalizar o job
job.commit()
