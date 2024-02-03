from datetime import datetime
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
    created_at: datetime = datetime.now()
    updated_at: datetime = datetime.now()
