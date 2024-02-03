from enum import Enum, unique


@unique
class OrganizationType(Enum):
    Govern = "gov"
    NonProfit = "org"
    Business = "com"
    Educational = "edu"
    Military = "mil"
    Other = "oth"
    Unknown = "unk"
