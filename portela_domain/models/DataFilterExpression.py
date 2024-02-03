from typing import Any, Optional

from .DataFilterOperation import DataFilterOperation


class DataFilterNode:
    filter: Any
    operation: Optional[DataFilterOperation] = None
    next: Optional["DataFilterNode"] = None
