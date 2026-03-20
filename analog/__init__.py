from .define import define_log_model
from .models import BaseLogEntry
from .util import LogEntryKindMap

LogEntryKind = LogEntryKindMap()

__version__ = "3.0.0"


__all__ = (
    "__version__",
    "BaseLogEntry",
    "LogEntryKind",
    "define_log_model",
)
