from overrides import override

from trades_ingest_forex.dtos import IngestRequestDto, IngestRequestExecCtxDto
from trades_ingest_forex.wf_tasks_util import WfTask
import os
import logging

logger = logging.getLogger(__file__)


class SetupHadoopConfPaths(WfTask):
    TASK_ID = "SetupHadoopConfPaths"

    @override
    def exec_wf_task(self, ingest_dto: IngestRequestDto, exec_ctx: IngestRequestExecCtxDto):
        os.environ['HADOOP_CONF_DIR'] = '/path/to/hadoop/conf'
