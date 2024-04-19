from trades_ingest_forex.dtos import IngestRequestDto, IngestRequestExecCtxDto
from trades_ingest_forex.trades_ingest_facade_impl import TradesIngestFacadeImpl
import logging

logger = logging.getLogger(__file__)


def run(*args):
    logger.info("Entered")

    ingest_dto = IngestRequestDto()
    exec_ctx = IngestRequestExecCtxDto()

    ingest_face = TradesIngestFacadeImpl()
    ingest_face.execute_ingest(ingest_dto, exec_ctx=exec_ctx)

    logger.info("Exiting")
