from pyspark.sql import SparkSession


class IngestRequestDto:

    def __init__(self):
        self.source_path: str = ""
        self.source_path_technology: str = "s3"
        self.destination_path: str = ""
        self.destination_path_technology: str = "s3"


class IngestRequestExecCtxDto:
    def __init__(self):
        self.spark_session: SparkSession = None
        self.spark_app_name: str = "Trades_Ingest_Forex_App"
