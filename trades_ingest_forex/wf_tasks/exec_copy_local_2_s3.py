from overrides import override

from trades_ingest_forex.dtos import IngestRequestDto, IngestRequestExecCtxDto
from trades_ingest_forex.wf_tasks_util import WfTask

import logging
logger = logging.getLogger(__file__)


class ExecCopyLocal2S3(WfTask):
    TASK_ID = "ExecCopyLocal2S3"

    @override
    def exec_wf_task(self, ingest_dto: IngestRequestDto, exec_ctx: IngestRequestExecCtxDto):
        pass
