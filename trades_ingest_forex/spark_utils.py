from trades_ingest_forex.dtos import IngestRequestDto, IngestRequestExecCtxDto


class SparkUtils:

    @staticmethod
    def create_pyspark_session(ingest_dto: IngestRequestDto, exec_ctx: IngestRequestExecCtxDto):
        pass