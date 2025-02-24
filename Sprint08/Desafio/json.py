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

match = re.search(r"(\d{4})/(\d{2})/(\d{2})", args["S3_INPUT_PATH"])
ano, mes, dia = match.groups()

# Ler dados da Raw Zone (todos os arquivos JSON no caminho especificado)
df_raw = spark.read.json(args["S3_INPUT_PATH"], multiLine=True)

# Criar caminho no S3 usando a data extraída
path = f"{args['S3_TARGET_PATH']}/{ano}/{mes}/{dia}"

# Salvar dados na Trusted Zone (Parquet, particionado por data de ingestão)
df_raw.write.mode("overwrite").parquet(path)

# Finalizar o job
job.commit()
