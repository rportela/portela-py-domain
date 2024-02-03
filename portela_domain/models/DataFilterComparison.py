from enum import Enum, unique


@unique
class DataFilterComparison(Enum):
    Equals = "="
    NotEquals = "!="
    GreaterThan = ">"
    LessThan = "<"
    GreaterThanOrEquals = ">="
    LessThanOrEquals = "<="
    IsNull = "IS NULL"
    IsNotNull = "IS NOT NULL"
    In = "IN"
    NotIn = "NOT IN"
    Between = "BETWEEN"
    NotBetween = "NOT BETWEEN"
    Like = "LIKE"
    NotLike = "NOT LIKE"
    ILike = "ILIKE"
    NotILike = "NOT ILIKE"
