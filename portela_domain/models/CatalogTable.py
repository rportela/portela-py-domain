from typing import List, Optional
from pydantic import BaseModel
from .CatalogColumn import CatalogColumn


class CatalogTable(BaseModel):
    """
    This represents a table in a dataset.
    """

    dataset_id: str
    name: str
    description: Optional[str] = None
    columns: Optional[List[CatalogColumn]] = None
    