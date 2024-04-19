from trades_ingest_forex.wf_tasks.close_pyspark_session import ClosePySparkSession
from trades_ingest_forex.wf_tasks.create_pyspark_session import CreatePySparkSession
from trades_ingest_forex.wf_tasks.exec_copy_local_2_s3 import ExecCopyLocal2S3
from trades_ingest_forex.wf_tasks.setup_hadoop_conf_paths import SetupHadoopConfPaths
from trades_ingest_forex.wf_tasks_util import WfTask


class WfTaskFactory:

    @staticmethod
    def get_or_create_wf_task(task_name: str) -> WfTask:
        match task_name:
            case SetupHadoopConfPaths.TASK_ID:
                return SetupHadoopConfPaths()
            case CreatePySparkSession.TASK_ID:
                return CreatePySparkSession()
            case ExecCopyLocal2S3.TASK_ID:
                return ExecCopyLocal2S3()
            case ClosePySparkSession.TASK_ID:
                return ClosePySparkSession()