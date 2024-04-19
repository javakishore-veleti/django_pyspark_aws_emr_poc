from trades_ingest_forex.dtos import IngestRequestDto, IngestRequestExecCtxDto
import logging

logger = logging.getLogger(__file__)


class TradesIngestFacadeImpl:

    def __init__(self):
        pass

    # noinspection PyMethodMayBeStatic
    def execute_ingest(self, ingest_dto: IngestRequestDto, exec_ctx: IngestRequestExecCtxDto):
        logger.info("Entered")

        logger.info("Exiting")
