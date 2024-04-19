from trades_ingest_forex.dtos import IngestRequestDto, IngestRequestExecCtxDto
import logging

from trades_ingest_forex.wf_tasks.close_pyspark_session import ClosePySparkSession
from trades_ingest_forex.wf_tasks.create_pyspark_session import CreatePySparkSession
from trades_ingest_forex.wf_tasks.exec_copy_local_2_s3 import ExecCopyLocal2S3
from trades_ingest_forex.wf_tasks_factory import WfTaskFactory

logger = logging.getLogger(__file__)

WF_TASK_IDS = [CreatePySparkSession.TASK_ID, ExecCopyLocal2S3.TASK_ID, ClosePySparkSession.TASK_ID]


class TradesIngestFacadeImpl:

    def __init__(self):
        pass

    # noinspection PyMethodMayBeStatic
    def execute_ingest(self, ingest_dto: IngestRequestDto, exec_ctx: IngestRequestExecCtxDto):
        logger.info("Entered")

        for a_wf_task in WF_TASK_IDS:
            logger.info(f"Executing WF_Task [{a_wf_task}]")
            WfTaskFactory.get_or_create_wf_task(a_wf_task).exec_wf_task(ingest_dto, exec_ctx)

        logger.info("Exiting")
