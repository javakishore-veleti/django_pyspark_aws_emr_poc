from trades_ingest_forex.dtos import IngestRequestDto, IngestRequestExecCtxDto
from pyspark.sql import SparkSession


class SparkUtils:

    @staticmethod
    def create_pyspark_session(ingest_dto: IngestRequestDto, exec_ctx: IngestRequestExecCtxDto) -> SparkSession:
        # .master("local[*]") \
        spark_session = SparkSession.builder \
            .appName(exec_ctx.spark_app_name) \
            .master("local[*]") \
            .config("spark.submit.deployMode", "client") \
            .config("spark.executor.memory", "2g") \
            .config("spark.executor.cores", "2") \
            .config("spark.executor.instances", "3") \
            .getOrCreate().newSession()
        return spark_session
