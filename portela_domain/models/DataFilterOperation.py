from enum import Enum, unique


@unique
class DataFilterOperation(Enum):
    "AND"
    "OR"
