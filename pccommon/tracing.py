import os

from opencensus.ext.azure.trace_exporter import AzureExporter
from opencensus.trace.attributes_helper import COMMON_ATTRIBUTES

from pccommon.config import CommonConfig

config = CommonConfig.from_environment()


HTTP_PATH = COMMON_ATTRIBUTES["HTTP_PATH"]
HTTP_URL = COMMON_ATTRIBUTES["HTTP_URL"]
HTTP_STATUS_CODE = COMMON_ATTRIBUTES["HTTP_STATUS_CODE"]
HTTP_METHOD = COMMON_ATTRIBUTES["HTTP_METHOD"]

LIVENESS_PATH = os.getenv("APP_LIVENESS_PROBE_PATH")

exporter = (
    AzureExporter(
        connection_string=(
            f"InstrumentationKey={config.app_insights_instrumentation_key}"
        )
    )
    if config.app_insights_instrumentation_key is not None
    else None
)
