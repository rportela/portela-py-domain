from typing import Any
from .DataFilterComparison import FilterComparison
from pydantic import BaseModel


class FilterTerm(BaseModel):
    name: str
    comparison: FilterComparison
    value: Any
