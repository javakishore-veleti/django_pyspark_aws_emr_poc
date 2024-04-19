from overrides import override

from trades_ingest_forex.dtos import IngestRequestDto, IngestRequestExecCtxDto
from trades_ingest_forex.wf_tasks_util import WfTask

import logging

logger = logging.getLogger(__file__)


class ClosePySparkSession(WfTask):
    TASK_ID = "ClosePySparkSession"

    @override
    def exec_wf_task(self, ingest_dto: IngestRequestDto, exec_ctx: IngestRequestExecCtxDto):
        logger.info("Entered")

        logger.info("Exiting")
