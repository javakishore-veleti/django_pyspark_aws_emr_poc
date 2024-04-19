from overrides import override

from trades_ingest_forex.dtos import IngestRequestDto, IngestRequestExecCtxDto
from trades_ingest_forex.spark_utils import SparkUtils
from trades_ingest_forex.wf_tasks_util import WfTask

import logging
logger = logging.getLogger(__file__)


class CreatePySparkSession(WfTask):
    TASK_ID = "CreatePySparkSession"

    @override
    def exec_wf_task(self, ingest_dto: IngestRequestDto, exec_ctx: IngestRequestExecCtxDto):
        logger.info("Entered Creating PySpark Session")

        exec_ctx.spark_session = SparkUtils.create_pyspark_session(ingest_dto, exec_ctx)

        logger.info("Exiting Creating PySpark Session")
